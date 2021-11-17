import { Entity, Column, ManyToOne, PrimaryColumn } from 'typeorm';
import { Order } from './order';
import { Item } from './item';

@Entity()
export class OrderItemLink {
    @PrimaryColumn()
    public orderId!: number;

    @PrimaryColumn()
    public itemId!: number;

    @Column()
    public quantity!: number;

    @ManyToOne(() => Order, (order) => order.orderItemLink)
    public order!: Order;

    @ManyToOne(() => Item, (item) => item.orderItemLink)
    public item!: Item;
}
