from flask import app
from app import db

from app import Category, Delegate

db.create_all()


cat_1 = Category(name="Higher Education")
db.session.add(cat_1)
db.session.commit()

cat_2 = Category(name="Armed Forces")
db.session.add(cat_2)
db.session.commit()

del_1 = Delegate(name="Example", location="1", internalurl="example", description="Blah blah blah.")
db.session.add(del_1)
db.session.commit()
