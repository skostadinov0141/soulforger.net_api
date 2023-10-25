import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveCharacterClassDocument =
  mongoose.HydratedDocument<NirveCharacterClass>;

@Schema()
export class NirveCharacterClass {
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

export const NirveCharacterClassSchema =
  SchemaFactory.createForClass(NirveCharacterClass);
