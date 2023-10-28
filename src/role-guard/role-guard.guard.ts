import { CanActivate, ExecutionContext, ForbiddenException, Injectable } from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class RoleGuard implements CanActivate {
  constructor(private roles: string[]) {}

  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    const request = context.switchToHttp().getRequest();

    const user = request.user;

    const hasRole = () => user.roles.some((role) => this.roles.includes(role));

    if(user && user.roles && hasRole()) return true;
    else throw new ForbiddenException("You don't have the required role to access this resource");
  }
}
