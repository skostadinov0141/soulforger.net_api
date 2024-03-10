import { IsNotEmpty, IsString, Length, Matches } from 'class-validator';

export class UpdatePasswordDto {
	@IsNotEmpty()
	@Length(8, 128)
	@Matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])/)
	@IsString()
	newPassword: string;
}
