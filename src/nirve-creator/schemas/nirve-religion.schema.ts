import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveReligionDocument = mongoose.HydratedDocument<NirveReligion>;

@Schema()
export class NirveReligion {
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

export const NirveReligionSchema = SchemaFactory.createForClass(NirveReligion);
