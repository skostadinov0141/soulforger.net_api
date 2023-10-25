import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';

export type NirveRaceDocument = mongoose.HydratedDocument<NirveRace>;

@Schema()
export class NirveRace {
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

export const NirveRaceSchema = SchemaFactory.createForClass(NirveRace);
