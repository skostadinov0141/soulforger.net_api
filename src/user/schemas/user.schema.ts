import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import mongoose, { HydratedDocument, Model } from 'mongoose';
import { Profile } from 'src/user/schemas/profile.schema';

export type UserDocument = HydratedDocument<User>;

@Schema({ timestamps: { createdAt: 'createdAt', updatedAt: 'updatedAt' } })
export class User {
	_id: string;
	@ApiProperty()
	@Prop({ required: true })
	email: string;
	@ApiProperty()
	@Prop({ required: true })
	passwordHash: string;
	@ApiProperty()
	@Prop({ required: true })
	username: string;
	@ApiProperty()
	@Prop([String])
	roles: string[];
	@ApiProperty()
	@Prop()
	createdAt: Date;
	@ApiProperty()
	@Prop()
	updatedAt: Date;
	@ApiProperty({ type: () => Profile })
	@Prop({ type: mongoose.Schema.Types.ObjectId, ref: 'Profile' })
	profile: Profile;
}

export const UserSchema = SchemaFactory.createForClass(User);

export const UserSchemaFactory = (profileModel: Model<Profile>) => {
	UserSchema.pre('deleteOne', function () {
		const _id = this.getQuery()['_id'];
		profileModel.deleteOne({ owner: _id }).exec();
	});
	return UserSchema;
};
