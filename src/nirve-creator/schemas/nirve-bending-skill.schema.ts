import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveBendingSkillDocument =
  mongoose.HydratedDocument<NirveBendingSkill>;

@Schema()
export class NirveBendingSkill {
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

export const NirveBendingSkillSchema =
  SchemaFactory.createForClass(NirveBendingSkill);
