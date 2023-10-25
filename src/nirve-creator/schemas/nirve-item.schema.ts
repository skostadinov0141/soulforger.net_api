import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveItemDocument = mongoose.HydratedDocument<NirveItem>;

@Schema()
export class NirveItem {
  _id: string;
  @Prop()
  @ApiProperty()
  name: string;
  @Prop()
  @ApiProperty()
  description: string;
  @Prop()
  @ApiProperty()
  location: string;
}

export const NirveItemSchema = SchemaFactory.createForClass(NirveItem);
