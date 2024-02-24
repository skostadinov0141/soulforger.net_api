import {
	Body,
	Controller,
	Get,
	Param,
	Patch,
	Post,
	Put,
	Query,
	Req,
	Search,
	UseGuards,
} from '@nestjs/common';
import { ProfileService } from './profile.service';
import {
	ApiBearerAuth,
	ApiBody,
	ApiOperation,
	ApiParam,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { Request } from 'express';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { UserIsOwnerGuard } from 'src/own-user/user-is-owner.guard';
import { Roles } from 'src/auth/auth.decorator';
import { SearchProfileDto } from './dto/search-profile.dto';
import { plainToClass } from 'class-transformer';

@ApiTags('Profile')
@Controller('v1/profile')
export class ProfileController {
	constructor(private profileService: ProfileService) {}

	@ApiBearerAuth()
	@UseGuards(AuthGuard)
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
		console.log(searchQuery);
		return this.profileService.findAll(searchQuery, limit, skip);
	}

	@ApiOperation({ summary: 'Get a Profile based on its ID' })
	@ApiBearerAuth()
	@UseGuards(AuthGuard)
	@Get(':id')
	async findOneById(@Param('id') profileId: string) {
		return this.profileService.findOneById(profileId);
	}

	@ApiOperation({ summary: 'Update a Profile based on its ID' })
	@ApiBearerAuth()
	@UseGuards(AuthGuard)
	@UseGuards(UserIsOwnerGuard)
	@Patch(':id')
	async update(
		@Param('id') profileId: string,
		@Body() profile: UpdateProfileDto,
	) {
		return this.profileService.updateById(profileId, profile);
	}
}
