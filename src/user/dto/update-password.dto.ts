import { Contains, IsNotEmpty, Max, Min } from 'class-validator';

export class UpdatePasswordDto {
	@IsNotEmpty()
	@Min(8)
	@Max(128)
	@Contains('(?=.*[a-z])', {})
	@Contains('(?=.*[A-Z])', {})
	@Contains('(?=.*[0-9])', {})
	@Contains('(?=.*[!@#$%^&*])', {})
	newPassword: string;
}
