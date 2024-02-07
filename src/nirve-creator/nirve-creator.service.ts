import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { NirveCreateDto } from './dto/nirve-create.dto';
import { User } from 'src/user/schemas/user.schema';
import { Model } from 'mongoose';
import { NirvePhase1Common } from './schemas/nirve-phase-1-common.schema';
import { NirveSearchDto } from './dto/nirve-search.dto';
import { NirveTag } from '../nirve-tag/schemas/nirve-tag-schema';
import { NirveGroup } from '../nirve-group/schemas/nirve-group.schema';

@Injectable()
export class NirveCreatorService {
	constructor(
		@InjectModel(NirvePhase1Common.name)
		private nirveCommonModel: Model<NirvePhase1Common>,
		@InjectModel(User.name) private userModel: Model<User>,
		@InjectModel(NirveTag.name) private nirveTagModel: Model<any>,
		@InjectModel(NirveGroup.name) private nirveGroupModel: Model<any>,
	) {}

	async create(
		dto: NirveCreateDto,
		creatorId: string,
	): Promise<NirvePhase1Common> {
		const model = new this.nirveCommonModel(dto);
		model.createdBy = await this.userModel.findById<User>(creatorId);
		model.creationPhase = 1;
		model.tags = await this.nirveTagModel.find({
			_id: { $in: dto.tags },
		});
		model.groups = await this.nirveGroupModel.find({
			_id: { $in: dto.groups },
		});
		await model.save();
		return this.nirveCommonModel.findById(model._id);
	}

	async updateOneById(
		id: string,
		dto: NirveCreateDto,
	): Promise<NirvePhase1Common> {
		dto.tags = await this.nirveTagModel.find({
			_id: { $in: dto.tags },
		});
		return this.nirveCommonModel.findByIdAndUpdate(id, dto, { new: true });
	}

	async deleteOneById(id: string): Promise<NirvePhase1Common> {
		return this.nirveCommonModel.findByIdAndRemove(id);
	}

	async findAll(
		searchQuery: NirveSearchDto,
		limit: number,
		skip: number,
	): Promise<NirvePhase1Common[]> {
		return this.nirveCommonModel
			.find(searchQuery, null, {
				limit: limit,
				skip: skip,
			})
			.exec();
	}

	async getOneById(id: string): Promise<NirvePhase1Common> {
		return this.nirveCommonModel.findById(id, null, {
			populate: ['tags', 'groups'],
		});
	}
}
