import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import { HydratedDocument } from 'mongoose';

export type UserDocument = HydratedDocument<User>;

@Schema()
export class User {
  _id: string;
  @ApiProperty()
  @Prop({ required: true })
  email: string;
  @ApiProperty()
  @Prop({ required: true })
  passwordHash: string;
  @ApiProperty()
  @Prop({ required: true })
  username: string;
  @ApiProperty()
  @Prop([String])
  roles: string[];
  @ApiProperty()
  @Prop()
  createdAt: Date;
  @ApiProperty()
  @Prop()
  updatedAt: Date;
}

export const UserSchema = SchemaFactory.createForClass(User);
