import {
	Body,
	Controller,
	Delete,
	Get,
	Patch,
	Post,
	Query,
	Req,
} from '@nestjs/common';
import { NirveGroupService } from './nirve-group.service';
import {
	ApiBearerAuth,
	ApiOperation,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { Roles } from '../auth/auth.decorator';
import { CreateNirveGroupDto } from './dto/create-nirve-group.dto';
import { UpdateNirveGroupDto } from './dto/update-nirve-group.dto';
import { SearchNirveGroupDto } from './dto/search-nirve-group.dto';

@ApiTags('Nirve Groups')
@Controller('v1/nirve-group')
@Roles(['creator:nirve', 'admin', 'dev'])
@ApiBearerAuth()
export class NirveGroupController {
	constructor(private readonly nirveGroupService: NirveGroupService) {}

	@Post()
	@ApiOperation({ summary: 'Create a new Nirve Group.' })
	async create(@Body() dto: CreateNirveGroupDto, @Req() req: any) {
		return this.nirveGroupService.create(dto, req.user.sub);
	}

	@Post('search')
	@ApiOperation({ summary: 'Search Nirve Groups.' })
	@ApiQuery({ name: 'limit', required: false, type: Number })
	@ApiQuery({ name: 'skip', required: false, type: Number })
	async search(
		@Body() dto: SearchNirveGroupDto,
		@Req() req: any,
		@Query('limit') limit: number,
		@Query('skip') skip: number,
	) {
		return this.nirveGroupService.search(dto, limit, skip);
	}

	@Get(':id')
	@ApiOperation({ summary: 'Get a Nirve Group by ID.' })
	async getById(id: string) {
		return this.nirveGroupService.getById(id);
	}

	@Patch(':id')
	@ApiOperation({ summary: 'Update a Nirve Group by ID.' })
	async updateById(id: string, @Body() dto: UpdateNirveGroupDto) {
		return this.nirveGroupService.updateById(id, dto);
	}

	@Delete(':id')
	@ApiOperation({ summary: 'Delete a Nirve Group by ID.' })
	async deleteById(id: string) {
		return this.nirveGroupService.deleteById(id);
	}
}
