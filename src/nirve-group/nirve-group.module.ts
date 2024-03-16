import { Module } from '@nestjs/common';
import { NirveGroupController } from './nirve-group.controller';
import { NirveGroupService } from './nirve-group.service';
import { getModelToken, MongooseModule } from '@nestjs/mongoose';
import {
	NirveGroup,
	NirveGroupSchemaFactory,
} from './schemas/nirve-group.schema';
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
				name: NirveGroup.name,
				useFactory: NirveGroupSchemaFactory,
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
	controllers: [NirveGroupController],
	providers: [NirveGroupService],
})
export class NirveGroupModule {}
