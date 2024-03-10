import { Injectable } from '@nestjs/common';
import { CreateNirveTagDto } from './dto/create-nirve-tag.dto';
import { UpdateNirveTagDto } from './dto/update-nirve-tag.dto';
import { InjectModel } from '@nestjs/mongoose';
import { NirveTag } from './schemas/nirve-tag-schema';
import { Model } from 'mongoose';
import { User } from '../user/schemas/user.schema';
import { SearchNirveTagDto } from './dto/search-nirve-tag.dto';

@Injectable()
export class NirveTagService {
	constructor(
		@InjectModel(NirveTag.name) private nirveTagModel: Model<NirveTag>,
		@InjectModel(User.name) private userModel: Model<User>,
	) {}

	async create(
		createNirveTagDto: CreateNirveTagDto,
		creatorId: string,
	): Promise<NirveTag> {
		const tag = new this.nirveTagModel();
		tag.tag = createNirveTagDto.tag;
		tag.createdBy = await this.userModel.findById(creatorId);
		await tag.save();
		return this.nirveTagModel.findById(tag._id);
	}

	findOne(id: string) {
		return this.nirveTagModel.findById(id);
	}

	async update(id: string, updateNirveTagDto: UpdateNirveTagDto) {
		return this.nirveTagModel.findOneAndUpdate(
			{ _id: id },
			updateNirveTagDto,
		);
	}

	remove(id: string) {
		return this.nirveTagModel.deleteOne({ _id: id });
	}

	search(searchObject: SearchNirveTagDto, limit: number, skip: number) {
		return this.nirveTagModel.find(searchObject, null, {
			limit: limit,
			skip: skip,
		});
	}
}
