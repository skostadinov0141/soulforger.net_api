import { PartialType } from '@nestjs/swagger';
import { CreateNirveTagDto } from './create-nirve-tag.dto';
import { IsString, Length } from 'class-validator';

export class UpdateNirveTagDto extends PartialType(CreateNirveTagDto) {
	@IsString()
	@Length(4, 192)
	tag: string;
}
