import { Module } from '@nestjs/common';
import { NirveTagService } from './nirve-tag.service';
import { NirveTagController } from './nirve-tag.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { NirveTagSchema } from './schemas/nirve-tag-schema';
import { UserSchema } from '../user/schemas/user.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{ name: 'NirveTag', schema: NirveTagSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
	],
	controllers: [NirveTagController],
	providers: [NirveTagService],
})
export class NirveTagModule {}
