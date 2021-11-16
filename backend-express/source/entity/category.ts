import { Entity, Column, PrimaryGeneratedColumn, OneToMany } from 'typeorm';
import { Item } from './item';

@Entity()
export class Category {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;

    @OneToMany(() => Item, (item) => item.category)
    items: Item[];
}
