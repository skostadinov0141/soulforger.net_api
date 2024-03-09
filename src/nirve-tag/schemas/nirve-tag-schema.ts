import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';
import { NirvePhase1Common } from '../../nirve-creator/schemas/nirve-phase-1-common.schema';
import { Model } from 'mongoose';

export type NirveTagDocument = mongoose.HydratedDocument<NirveTag>;

@Schema({ timestamps: { createdAt: 'createdAt', updatedAt: 'updatedAt' } })
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

export const NirveTagSchemaFactory = (
	commonModel: Model<NirvePhase1Common>,
) => {
	NirveTagSchema.post('deleteOne', async function () {
		const _id = this.getQuery()['_id'];
		console.log('Deleting tag with id: ', _id);
		await commonModel
			.updateMany({ tags: _id }, { $pull: { tags: _id } })
			.exec();
	});
	return NirveTagSchema;
};
