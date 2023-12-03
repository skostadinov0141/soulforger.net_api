import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';
import { NirveTag } from '../../nirve-tag/schemas/nirve-tag-schema';
import { NirveGroup } from '../../nirve-group/schemas/nirve-group.schema';

export type NirveBendingSkillDocument =
	mongoose.HydratedDocument<NirvePhase1Common>;

@Schema()
export class NirvePhase1Common {
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
	@Prop()
	@ApiProperty()
	creatorNotes: string;
	@Prop()
	@ApiProperty()
	type: string;
	@Prop({ type: [mongoose.Schema.Types.ObjectId], ref: 'NirveTag' })
	@ApiProperty()
	tags: NirveTag[];
	@Prop({ type: [mongoose.Schema.Types.ObjectId], ref: 'NirveGroup' })
	@ApiProperty()
	groups: NirveGroup[];
}

export const NirvePhase1CommonSchema =
	SchemaFactory.createForClass(NirvePhase1Common);
