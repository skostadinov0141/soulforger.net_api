import { Module } from '@nestjs/common';
import { NirveTagService } from './nirve-tag.service';
import { NirveTagController } from './nirve-tag.controller';
import { getModelToken, MongooseModule } from '@nestjs/mongoose';
import {
	NirveTag,
	NirveTagSchema,
	NirveTagSchemaFactory,
} from './schemas/nirve-tag-schema';
import { UserSchema } from '../user/schemas/user.schema';
import {
	NirvePhase1Common,
	NirvePhase1CommonSchema,
} from '../nirve-creator/schemas/nirve-phase-1-common.schema';

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
			{ name: 'User', useFactory: () => UserSchema },
		]),
	],
	controllers: [NirveTagController],
	providers: [NirveTagService],
})
export class NirveTagModule {}
