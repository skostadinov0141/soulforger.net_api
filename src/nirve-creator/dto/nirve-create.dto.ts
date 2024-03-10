import { IsString, Length, MaxLength } from 'class-validator';

export class NirveCreateDto {
	@IsString()
	@Length(3, 192)
	name: string;
	@IsString()
	@MaxLength(4096)
	description: string;
	@IsString()
	@MaxLength(4096)
	creatorNotes: string;
	type: NirveTypes;
	tags: string[];
	groups: string[];
}

export type NirveTypes =
	| 'bending-skill'
	| 'character-class'
	| 'disadvantage'
	| 'item'
	| 'race'
	| 'religion'
	| 'skill'
	| 'spell';
