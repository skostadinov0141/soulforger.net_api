import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Profile } from './schemas/profile.schema';
import { Model } from 'mongoose';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { SearchProfileDto } from './dto/search-profile.dto';

@Injectable()
export class ProfileService {
	constructor(
		@InjectModel(Profile.name) private profileModel: Model<Profile>,
	) {}

	async delete(id: string): Promise<Profile> {
		return this.profileModel.findByIdAndRemove(id);
	}

	async updateById(id: string, profile: UpdateProfileDto): Promise<Profile> {
		profile.updatedAt = new Date();
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
}
