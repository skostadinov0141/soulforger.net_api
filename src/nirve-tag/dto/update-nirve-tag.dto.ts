import { PartialType } from '@nestjs/swagger';
import { CreateNirveTagDto } from './create-nirve-tag.dto';

export class UpdateNirveTagDto extends PartialType(CreateNirveTagDto) {
	tag: string;
	updatedAt: Date;
}
