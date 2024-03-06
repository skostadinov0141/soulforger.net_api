import { Module } from '@nestjs/common';
import { ProfileController } from './profile.controller';
import { ProfileService } from './profile.service';
import { MongooseModule } from '@nestjs/mongoose';
import { ProfileSchema } from './schemas/profile.schema';
import { CloudinaryModule } from '../cloudinary/cloudinary.module';

@Module({
	imports: [
		MongooseModule.forFeature([{ name: 'Profile', schema: ProfileSchema }]),
		CloudinaryModule,
	],
	exports: [ProfileService],
	controllers: [ProfileController],
	providers: [ProfileService],
})
export class ProfileModule {}
