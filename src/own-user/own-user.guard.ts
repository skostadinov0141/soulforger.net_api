import {
	CanActivate,
	ExecutionContext,
	ForbiddenException,
	Injectable,
} from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class OwnUserGuard implements CanActivate {
	canActivate(
		context: ExecutionContext,
	): boolean | Promise<boolean> | Observable<boolean> {
		const request = context.switchToHttp().getRequest();
		const userId = request.params.id;
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
