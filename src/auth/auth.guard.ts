import {
  CanActivate,
  ExecutionContext,
  Injectable,
  UnauthorizedException,
} from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Request } from 'express';
import { TokenDto } from './dto/token.dto';

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private jwtService: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const token = this.extractTokenFromHeader(request);
    if (!token) throw new UnauthorizedException("No token provided");
    try {
      const payload = await this.jwtService.verifyAsync<TokenDto>(token, {
        secret: process.env.JWT_SECRET,
      });
      if (!payload) throw new UnauthorizedException("Invalid token");
      if (payload.expires_at < Date.now()) throw new UnauthorizedException("Token expired");
      // We're assigning the payload to the request object here
      // so that we can access it in our route handlers
      request.user = payload;
    } catch (e) {
      throw new UnauthorizedException("Invalid token");
    }
    return true;
  }

  private extractTokenFromHeader(request: Request): string | undefined {
    const [type, token] = request.headers.authorization?.split(' ') ?? [];
    return type === 'Bearer' ? token : undefined;
  }
}
