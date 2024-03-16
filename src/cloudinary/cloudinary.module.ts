import { Module } from '@nestjs/common';
import { Cloudinary } from './cloudinary';
import { CloudinaryService } from './cloudinary.service';

@Module({
	providers: [Cloudinary, CloudinaryService],
	exports: [CloudinaryService, Cloudinary],
})
export class CloudinaryModule {}
