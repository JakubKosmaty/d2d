from sqlmodel import Session

from app.database import engine
from app.models.category import Category
from app.models.category import CategoryCreate
from app.models.item import Item
from app.models.user import User
from app.models.user import UserCreate
from app.routers.auth import get_password_hash


def create_example_data():
    with Session(engine) as session:
        user = UserCreate(
            username="Tony", password=get_password_hash("123"), email="tony@gmail.com"
        )
        db_user = User.from_orm(user)
        session.add(db_user)

        categories = ["Main Dish", "Sushi", "Desserts"]

        for category_name in categories:
            category = CategoryCreate(name=category_name)
            db_category = Category.from_orm(category)
            session.add(db_category)

        db_item = Item(name="Tortillas", price=10.2, category_id=1)
        session.add(db_item)

        db_item = Item(name="Cheeseburgers", price=2.2, category_id=1)
        session.add(db_item)

        db_item = Item(name="Pizza", price=2.2, category_id=1)
        session.add(db_item)

        db_item = Item(name="Futomaki", price=50.0, category_id=2)
        session.add(db_item)

        db_item = Item(name="Hosokami", price=100.0, category_id=2)
        session.add(db_item)

        db_item = Item(name="Ice Cream", price=2.0, category_id=3)
        session.add(db_item)

        db_item = Item(name="Fruits", price=9.0, category_id=3)
        session.add(db_item)

        session.commit()
