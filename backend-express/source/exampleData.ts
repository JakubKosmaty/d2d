import { getRepository } from 'typeorm';
import { Category } from './entity/category';
import { User } from './entity/user';
import { Item } from './entity/item';
import bcryptjs from 'bcryptjs';

const createExampleData = async () => {
    // const user = new User();

    // const salt = bcryptjs.genSaltSync(10);

    // user.name = 'David';
    // user.email = 'david@example.com';
    // user.password = bcryptjs.hashSync('123', salt);

    // await getRepository(User).save(user);

    const item1 = new Item();
    item1.name = 'Tortillas';
    item1.price = 8.0;
    item1.imageUrl = 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658';
    await getRepository(Item).save(item1);

    const item2 = new Item();
    item2.name = 'Cheeseburgers';
    item2.price = 10.0;
    item2.imageUrl = 'https://img.redro.pl/obrazy/two-tasty-cheeseburgers-with-american-cheese-700-212331665.jpg';
    await getRepository(Item).save(item2);

    const item3 = new Item();
    item3.name = 'Pizza';
    item3.price = 15.5;
    item3.imageUrl = 'https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0002/11/pizza-pepperoni.jpeg';
    await getRepository(Item).save(item3);

    const category = new Category();

    category.name = 'Main Dish';

    category.items = [item1, item2, item3];

    await getRepository(Category).save(category);
};

export default createExampleData;
