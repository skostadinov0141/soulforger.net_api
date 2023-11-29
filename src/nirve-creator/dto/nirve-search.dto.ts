import { ApiProperty } from '@nestjs/swagger';
import { NirveTypes } from './nirve-create.dto';

export class NirveSearchDto {
	_id: any;
	name: any;
	description: any;
	location: any;
	createdBy: any;
	createdAt: any;
	updatedAt: any;
	creationPhase: any;
	creatorNotes: string;
	type: NirveTypes;
}
