import {
  Body,
  Controller,
  Get,
  Param,
  Patch,
  Put,
  Req,
  UseGuards,
} from '@nestjs/common';
import { ProfileService } from './profile.service';
import {
  ApiBearerAuth,
  ApiOperation,
  ApiParam,
  ApiTags,
} from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { Request } from 'express';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { UserIsOwnerGuard } from 'src/own-user/user-is-owner.guard';
import { Roles } from 'src/auth/auth.decorator';

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
  @ApiParam({ name: 'limit', type: Number, required: false })
  @ApiParam({ name: 'skip', type: Number, required: false })
  @ApiParam({ name: 'searchQuery', type: String, required: false })
  @Get()
  async findOne(@Param('limit') limit: number, @Param('skip') skip: number, @Param('searchQuery') searchQuery: string) {
    if (!searchQuery) {
      searchQuery = '{}';
    }
    return this.profileService.findAll(JSON.parse(searchQuery), limit, skip);
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
