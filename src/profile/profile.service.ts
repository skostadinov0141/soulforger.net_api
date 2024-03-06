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
		console.log(profile);
		console.log(id);
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

	async uploadProfileImage(id: string, file: Express.Multer.File): Promise<Profile> {
		const profile = await this.profileModel.findById(id).exec();
		const response = await this.cloudinaryService.uploadImage(file);
		profile.avatarUrl = response.url;
		return profile.save();
	}
}
