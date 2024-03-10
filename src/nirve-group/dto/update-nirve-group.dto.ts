import { IsString, Length, MaxLength } from 'class-validator';

export class UpdateNirveGroupDto {
	@IsString()
	@Length(3, 64)
	name: string;
	@IsString()
	@MaxLength(2048)
	description: string;
	updatedAt?: Date;
}
