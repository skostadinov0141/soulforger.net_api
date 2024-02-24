import {
	CanActivate,
	ExecutionContext,
	ForbiddenException,
	Injectable,
	UnauthorizedException,
} from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Request } from 'express';
import { TokenDto } from './dto/token.dto';
import { Reflector } from '@nestjs/core';
import { Roles } from './auth.decorator';
import { IS_PUBLIC_KEY } from './public.decorator';

@Injectable()
export class AuthGuard implements CanActivate {
	constructor(
		private jwtService: JwtService,
		private reflector: Reflector,
	) {}

	async canActivate(context: ExecutionContext): Promise<boolean> {
		const isPublic = this.reflector.getAllAndOverride<boolean>(
			IS_PUBLIC_KEY,
			[context.getHandler(), context.getClass()],
		);
		if (isPublic) {
			return true;
		}
		const request = context.switchToHttp().getRequest();
		const token = this.extractTokenFromHeader(request);
		if (!token) throw new UnauthorizedException('No token provided');
		try {
			const payload = await this.jwtService.verifyAsync(token, {
				secret: process.env.JWT_SECRET,
			});
			if (!payload) throw new UnauthorizedException('Invalid token');
			if (payload.expires_at < Date.now())
				throw new UnauthorizedException('Token expired');
			// We're assigning the payload to the request object here
			// so that we can access it in our route handlers
			request.user = payload;
			const roles = this.reflector.get<string[]>(
				Roles,
				context.getHandler(),
			);
			if (!roles) return true;
			const hasRole = () =>
				payload.roles.some((role) => roles.includes(role));
			if (hasRole()) return true;
			else
				throw new ForbiddenException(
					`You don't have the required role to access this resource. Allowed roles: ${roles}. Your roles: ${payload.roles}`,
				);
		} catch (e) {
			throw e;
		}
	}

	private extractTokenFromHeader(request: Request): string | undefined {
		const [type, token] = request.headers.authorization?.split(' ') ?? [];
		return type === 'Bearer' ? token : undefined;
	}
}
