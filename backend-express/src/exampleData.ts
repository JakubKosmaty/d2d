import { getRepository } from 'typeorm';
import { Category } from './entity/category';
import { User } from './entity/user';
import { Item } from './entity/item';
import bcryptjs from 'bcryptjs';

const createExampleData = async () => {
    try {
        const user = new User();

        const hash = await bcryptjs.hash('123', 10);

        user.name = 'David';
        user.email = 'david@example.com';
        user.password = hash;

        await getRepository(User).save(user);

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

        const item4 = new Item();
        item4.name = 'Futomaki';
        item4.price = 50.0;
        item4.imageUrl = 'https://kaiseki.pl/wp-content/uploads/2019/07/kaiseki-menu-futomaki.jpg';
        await getRepository(Item).save(item4);

        const item5 = new Item();
        item5.name = 'Hosokami';
        item5.price = 30.0;
        item5.imageUrl = 'https://kuchnialidla.pl/img/PL/960x540/ff45002b0c10-5879e835f6fe-Kinga_Paruzel-sushi-hosomaki-futomaki-uramaki-nigiri-1250x700.jpg';
        await getRepository(Item).save(item5);

        const item6 = new Item();
        item6.name = 'Ice Cream';
        item6.price = 3.0;
        item6.imageUrl = 'https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/0C9310E2-D356-4ED3-BBA0-147E7D21C67C/Derivates/E08BD85D-9D20-471A-BE8F-990ED6E2C1C3.jpg';
        await getRepository(Item).save(item6);

        const item7 = new Item();
        item7.name = 'Fruits';
        item7.price = 2.0;
        item7.imageUrl = 'https://ellalanguage.com/blog/wp-content/uploads/2021/12/fruit_czy_fruits_blogT-740x499.jpg';
        await getRepository(Item).save(item7);

        const category = new Category();
        category.name = 'Main Dish';
        category.items = [item1, item2, item3];
        await getRepository(Category).save(category);

        const category2 = new Category();
        category2.name = 'Sushi';
        category2.items = [item4, item5];
        await getRepository(Category).save(category2);

        const category3 = new Category();
        category3.name = 'Desserts';
        category3.items = [item6, item7];
        await getRepository(Category).save(category3);
    } catch (error) {
        // console.log(error);
    }
};

export default createExampleData;
