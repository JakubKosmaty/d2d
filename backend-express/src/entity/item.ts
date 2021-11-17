import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, OneToMany } from 'typeorm';
import { Category } from './category';
import { OrderItemLink } from './orderItemLink';

@Entity()
export class Item {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;

    @Column({ type: 'float' })
    price: number;

    @Column()
    imageUrl: string;

    @ManyToOne(() => Category, (category) => category.items)
    category: Category;

    @OneToMany(() => OrderItemLink, (orderItemLink) => orderItemLink.item)
    public orderItemLink!: OrderItemLink[];
}
