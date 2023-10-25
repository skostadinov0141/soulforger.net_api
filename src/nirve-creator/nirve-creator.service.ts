import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { NirveBendingSkill } from './schemas/nirve-bending-skill.schema';
import { NirveCharacterClass } from './schemas/nirve-character-class.schema';
import { NirveDisadvantage } from './schemas/nirve-disadvantage.schema';
import { NirveItem } from './schemas/nirve-item.schema';
import { NirveRace } from './schemas/nirve-race.schema';
import { NirveReligion } from './schemas/nirve-religion.schema';
import { NirveSkill } from './schemas/nirve-skill.schema';
import { NirveSpell } from './schemas/nirve-spell.schema';
import { NirveCreateDto } from './dto/nirve-create.dto';

@Injectable()
export class NirveCreatorService {
  constructor(
    @InjectModel(NirveBendingSkill.name)
    private readonly nirveBendingSkillModel,
    @InjectModel(NirveCharacterClass.name)
    private readonly nirveCharacterClassModel,
    @InjectModel(NirveDisadvantage.name)
    private readonly nirveDisadvantageModel,
    @InjectModel(NirveItem.name) private readonly nirveItemModel,
    @InjectModel(NirveRace.name) private readonly nirveRaceModel,
    @InjectModel(NirveReligion.name) private readonly nirveReligionModel,
    @InjectModel(NirveSkill.name) private readonly nirveSkillModel,
    @InjectModel(NirveSpell.name) private readonly nirveSpellModel,
  ) {}

  async create(dto: NirveCreateDto, type: string): Promise<any> {
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
    return creationMap[type].save();
  }

  async updateOneById(
    id: string,
    dto: NirveCreateDto,
    type: string,
  ): Promise<any> {
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
    return updateMap[type].findByIdAndUpdate(id, dto, { new: true });
  }

  async deleteOneById(id: string, type: string): Promise<any> {
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
}
