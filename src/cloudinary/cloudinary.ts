import { v2 } from 'cloudinary';
import { CLOUDINARY } from './constants';
import { ConfigService } from '@nestjs/config';

export const Cloudinary = {
	provide: CLOUDINARY,
	inject: [ConfigService],
	useFactory: (configService: ConfigService) => {
		return v2.config({
			cloud_name: configService.get('CLOUDINARY_CLOUD_NAME'),
			api_key: configService.get('CLOUDINARY_API_KEY'),
			api_secret: configService.get('CLOUDINARY_API_SECRET'),
		});
	},
};
