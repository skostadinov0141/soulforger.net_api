import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { ApiProperty } from '@nestjs/swagger';
import * as mongoose from 'mongoose';
import { User } from 'src/user/schemas/user.schema';

export type ProfileDocument = mongoose.HydratedDocument<Profile>;

@Schema()
export class Profile {
	_id: string;
	@Prop()
	@ApiProperty()
	displayName: string;
	@Prop()
	@ApiProperty()
	bio: string;
	@Prop()
	@ApiProperty()
	avatarUrl: string;
	@Prop()
	@ApiProperty()
	preferredLanguage: string;
	@Prop()
	@ApiProperty()
	favoriteRulebook: string;
	@Prop()
	@ApiProperty()
	preferredRole: string;
	@Prop()
	@ApiProperty()
	createdAt: Date;
	@Prop()
	@ApiProperty()
	updatedAt: Date;
}

export const ProfileSchema = SchemaFactory.createForClass(Profile);
