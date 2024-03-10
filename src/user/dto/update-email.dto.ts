import { IsEmail, IsNotEmpty, IsString } from 'class-validator';

export class UpdateEmailDto {
	@IsEmail()
	@IsNotEmpty()
	@IsString()
	newEmail: string;
}
