import {
	Body,
	Controller,
	Delete,
	Get,
	Param,
	Patch,
	Post,
	Put,
	Query,
	Req,
	UseGuards,
	UseInterceptors,
} from '@nestjs/common';
import {
	ApiBearerAuth,
	ApiOperation,
	ApiParam,
	ApiProperty,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { CreateUserDto } from './dto/create-user.dto';
import { UserService } from './user.service';
import { User } from './schemas/user.schema';
import { Request } from 'express';
import { UpdateUserDto } from 'src/auth/dto/update-user.dto';
import { SearchUserDto } from './dto/search-users.dto';
import { OwnUserGuard } from 'src/own-user/own-user.guard';
import { Roles } from 'src/auth/auth.decorator';
import { Public } from 'src/auth/public.decorator';

@ApiTags('user')
@Controller('v1/user')
export class UserController {
	constructor(private userService: UserService) {}

	@Public()
	@Post()
	@ApiOperation({ summary: 'Creates a user and their associated data' })
	async create(@Body() createUserDto: CreateUserDto): Promise<User> {
		return this.userService.create(createUserDto);
	}

	@ApiBearerAuth()
	@ApiOperation({
		summary:
			'Search through users by providing a query object in the searchQuery and/or limit + skip in the query params.',
	})
	@Roles(['admin', 'user'])
	@ApiQuery({ name: 'limit', type: Number, required: false })
	@ApiQuery({ name: 'skip', type: Number, required: false })
	@Post('search')
	async findAll(
		@Body() searchObject: SearchUserDto,
		@Query('limit') limit: number,
		@Query('skip') skip: number,
	): Promise<User[]> {
		return this.userService.findAll(searchObject, limit, skip);
	}

	@ApiBearerAuth()
	@ApiOperation({ summary: 'Find a specific user based on their ID' })
	@Roles(['admin', 'user'])
	@Get(':id')
	@ApiParam({ name: 'id', type: String })
	async findOneById(@Param('id') id: string): Promise<User> {
		return this.userService.findOneById(id);
	}

	@ApiBearerAuth()
	@ApiOperation({ summary: 'Update a specific user based on their ID' })
	@Roles(['admin', 'user'])
	@UseGuards(OwnUserGuard)
	@Patch(':id')
	@ApiParam({ name: 'id', type: String })
	async updateOneByIdParam(
		@Param('id') id: string,
		@Body() user: UpdateUserDto,
	): Promise<User> {
		return this.userService.updateOneById(id, user);
	}

	@ApiBearerAuth()
	@ApiOperation({ summary: 'Delete a specific user based on their ID' })
	@Roles(['admin', 'user'])
	@UseGuards(OwnUserGuard)
	@Delete(':id')
	@ApiParam({ name: 'id', type: String })
	async deleteById(@Param('id') id: string): Promise<User> {
		return this.userService.deleteOneById(id);
	}
}
