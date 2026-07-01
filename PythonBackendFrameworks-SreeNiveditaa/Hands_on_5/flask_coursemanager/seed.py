from app import app
from extensions import db
from models import Department, Course

with app.app_context():
    cs = Department(
        name="Computer Science",
        head_of_dept="Dr. Smith",
        budget=500000
    )

    it = Department(
        name="Information Technology",
        head_of_dept="Dr. Johnson",
        budget=450000
    )

    db.session.add(cs)
    db.session.add(it)
    db.session.commit()

    c1 = Course(
        name="Python",
        code="CS101",
        credits=4,
        department=cs
    )

    c2 = Course(
        name="Database",
        code="CS102",
        credits=3,
        department=cs
    )

    c3 = Course(
        name="Cloud",
        code="IT101",
        credits=4,
        department=it
    )

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    print(Course.query.all())