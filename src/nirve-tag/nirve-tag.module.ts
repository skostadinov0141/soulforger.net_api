import { Module } from '@nestjs/common';
import { NirveTagService } from './nirve-tag.service';
import { NirveTagController } from './nirve-tag.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { NirveTag, NirveTagSchema } from './schemas/nirve-tag-schema';
import { UserSchema } from '../user/schemas/user.schema';
import {
	NirvePhase1Common,
	NirvePhase1CommonSchema,
} from '../nirve-creator/schemas/nirve-phase-1-common.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{
				name: NirveTag.name,
				schema: NirveTagSchema,
			},
		]),
		MongooseModule.forFeature([
			{ name: 'NirvePhase1Common', schema: NirvePhase1CommonSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
	],
	controllers: [NirveTagController],
	providers: [NirveTagService],
})
export class NirveTagModule {}
