import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, OneToMany } from 'typeorm';
import { User } from './user';
import { OrderItemLink } from './orderItemLink';

@Entity()
export class Order {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    date: string;

    @ManyToOne(() => User, (user) => user.orders)
    user: User;

    @OneToMany(() => OrderItemLink, (orderItemLink) => orderItemLink.order)
    public orderItemLink!: OrderItemLink[];
}