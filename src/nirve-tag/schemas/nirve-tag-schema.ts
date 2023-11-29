import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';

export type NirveTagDocument = mongoose.HydratedDocument<NirveTag>;

@Schema()
export class NirveTag {
	_id: string;
	@Prop()
	@ApiProperty()
	tag: string;
	@Prop({ type: mongoose.Schema.Types.ObjectId, ref: 'User' })
	@ApiProperty()
	createdBy: User;
	@Prop()
	@ApiProperty()
	createdAt: Date;
	@Prop()
	@ApiProperty()
	updatedAt: Date;
}

export const NirveTagSchema = SchemaFactory.createForClass(NirveTag);
