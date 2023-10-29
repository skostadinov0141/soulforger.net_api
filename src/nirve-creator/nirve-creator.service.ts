import { Injectable } from '@nestjs/common';
import { InjectModel, ModelDefinition } from '@nestjs/mongoose';
import { NirveBendingSkill } from './schemas/nirve-bending-skill.schema';
import { NirveCharacterClass } from './schemas/nirve-character-class.schema';
import { NirveDisadvantage } from './schemas/nirve-disadvantage.schema';
import { NirveItem } from './schemas/nirve-item.schema';
import { NirveRace } from './schemas/nirve-race.schema';
import { NirveReligion } from './schemas/nirve-religion.schema';
import { NirveSkill } from './schemas/nirve-skill.schema';
import { NirveSpell } from './schemas/nirve-spell.schema';
import { NirveCreateDto } from './dto/nirve-create.dto';
import { User } from 'src/user/schemas/user.schema';
import { Model } from 'mongoose';
import { NirveCommonDto } from './dto/nirve-common.dto';

@Injectable()
export class NirveCreatorService {
	constructor(
		@InjectModel(NirveBendingSkill.name)
		private nirveBendingSkillModel: Model<NirveBendingSkill>,
		@InjectModel(NirveCharacterClass.name)
		private nirveCharacterClassModel: Model<NirveCharacterClass>,
		@InjectModel(NirveDisadvantage.name)
		private nirveDisadvantageModel: Model<NirveDisadvantage>,
		@InjectModel(NirveItem.name) private nirveItemModel: Model<NirveItem>,
		@InjectModel(NirveRace.name) private nirveRaceModel: Model<NirveRace>,
		@InjectModel(NirveReligion.name)
		private nirveReligionModel: Model<NirveReligion>,
		@InjectModel(NirveSkill.name)
		private nirveSkillModel: Model<NirveSkill>,
		@InjectModel(NirveSpell.name)
		private nirveSpellModel: Model<NirveSpell>,
		@InjectModel(User.name) private userModel: Model<User>,
	) {}

	async create(
		dto: NirveCreateDto,
		type: string,
		creatorId: string,
	): Promise<NirveCommonDto> {
		const creationMap = {
			'bending-skill': new this.nirveBendingSkillModel(dto),
			'character-class': new this.nirveCharacterClassModel(dto),
			disadvantage: new this.nirveDisadvantageModel(dto),
			item: new this.nirveItemModel(dto),
			race: new this.nirveRaceModel(dto),
			religion: new this.nirveReligionModel(dto),
			skill: new this.nirveSkillModel(dto),
			spell: new this.nirveSpellModel(dto),
		};
		creationMap[type].createdAt = new Date();
		creationMap[type].updatedAt = new Date();
		creationMap[type].createdBy =
			await this.userModel.findById<User>(creatorId);
		creationMap[type].creationPhase = 1;
		await creationMap[type].save();
		const modelMap = {
			'bending-skill': this.nirveBendingSkillModel,
			'character-class': this.nirveCharacterClassModel,
			disadvantage: this.nirveDisadvantageModel,
			item: this.nirveItemModel,
			race: this.nirveRaceModel,
			religion: this.nirveReligionModel,
			skill: this.nirveSkillModel,
			spell: this.nirveSpellModel,
		};
		return modelMap[type].findById(creationMap[type]._id);
	}

	async updateOneById(
		id: string,
		dto: NirveCreateDto,
		type: string,
	): Promise<NirveCommonDto> {
		const updateMap = {
			'bending-skill': this.nirveBendingSkillModel,
			'character-class': this.nirveCharacterClassModel,
			disadvantage: this.nirveDisadvantageModel,
			item: this.nirveItemModel,
			race: this.nirveRaceModel,
			religion: this.nirveReligionModel,
			skill: this.nirveSkillModel,
			spell: this.nirveSpellModel,
		};
		dto.updatedAt = new Date();
		return updateMap[type].findByIdAndUpdate(id, dto, { new: true });
	}

	async deleteOneById(id: string, type: string): Promise<NirveCommonDto> {
		const updateMap = {
			'bending-skill': this.nirveBendingSkillModel,
			'character-class': this.nirveCharacterClassModel,
			disadvantage: this.nirveDisadvantageModel,
			item: this.nirveItemModel,
			race: this.nirveRaceModel,
			religion: this.nirveReligionModel,
			skill: this.nirveSkillModel,
			spell: this.nirveSpellModel,
		};
		return updateMap[type].findByIdAndRemove(id);
	}

	async findAll(
		type: string,
		searchQuery: NirveCommonDto,
		limit: number,
		skip: number,
	): Promise<NirveCommonDto> {
		const updateMap = {
			'bending-skill': this.nirveBendingSkillModel,
			'character-class': this.nirveCharacterClassModel,
			disadvantage: this.nirveDisadvantageModel,
			item: this.nirveItemModel,
			race: this.nirveRaceModel,
			religion: this.nirveReligionModel,
			skill: this.nirveSkillModel,
			spell: this.nirveSpellModel,
		};
		return updateMap[type]
			.find(searchQuery, null, {
				limit: limit,
				skip: skip,
			})
			.exec();
	}

	async getOneById(id: string, type: string): Promise<NirveCommonDto> {
		const updateMap = {
			'bending-skill': this.nirveBendingSkillModel,
			'character-class': this.nirveCharacterClassModel,
			disadvantage: this.nirveDisadvantageModel,
			item: this.nirveItemModel,
			race: this.nirveRaceModel,
			religion: this.nirveReligionModel,
			skill: this.nirveSkillModel,
			spell: this.nirveSpellModel,
		};
		return updateMap[type].findById(id);
	}
}
