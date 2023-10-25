import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveSkillDocument = mongoose.HydratedDocument<NirveSkill>;

@Schema()
export class NirveSkill {
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

export const NirveSkillSchema = SchemaFactory.createForClass(NirveSkill);
