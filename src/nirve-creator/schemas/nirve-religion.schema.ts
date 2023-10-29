import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';

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
  @Prop({ type: mongoose.Schema.Types.ObjectId, ref: 'User' })
  @ApiProperty()
  createdBy: User;
  @Prop()
  @ApiProperty()
  createdAt: Date;
  @Prop()
  @ApiProperty()
  updatedAt: Date;
  @Prop()
  @ApiProperty()
  creationPhase: number;
}

export const NirveReligionSchema = SchemaFactory.createForClass(NirveReligion);
