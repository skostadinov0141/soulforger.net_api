import { Module } from '@nestjs/common';
import { NirveGroupController } from './nirve-group.controller';
import { NirveGroupService } from './nirve-group.service';
import { MongooseModule } from '@nestjs/mongoose';
import { UserSchema } from '../user/schemas/user.schema';
import { NirveGroupSchema } from './schemas/nirve-group.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{ name: 'NirveGroup', schema: NirveGroupSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
	],
	controllers: [NirveGroupController],
	providers: [NirveGroupService],
})
export class NirveGroupModule {}
