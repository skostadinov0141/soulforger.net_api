import {
	Body,
	Controller,
	Get,
	Param,
	Patch,
	Post,
	Query,
	Req,
	UploadedFile,
	UseGuards,
	UseInterceptors,
} from '@nestjs/common';
import { ProfileService } from './profile.service';
import {
	ApiBearerAuth,
	ApiBody,
	ApiConsumes,
	ApiOperation,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { UserIsOwnerGuard } from 'src/own-user/user-is-owner.guard';
import { SearchProfileDto } from './dto/search-profile.dto';
import { FileInterceptor } from '@nestjs/platform-express';

@ApiTags('Profile')
@Controller('v1/profile')
@ApiBearerAuth()
export class ProfileController {
	constructor(private profileService: ProfileService) {}

	@ApiOperation({
		summary:
			'Get all profiles that a certain optional query applies to. Limit and skip can be provided for pagination.',
	})
	@ApiQuery({ name: 'limit', type: Number, required: false })
	@ApiQuery({ name: 'skip', type: Number, required: false })
	@ApiBody({ type: SearchProfileDto })
	@Post('search')
	async findOne(
		@Query('limit') limit: number,
		@Query('skip') skip: number,
		@Body() searchQuery: SearchProfileDto,
	) {
		return this.profileService.findAll(searchQuery, limit, skip);
	}

	@ApiOperation({ summary: 'Get a Profile based on its ID' })
	@Get(':id')
	async findOneById(@Param('id') profileId: string) {
		return this.profileService.findOneById(profileId);
	}

	@ApiOperation({ summary: 'Update a Profile based on its ID' })
	@UseGuards(UserIsOwnerGuard)
	@Patch(':id')
	async update(
		@Param('id') profileId: string,
		@Body() profile: UpdateProfileDto,
	) {
		return this.profileService.updateById(profileId, profile);
	}

	@ApiOperation({
		summary: 'Upload or update the profile picture of a user.',
	})
	@UseInterceptors(FileInterceptor('file'))
	@ApiConsumes('multipart/form-data')
	@ApiBody({
		schema: {
			type: 'object',
			properties: {
				file: {
					type: 'string',
					format: 'binary',
				},
			},
		},
	})
	@Post('avatar')
	async uploadProfileImage(
		@UploadedFile() file: Express.Multer.File,
		@Req() req,
	) {
		return this.profileService.uploadProfileImage(req.user.sub, file);
	}
}
