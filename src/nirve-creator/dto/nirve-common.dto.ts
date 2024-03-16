import { ApiProperty } from '@nestjs/swagger';
import { NirveTypes } from './nirve-create.dto';

export class NirveCommonDto {
	@ApiProperty()
	name: string;
	@ApiProperty()
	description: string;
	@ApiProperty()
	location: string;
	@ApiProperty()
	creationPhase: number;
	@ApiProperty()
	creatorNotes: string;
	@ApiProperty()
	type: NirveTypes;
	@ApiProperty()
	tags: string[];
	@ApiProperty()
	groups: string[];
}
