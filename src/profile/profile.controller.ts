import {
	Body,
	Controller,
	Get,
	Param,
	Patch,
	Post,
	Query,
	UseGuards,
} from '@nestjs/common';
import { ProfileService } from './profile.service';
import {
	ApiBearerAuth,
	ApiBody,
	ApiOperation,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { UserIsOwnerGuard } from 'src/own-user/user-is-owner.guard';
import { SearchProfileDto } from './dto/search-profile.dto';

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
}
