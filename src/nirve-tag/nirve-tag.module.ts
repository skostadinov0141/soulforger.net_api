import { Module } from '@nestjs/common';
import { NirveTagService } from './nirve-tag.service';
import { NirveTagController } from './nirve-tag.controller';
import { getModelToken, MongooseModule } from '@nestjs/mongoose';
import { NirveTag, NirveTagSchemaFactory } from './schemas/nirve-tag-schema';
import {
	NirvePhase1Common,
	NirvePhase1CommonSchema,
} from '../nirve-creator/schemas/nirve-phase-1-common.schema';
import { UserSchemaFactory } from '../user/schemas/user.schema';
import { Profile, ProfileSchema } from '../user/schemas/profile.schema';

@Module({
	imports: [
		MongooseModule.forFeatureAsync([
			{
				name: NirveTag.name,
				useFactory: NirveTagSchemaFactory,
				inject: [getModelToken(NirvePhase1Common.name)],
			},
			{
				name: 'NirvePhase1Common',
				useFactory: () => NirvePhase1CommonSchema,
			},
			{
				name: 'User',
				useFactory: UserSchemaFactory,
				inject: [getModelToken(Profile.name)],
			},
			{
				name: 'Profile',
				useFactory: () => ProfileSchema,
			},
		]),
	],
	controllers: [NirveTagController],
	providers: [NirveTagService],
})
export class NirveTagModule {}
