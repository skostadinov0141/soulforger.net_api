import {
	Body,
	Controller,
	Delete,
	Get,
	Param,
	Patch,
	Post,
	Query,
	UploadedFile,
	UseGuards,
	UseInterceptors,
} from '@nestjs/common';
import {
	ApiBearerAuth,
	ApiBody,
	ApiConsumes,
	ApiOperation,
	ApiParam,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { CreateUserDto } from './dto/create-user.dto';
import { UserService } from './user.service';
import { User } from './schemas/user.schema';
import { SearchUserDto } from './dto/search-users.dto';
import { OwnUserGuard } from 'src/own-user/own-user.guard';
import { Roles } from 'src/auth/auth.decorator';
import { Public } from 'src/auth/public.decorator';
import { Profile } from './schemas/profile.schema';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { UpdatePasswordDto } from './dto/update-password.dto';
import { UpdateEmailDto } from './dto/update-email.dto';
import { FileInterceptor } from '@nestjs/platform-express';

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
	@ApiOperation({ summary: 'Delete a specific user based on their ID' })
	@Roles(['admin', 'user'])
	@UseGuards(OwnUserGuard)
	@Delete(':id')
	@ApiParam({ name: 'id', type: String })
	async deleteById(@Param('id') id: string) {
		return this.userService.deleteOneById(id);
	}

	@ApiBearerAuth()
	@UseGuards(OwnUserGuard)
	@ApiOperation({ summary: "Change a user's password" })
	@Roles(['admin', 'user'])
	@Patch(':id/update-password')
	@ApiParam({ name: 'id', type: String })
	async updatePassword(
		@Param('id') id: string,
		@Body() updatePasswordDTO: UpdatePasswordDto,
	): Promise<User> {
		return this.userService.updatePassword(
			id,
			updatePasswordDTO.newPassword,
		);
	}

	@ApiBearerAuth()
	@UseGuards(OwnUserGuard)
	@ApiOperation({ summary: "Change a user's email address" })
	@Roles(['admin', 'user'])
	@Patch(':id/update-email')
	@ApiParam({ name: 'id', type: String })
	async updateEMail(
		@Param('id') id: string,
		@Body() updateEmailDto: UpdateEmailDto,
	): Promise<User> {
		return this.userService.updateEMail(id, updateEmailDto.newEmail);
	}

	@Public()
	@ApiOperation({ summary: "Get a user's profile based on the user's ID" })
	@Roles(['admin', 'user'])
	@Get(':id/profile')
	@ApiParam({ name: 'id', type: String })
	async getProfile(@Param('id') id: string): Promise<Profile> {
		return this.userService.getUserProfile(id);
	}

	@ApiBearerAuth()
	@UseGuards(OwnUserGuard)
	@ApiOperation({ summary: "Update a user's profile." })
	@Roles(['admin', 'user'])
	@Patch(':id/profile')
	@ApiParam({ name: 'id', type: String })
	async updateProfile(
		@Param('id') id: string,
		@Body() updateProfileDTO: UpdateProfileDto,
	): Promise<Profile> {
		return this.userService.updateProfile(id, updateProfileDTO);
	}

	@ApiBearerAuth()
	@ApiConsumes('multipart/form-data')
	@UseInterceptors(FileInterceptor('avatar'))
	@ApiBody({
		schema: {
			type: 'object',
			properties: {
				avatar: {
					type: 'string',
					format: 'binary',
				},
			},
		},
	})
	@UseGuards(OwnUserGuard)
	@ApiOperation({ summary: "Update a user's avatar image." })
	@Roles(['admin', 'user'])
	@Patch(':id/profile/update-avatar')
	@ApiParam({ name: 'id', type: String })
	async updateProfileAvatar(
		@Param('id') id: string,
		@UploadedFile() avatar: Express.Multer.File,
	): Promise<Profile> {
		return this.userService.updateAvatar(id, avatar);
	}

	@ApiBearerAuth()
	@UseGuards(OwnUserGuard)
	@ApiOperation({ summary: "Delete a user's avatar" })
	@Roles(['admin', 'user'])
	@Patch(':id/profile/delete-avatar')
	@ApiParam({ name: 'id', type: String })
	async deleteProfileAvatar(@Param('id') id: string): Promise<Profile> {
		return this.userService.deleteAvatar(id);
	}
}
