import { Module } from '@nestjs/common';
import { NirveCreatorController } from './nirve-creator.controller';
import { NirveCreatorService } from './nirve-creator.service';
import { MongooseModule } from '@nestjs/mongoose';
import { NirvePhase1CommonSchema } from './schemas/nirve-phase-1-common.schema';
import { UserSchema } from 'src/user/schemas/user.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{ name: 'NirvePhase1Common', schema: NirvePhase1CommonSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
	],
	controllers: [NirveCreatorController],
	providers: [NirveCreatorService],
})
export class NirveCreatorModule {}
