import { Body, Controller, HttpCode, HttpStatus, Post } from '@nestjs/common';
import { AuthService } from './auth.service';
import { SignInDto } from './dto/sign-in.dto';
import { ApiTags } from '@nestjs/swagger';
import { TokenDto } from './dto/token.dto';
import { RefreshTokenDto } from './dto/refresh-token.dto';
import { Public } from './public.decorator';

@ApiTags('auth')
@Controller('v1/auth')
export class AuthController {
	constructor(private authService: AuthService) {}

	@Public()
	@HttpCode(HttpStatus.OK)
	@Post('sign-in')
	async signIn(@Body() signInDto: SignInDto): Promise<TokenDto> {
		return this.authService.signIn(signInDto.email, signInDto.password);
	}

	@Public()
	@HttpCode(HttpStatus.OK)
	@Post('refresh')
	async refreshToken(@Body() signInDto: RefreshTokenDto): Promise<TokenDto> {
		return this.authService.refresh(signInDto.refresh_token);
	}
}
