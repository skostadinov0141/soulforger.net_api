import {
  Body,
  Controller,
  Get,
  Param,
  Put,
  Req,
  UseGuards,
} from '@nestjs/common';
import { ProfileService } from './profile.service';
import { ApiBearerAuth, ApiTags } from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { Request } from 'express';
import { UpdateProfileDto } from './dto/update-profile.dto';

@ApiTags('Profile')
@Controller('profile')
export class ProfileController {
  constructor(private profileService: ProfileService) {}

  /**
   * Update own profile
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Put()
  async update(@Req() request: Request, @Body() profile: UpdateProfileDto) {
    return this.profileService.updateById(
      (request as any).user.profile,
      profile,
    );
  }

  /**
   * Get profile by id
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Get(':id')
  async findOneById(@Param('id') id: string) {
    return this.profileService.findOneById(id);
  }

  /**
   * Get own profile
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Get()
  async findOne(@Req() request: Request) {
    return this.profileService.findOneById((request as any).user.profile);
  }
}
