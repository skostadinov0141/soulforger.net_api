import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
  Req,
  UseGuards,
} from '@nestjs/common';
import { ApiBearerAuth, ApiParam, ApiTags } from '@nestjs/swagger';
import { CreateUserDto } from './dto/create-user.dto';
import { UserService } from './user.service';
import { User } from './schemas/user.schema';
import { AuthGuard } from 'src/auth/auth.guard';
import { Request } from 'express';
import { UpdateUserDto } from 'src/auth/dto/update-user.dto';

@ApiTags('user')
@Controller('user')
export class UserController {
  constructor(private userService: UserService) {}

  /**
   * Create a new user
   */
  @Post()
  async create(@Body() createUserDto: CreateUserDto): Promise<User> {
    return this.userService.create(createUserDto);
  }

  /**
   * Get all users
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Get()
  async findAll(): Promise<User[]> {
    return this.userService.findAll();
  }

  /**
   * Update own user
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Put()
  async updateOneById(
    @Req() request: Request,
    @Body() user: UpdateUserDto,
  ): Promise<User> {
    return this.userService.updateOneById((request as any).user.sub, user);
  }

  /**
   * Update user by id
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Put(':id')
  @ApiParam({ name: 'id', type: String })
  async updateOneByIdParam(
    @Param('id') id: string,
    @Body() user: UpdateUserDto,
  ): Promise<User> {
    return this.userService.updateOneById(id, user);
  }

  /**
   * Delete own user
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Delete()
  async delete(@Req() request: Request): Promise<User> {
    return this.userService.deleteOneById((request as any).user.sub);
  }

  /**
   * Delete user by id
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Delete(':id')
  @ApiParam({ name: 'id', type: String })
  async deleteById(@Param('id') id: string): Promise<User> {
    return this.userService.deleteOneById(id);
  }

  /**
   * Get user by id
   */
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @Get(':id')
  @ApiParam({ name: 'id', type: String })
  async findOneById(@Param('id') id: string): Promise<User> {
    return this.userService.findOneById(id);
  }
}
