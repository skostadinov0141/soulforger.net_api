import { Injectable } from '@nestjs/common';
import { InjectModel, ModelDefinition } from '@nestjs/mongoose';
import { NirveCreateDto } from './dto/nirve-create.dto';
import { User } from 'src/user/schemas/user.schema';
import { Model } from 'mongoose';
import { NirveCommonDto } from './dto/nirve-common.dto';
import { NirvePhase1Common } from './schemas/nirve-phase-1-common.schema';
import { NirveSearchDto } from './dto/nirve-search.dto';

@Injectable()
export class NirveCreatorService {
	constructor(
		@InjectModel(NirvePhase1Common.name)
		private nirveCommonModel: Model<NirvePhase1Common>,
		@InjectModel(User.name) private userModel: Model<User>,
	) {}

	async create(
		dto: NirveCreateDto,
		creatorId: string,
	): Promise<NirvePhase1Common> {
		const model = new this.nirveCommonModel(dto);
		model.createdAt = new Date();
		model.updatedAt = new Date();
		model.createdBy = await this.userModel.findById<User>(creatorId);
		model.creationPhase = 1;
		await model.save();
		return this.nirveCommonModel.findById(model._id);
	}

	async updateOneById(
		id: string,
		dto: NirveCreateDto,
	): Promise<NirvePhase1Common> {
		dto.updatedAt = new Date();
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
		return this.nirveCommonModel.findById(id);
	}
}
