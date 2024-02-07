import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { NirveGroup, NirveGroupDocument } from './schemas/nirve-group.schema';
import { Model } from 'mongoose';
import { CreateNirveGroupDto } from './dto/create-nirve-group.dto';
import { User } from '../user/schemas/user.schema';
import { UpdateNirveGroupDto } from './dto/update-nirve-group.dto';
import { SearchNirveGroupDto } from './dto/search-nirve-group.dto';

@Injectable()
export class NirveGroupService {
	constructor(
		@InjectModel(NirveGroup.name)
		private readonly nirveGroupModel: Model<NirveGroupDocument>,
		@InjectModel(User.name) private readonly userModel: Model<User>,
	) {}

	async create(
		dto: CreateNirveGroupDto,
		creatorId: string,
	): Promise<NirveGroup> {
		const group = new this.nirveGroupModel();
		group.name = dto.name;
		group.description = dto.description;
		group.createdBy = await this.userModel.findById(creatorId);
		await group.save();
		return this.nirveGroupModel.findById(group._id);
	}

	async getById(id: string): Promise<NirveGroup> {
		return this.nirveGroupModel.findById(id);
	}

	async updateById(
		id: string,
		dto: UpdateNirveGroupDto,
	): Promise<NirveGroup> {
		return this.nirveGroupModel.findByIdAndUpdate(id, dto, { new: true });
	}

	async deleteById(id: string): Promise<NirveGroup> {
		return this.nirveGroupModel.findByIdAndDelete(id);
	}

	async search(
		dto: SearchNirveGroupDto,
		limit: number,
		skip: number,
	): Promise<NirveGroup[]> {
		return this.nirveGroupModel.find(dto, null, {
			limit: limit,
			skip: skip,
		});
	}
}
