import { Injectable } from '@nestjs/common';
import { UploadApiErrorResponse, UploadApiResponse, v2 } from 'cloudinary';
import toStream = require('buffer-to-stream');
import { extractPublicId } from 'cloudinary-build-url';

@Injectable()
export class CloudinaryService {
	async uploadUserAvatarImage(
		file: Express.Multer.File,
		userId: string,
	): Promise<UploadApiResponse | UploadApiErrorResponse> {
		return new Promise((resolve, reject) => {
			const upload = v2.uploader.upload_stream(
				{
					folder: 'user-avatars',
					public_id: `${userId}-avatar`,
				},
				(error, result) => {
					if (error) return reject(error);
					resolve(result);
				},
			);
			toStream(file.buffer).pipe(upload);
		});
	}

	async deleteImage(url: string): Promise<boolean> {
		return v2.uploader.destroy(extractPublicId(url), (error, result) => {
			return new Promise((resolve, reject) => {
				if (error) reject(error);
				if (result.result !== 'ok') reject('Failed to delete image');
				resolve(true);
			});
		});
	}
}
