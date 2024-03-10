import {
	IsEmail,
	IsNotEmpty,
	IsString,
	Length,
	Matches,
} from 'class-validator';

export class CreateUserDto {
	@IsEmail()
	@IsNotEmpty()
	@IsString()
	email: string;

	@IsString()
	@IsNotEmpty()
	@Length(8, 128)
	@Matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*+-])/)
	password: string;

	@IsString()
	@IsNotEmpty()
	@Length(5, 32)
	username: string;
}
