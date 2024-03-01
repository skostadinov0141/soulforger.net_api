import { Module } from '@nestjs/common';
import { NirveCreatorController } from './nirve-creator.controller';
import { NirveCreatorService } from './nirve-creator.service';
import { getModelToken, MongooseModule } from '@nestjs/mongoose';
import {
	NirvePhase1Common,
	NirvePhase1CommonSchema,
} from './schemas/nirve-phase-1-common.schema';
import { UserSchema } from 'src/user/schemas/user.schema';
import { NirveTagSchemaFactory } from '../nirve-tag/schemas/nirve-tag-schema';
import {
	NirveGroup,
	NirveGroupSchemaFactory,
} from '../nirve-group/schemas/nirve-group.schema';

@Module({
	imports: [
		MongooseModule.forFeatureAsync([
			{
				name: 'NirveTag',
				useFactory: NirveTagSchemaFactory,
				inject: [getModelToken(NirvePhase1Common.name)],
			},
			{
				name: NirveGroup.name,
				useFactory: NirveGroupSchemaFactory,
				inject: [getModelToken(NirvePhase1Common.name)],
			},
			{ name: 'User', useFactory: () => UserSchema },
			{
				name: 'NirvePhase1Common',
				useFactory: () => NirvePhase1CommonSchema,
			},
		]),
	],
	controllers: [NirveCreatorController],
	providers: [NirveCreatorService],
})
export class NirveCreatorModule {}
