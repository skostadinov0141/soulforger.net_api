import { Module } from '@nestjs/common';
import { NirveCreatorController } from './nirve-creator.controller';
import { NirveCreatorService } from './nirve-creator.service';
import { MongooseModule } from '@nestjs/mongoose';
import { NirvePhase1CommonSchema } from './schemas/nirve-phase-1-common.schema';
import { UserSchema } from 'src/user/schemas/user.schema';
import { NirveTagSchema } from '../nirve-tag/schemas/nirve-tag-schema';
import {
	NirveGroup,
	NirveGroupSchema,
} from '../nirve-group/schemas/nirve-group.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{ name: 'NirvePhase1Common', schema: NirvePhase1CommonSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
		MongooseModule.forFeature([
			{ name: 'NirveTag', schema: NirveTagSchema },
		]),
		MongooseModule.forFeature([
			{ name: NirveGroup.name, schema: NirveGroupSchema },
		]),
	],
	controllers: [NirveCreatorController],
	providers: [NirveCreatorService],
})
export class NirveCreatorModule {}
