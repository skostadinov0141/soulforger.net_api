import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UserService } from 'src/user/user.service';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';
import { TokenDto } from './dto/token.dto';

@Injectable()
export class AuthService {
  constructor(
    private userService: UserService,
    private jwtService: JwtService,
  ) {}

  async signIn(email: string, password: string): Promise<TokenDto> {
    const user = await this.userService.findOneByEmail(email);
    if (!user) {
      throw new UnauthorizedException();
    }
    if (!(await bcrypt.compare(password, user.passwordHash))) {
      throw new UnauthorizedException();
    }
    const payload = {
      sub: user._id,
      profile: user.profile._id,
      roles: user.roles,
      exp: 60 * 30,
      iat: Date.now(),
    };
    const refreshPayload = {
      sub: user._id,
      exp: 60*60*24*30,
      iat: Date.now(),
    };
    return {
      access_token: await this.jwtService.signAsync(payload),
      refresh_token: await this.jwtService.signAsync(refreshPayload),
      token_type: 'Bearer',
      expires_at: Date.now() + 60 * 30 * 1000,
    };
  }

  async refresh(refreshToken: string): Promise<TokenDto> {
    const payload = await this.jwtService.verifyAsync(refreshToken);
    const user = await this.userService.findOneById(payload.sub);
    if (!user) {
      throw new UnauthorizedException();
    }
    const newPayload = {
      sub: user._id,
      profile: user.profile._id,
      roles: user.roles,
      exp: 60 * 30,
      iat: Date.now(),
    };
    const newRefreshPayload = {
      sub: user._id,
      exp: 60*60*24*30,
      iat: Date.now(),
    };
    return {
      access_token: await this.jwtService.signAsync(newPayload),
      refresh_token: await this.jwtService.signAsync(newRefreshPayload),
      token_type: 'Bearer',
      expires_at: Date.now() + 60 * 30 * 1000,
    };
  }
}
