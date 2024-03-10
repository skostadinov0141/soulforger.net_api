import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';
import { Model } from 'mongoose';
import { NirvePhase1Common } from '../../nirve-creator/schemas/nirve-phase-1-common.schema';

export type NirveGroupDocument = mongoose.HydratedDocument<NirveGroup>;

@Schema({ timestamps: { createdAt: 'createdAt', updatedAt: 'updatedAt' } })
export class NirveGroup {
	_id: string;
	@Prop()
	@ApiProperty()
	name: string;
	@Prop()
	@ApiProperty()
	description: string;
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

export const NirveGroupSchema = SchemaFactory.createForClass(NirveGroup);

export const NirveGroupSchemaFactory = (
	commonModel: Model<NirvePhase1Common>,
) => {
	NirveGroupSchema.post('deleteOne', async function () {
		const _id = this.getQuery()['_id'];
		await commonModel
			.updateMany({ groups: _id }, { $pull: { groups: _id } })
			.exec();
	});
	return NirveGroupSchema;
};
