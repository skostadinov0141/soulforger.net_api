import { IsOptional, IsString, Length, MaxLength } from 'class-validator';

export class UpdateProfileDto {
	@IsString()
	@Length(4, 32)
	@IsOptional()
	displayName?: string;

	@IsString()
	@MaxLength(2000)
	@IsOptional()
	bio?: string;

	@IsString()
	@MaxLength(32)
	@IsOptional()
	preferredLanguage?: string;

	@IsString()
	@MaxLength(64)
	@IsOptional()
	favoriteRulebook?: string;

	@IsString()
	@MaxLength(32)
	@IsOptional()
	preferredRole?: string;
}
