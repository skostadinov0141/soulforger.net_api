import { ApiHideProperty } from '@nestjs/swagger';

export class NirveCreateDto {
	name: string;
	description: string;
	@ApiHideProperty()
	updatedAt: Date;
	creatorNotes: string;
	type: NirveTypes;
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
