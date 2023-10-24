import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UserService } from 'src/user/user.service';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
  constructor(
    private userService: UserService,
    private jwtService: JwtService,
  ) {}

  async signIn(email: string, password: string): Promise<any> {
    const user = await this.userService.findOneByEmail(email);
    if (!user) {
      throw new UnauthorizedException();
    }
    if (!(await bcrypt.compare(password, user.passwordHash))) {
      throw new UnauthorizedException();
    }
    const payload = { sub: user._id, profile: user.profile._id };
    return {
      access_token: await this.jwtService.signAsync(payload),
    };
  }
}
