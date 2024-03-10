import { IsString, Length } from 'class-validator';

export class CreateNirveTagDto {
	@IsString()
	@Length(4, 192)
	tag: string;
}
