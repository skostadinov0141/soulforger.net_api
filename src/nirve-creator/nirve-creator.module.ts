import { Module } from '@nestjs/common';
import { NirveCreatorController } from './nirve-creator.controller';
import { NirveCreatorService } from './nirve-creator.service';
import { MongooseModule } from '@nestjs/mongoose';
import { NirveBendingSkillSchema } from './schemas/nirve-bending-skill.schema';
import { NirveCharacterClassSchema } from './schemas/nirve-character-class.schema';
import { NirveRaceSchema } from './schemas/nirve-race.schema';
import { NirveDisadvantageSchema } from './schemas/nirve-disadvantage.schema';
import { NirveItemSchema } from './schemas/nirve-item.schema';
import { NirveReligionSchema } from './schemas/nirve-religion.schema';
import { NirveSkillSchema } from './schemas/nirve-skill.schema';
import { NirveSpellSchema } from './schemas/nirve-spell.schema';
import { UserSchema } from 'src/user/schemas/user.schema';

@Module({
	imports: [
		MongooseModule.forFeature([
			{ name: 'NirveBendingSkill', schema: NirveBendingSkillSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveCharacterClass', schema: NirveCharacterClassSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveDisadvantage', schema: NirveDisadvantageSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveItem', schema: NirveItemSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveRace', schema: NirveRaceSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveReligion', schema: NirveReligionSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveSkill', schema: NirveSkillSchema },
		]),
		MongooseModule.forFeature([
			{ name: 'NirveSpell', schema: NirveSpellSchema },
		]),
		MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
	],
	controllers: [NirveCreatorController],
	providers: [NirveCreatorService],
})
export class NirveCreatorModule {}
