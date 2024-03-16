import { IsString, Length, MaxLength } from 'class-validator';

export class UpdateProfileDto {
	@IsString()
	@Length(4, 32)
	displayName?: string;

	@IsString()
	@MaxLength(2000)
	bio?: string;

	@IsString()
	@MaxLength(32)
	preferredLanguage?: string;

	@IsString()
	@MaxLength(64)
	favoriteRulebook?: string;

	@IsString()
	@MaxLength(32)
	preferredRole?: string;

	updatedAt?: Date;
}
