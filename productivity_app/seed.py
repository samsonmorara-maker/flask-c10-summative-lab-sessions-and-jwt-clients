from app import app
from extensions import db
from models import User, Note


with app.app_context():
    print("Clearing database...")
    Note.query.delete()
    User.query.delete()
    print("Creating users...")
    user1 = User(
        username="john",
        email="john@test.com"
    )
    user1.set_password("password123")
    user2 = User(
        username="mary",
        email="mary@test.com"
    )

    user2.set_password("password123")
    db.session.add_all([
        user1,
        user2
    ])
    db.session.commit()
    print("Creating notes...")
    note1 = Note(
        title="Workout Plan",
        content="Run 5km and do strength training",
        user_id=user1.id
    )
    note2 = Note(
        title="Daily Goals",
        content="Finish Flask API project",
        user_id=user1.id
    )
    note3 = Note(
        title="Shopping List",
        content="Buy groceries",
        user_id=user2.id
    )
    db.session.add_all([
        note1,
        note2,
        note3
    ])
    db.session.commit()
    print("Seed complete!")