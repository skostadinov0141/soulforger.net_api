import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveSpellDocument = mongoose.HydratedDocument<NirveSpell>;

@Schema()
export class NirveSpell {
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

export const NirveSpellSchema = SchemaFactory.createForClass(NirveSpell);
