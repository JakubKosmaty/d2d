from sqlmodel import Session

from d2d.database import engine
from d2d.models.category import Category
from d2d.models.category import CategoryCreate
from d2d.models.item import Item
from d2d.models.user import User
from d2d.models.user import UserCreate
from d2d.models.code import CodeCreate
from d2d.models.code import Code
from d2d.routers.auth import get_password_hash


def create_example_data():
    with Session(engine) as session:
        user = UserCreate(
            name='David', email="david@example.com", password=get_password_hash("123")
        )
        db_user = User.from_orm(user)
        session.add(db_user)

        categories = ["Main Dish", "Sushi", "Desserts"]

        for category_name in categories:
            category = CategoryCreate(name=category_name)
            db_category = Category.from_orm(category)
            session.add(db_category)

        db_item = Item(name="Tortillas", price=8.0, category_id=1, image_url='https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658')
        session.add(db_item)

        db_item = Item(name="Cheeseburgers", price=10.0, category_id=1, image_url='https://img.redro.pl/obrazy/two-tasty-cheeseburgers-with-american-cheese-700-212331665.jpg')
        session.add(db_item)

        db_item = Item(name="Pizza", price=15.5, category_id=1, image_url='https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0002/11/pizza-pepperoni.jpeg')
        session.add(db_item)

        db_item = Item(name="Futomaki", price=50.0, category_id=2, image_url='https://kaiseki.pl/wp-content/uploads/2019/07/kaiseki-menu-futomaki.jpg')
        session.add(db_item)

        db_item = Item(name="Hosokami", price=30.0, category_id=2, image_url='https://kuchnialidla.pl/img/PL/960x540/ff45002b0c10-5879e835f6fe-Kinga_Paruzel-sushi-hosomaki-futomaki-uramaki-nigiri-1250x700.jpg')
        session.add(db_item)

        db_item = Item(name="Ice Cream", price=3.0, category_id=3, image_url='https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/0C9310E2-D356-4ED3-BBA0-147E7D21C67C/Derivates/E08BD85D-9D20-471A-BE8F-990ED6E2C1C3.jpg')
        session.add(db_item)

        db_item = Item(name="Fruits", price=2.0, category_id=3, image_url='https://ellalanguage.com/blog/wp-content/uploads/2021/12/fruit_czy_fruits_blogT-740x499.jpg')
        session.add(db_item)

        code = Code(code='STYCZEN15', discount=15)
        db_code = Code.from_orm(code)
        session.add(db_code)

        session.commit()
