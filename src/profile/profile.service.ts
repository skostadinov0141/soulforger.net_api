import { Inject, Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Profile } from './schemas/profile.schema';
import { Model } from 'mongoose';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { SearchProfileDto } from './dto/search-profile.dto';
import { CloudinaryService } from '../cloudinary/cloudinary.service';

@Injectable()
export class ProfileService {
	constructor(
		@InjectModel(Profile.name) private profileModel: Model<Profile>,
		@Inject(CloudinaryService) private cloudinaryService: CloudinaryService,
	) {}

	async delete(id: string): Promise<Profile> {
		return this.profileModel.findByIdAndRemove(id);
	}

	async updateById(id: string, profile: UpdateProfileDto): Promise<Profile> {
		return this.profileModel.findByIdAndUpdate(id, profile, { new: true });
	}

	async findOneById(id: string): Promise<Profile> {
		return this.profileModel.findById(id);
	}

	async findAll(
		searchQuery: SearchProfileDto,
		limit: number,
		skip: number,
	): Promise<Profile[]> {
		return this.profileModel
			.find(searchQuery, null, { limit: limit, skip: skip })
			.exec();
	}

	async uploadProfileImage(
		ownerId: string,
		file: Express.Multer.File,
	): Promise<Profile> {
		const response = await this.cloudinaryService.uploadUserAvatarImage(
			file,
			ownerId,
		);
		const updatedDoc = await this.profileModel.findOneAndUpdate(
			{ owner: ownerId },
			{ avatarUrl: response.url },
			{ new: true },
		);
		console.log(updatedDoc);
		return updatedDoc;
	}
}
