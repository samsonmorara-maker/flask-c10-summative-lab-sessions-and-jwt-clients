from flask import request, jsonify

from app import app
from extensions import db

from models import User, Note

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Productivity API running"
    })


# Register User
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")


    if not username or not email or not password:
        return jsonify({
            "error": "All fields are required"
        }), 400


    existing_user = User.query.filter(
        (User.username == username) |
        (User.email == email)
    ).first()
    if existing_user:
        return jsonify({
            "error": "Username or email already exists"
        }), 400

    user = User(
        username=username,
        email=email
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "message": "User created successfully"
    }), 201



# Login User
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(
        email=email
    ).first()
    if not user or not user.check_password(password):
        return jsonify({
            "error": "Invalid email or password"
        }), 401
    token = create_access_token(
        identity=user.id
    )
    return jsonify({
        "access_token": token,
        "user": user.to_dict()
    }), 200



# Check Current User
@app.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "error": "User not found"
        }), 404


    return jsonify(
        user.to_dict()
    ), 200

@app.route("/notes", methods=["GET"])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()
    page = request.args.get(
        "page",
        1,
        type=int
    )
    per_page = request.args.get(
        "per_page",
        10,
        type=int
    )
    notes = Note.query.filter_by(
        user_id=user_id
    ).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    return jsonify({
        "items": [
            note.to_dict()
            for note in notes.items
        ],
        "page": notes.page,
        "pages": notes.pages,
        "total": notes.total
    }), 200

@app.route("/notes", methods=["POST"])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    if not title or not content:
        return jsonify({
            "error": "Title and content required"
        }), 400
    note = Note(
        title=title,
        content=content,
        user_id=user_id
    )
    db.session.add(note)
    db.session.commit()
    return jsonify(
        note.to_dict()
    ), 201

@app.route("/notes/<int:id>", methods=["PATCH"])
@jwt_required()
def update_note(id):
    user_id = get_jwt_identity()
    note = Note.query.filter_by(
        id=id,
        user_id=user_id
    ).first()
    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404
    data = request.get_json()
    if "title" in data:
        note.title = data["title"]
    if "content" in data:
        note.content = data["content"]
    db.session.commit()
    return jsonify(
        note.to_dict()
    ), 200

@app.route("/notes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_note(id):
    user_id = get_jwt_identity()
    note = Note.query.filter_by(
        id=id,
        user_id=user_id
    ).first()
    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({
        "message": "Note deleted successfully"
    }), 200