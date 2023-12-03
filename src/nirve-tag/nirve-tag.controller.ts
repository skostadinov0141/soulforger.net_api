import {
	Controller,
	Get,
	Post,
	Body,
	Patch,
	Param,
	Delete,
	Req,
	Query,
} from '@nestjs/common';
import { NirveTagService } from './nirve-tag.service';
import { CreateNirveTagDto } from './dto/create-nirve-tag.dto';
import { UpdateNirveTagDto } from './dto/update-nirve-tag.dto';
import {
	ApiBearerAuth,
	ApiOperation,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { NirveTag } from './schemas/nirve-tag-schema';
import { Roles } from '../auth/auth.decorator';
import { SearchNirveTagDto } from './dto/search-nirve-tag.dto';

@ApiTags('Nirve Tags')
@Controller('v1/nirve-tag')
@ApiBearerAuth()
@Roles(['creator:nirve', 'admin', 'dev'])
export class NirveTagController {
	constructor(private readonly nirveTagService: NirveTagService) {}

	@Post()
	@ApiOperation({ summary: 'Create a new Nirve Tag.' })
	async create(
		@Body() createNirveTagDto: CreateNirveTagDto,
		@Req() req: any,
	): Promise<NirveTag> {
		return this.nirveTagService.create(createNirveTagDto, req.user.sub);
	}

	@Post('search')
	@ApiOperation({ summary: 'Search Nirve Tags.' })
	@ApiQuery({ name: 'limit', required: false, type: Number })
	@ApiQuery({ name: 'skip', required: false, type: Number })
	search(
		@Body() searchObject: SearchNirveTagDto,
		@Query('limit') limit: number,
		@Query('skip') skip: number,
	) {
		return this.nirveTagService.search(searchObject, limit, skip);
	}

	@Get(':id')
	@ApiOperation({ summary: 'Get a Nirve Tag by ID.' })
	findOne(@Param('id') id: string) {
		return this.nirveTagService.findOne(id);
	}

	@Patch(':id')
	@ApiOperation({ summary: 'Update a Nirve Tag by ID.' })
	update(
		@Param('id') id: string,
		@Body() updateNirveTagDto: UpdateNirveTagDto,
	): Promise<NirveTag> {
		return this.nirveTagService.update(id, updateNirveTagDto);
	}

	@Delete(':id')
	@ApiOperation({ summary: 'Delete a Nirve Tag by ID.' })
	remove(@Param('id') id: string) {
		return this.nirveTagService.remove(id);
	}
}
