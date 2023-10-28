import {
  Body,
  Controller,
  Delete,
  Param,
  Post,
  Put,
  UseGuards,
} from '@nestjs/common';
import { NirveCreatorService } from './nirve-creator.service';
import { ApiBearerAuth, ApiParam, ApiTags } from '@nestjs/swagger';
import { AuthGuard } from 'src/auth/auth.guard';
import { NirveCreateDto } from './dto/nirve-create.dto';
import { RoleGuard } from 'src/role-guard/role-guard.guard';

@ApiTags('Nirve Creator')
@Controller('v1/nirve-creator')
export class NirveCreatorController {
  constructor(private nirveCreatorService: NirveCreatorService) {}

  @Post(':type')
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @UseGuards(new RoleGuard(['nirve-creator']))
  @ApiParam({
    name: 'type',
    enum: [
      'bending-skill',
      'character-class',
      'disadvantage',
      'item',
      'race',
      'race',
      'religion',
      'skill',
      'spell',
    ],
  })
  async create(
    @Body() dto: NirveCreateDto,
    @Param('type') type: string,
  ): Promise<any> {
    return this.nirveCreatorService.create(dto, type);
  }

  @Put(':type/:id')
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @UseGuards(new RoleGuard(['nirve-creator']))
  @ApiParam({ name: 'id', type: String })
  @ApiParam({
    name: 'type',
    enum: [
      'bending-skill',
      'character-class',
      'disadvantage',
      'item',
      'race',
      'race',
      'religion',
      'skill',
      'spell',
    ],
  })
  async updateOneById(
    @Body() dto: NirveCreateDto,
    @Param('id') id: string,
    @Param('type') type: string,
  ): Promise<any> {
    return this.nirveCreatorService.updateOneById(id, dto, type);
  }

  @Delete(':type/:id')
  @ApiBearerAuth()
  @UseGuards(AuthGuard)
  @UseGuards(new RoleGuard(['nirve-creator']))
  @ApiParam({ name: 'id', type: String })
  @ApiParam({
    name: 'type',
    enum: [
      'bending-skill',
      'character-class',
      'disadvantage',
      'item',
      'race',
      'race',
      'religion',
      'skill',
      'spell',
    ],
  })
  async deleteOneById(
    @Param('id') id: string,
    @Param('type') type: string,
  ): Promise<any> {
    return this.nirveCreatorService.deleteOneById(id, type);
  }
}
