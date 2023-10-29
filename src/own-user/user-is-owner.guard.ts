import {
	CanActivate,
	ExecutionContext,
	ForbiddenException,
	Injectable,
} from '@nestjs/common';
import { Request } from 'express';
import { Observable } from 'rxjs';

@Injectable()
export class UserIsOwnerGuard implements CanActivate {
	canActivate(
		context: ExecutionContext,
	): boolean | Promise<boolean> | Observable<boolean> {
		const request = context.switchToHttp().getRequest();
		const userId = request.body.owner;
		const user = request.user;
		if (userId === user.sub.toString()) {
			return true;
		} else if (user.roles.includes('admin')) {
			return true;
		} else {
			throw new ForbiddenException(
				"You don't have permission to access this resource",
			);
		}
	}
}
