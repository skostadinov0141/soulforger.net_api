import {
	Body,
	Controller,
	Delete,
	Get,
	Param,
	Patch,
	Post,
	Query,
	Req,
} from '@nestjs/common';
import { NirveCreatorService } from './nirve-creator.service';
import {
	ApiBearerAuth,
	ApiBody,
	ApiOperation,
	ApiParam,
	ApiQuery,
	ApiTags,
} from '@nestjs/swagger';
import { NirveCreateDto } from './dto/nirve-create.dto';
import { Roles } from 'src/auth/auth.decorator';
import { NirveCommonDto } from './dto/nirve-common.dto';
import { NirveSearchDto } from './dto/nirve-search.dto';
import { NirvePhase1Common } from './schemas/nirve-phase-1-common.schema';

@ApiTags('Nirve Creator')
@Controller('v1/nirve-creator')
export class NirveCreatorController {
	constructor(private nirveCreatorService: NirveCreatorService) {}

	@ApiOperation({ summary: 'Create a new Nirve of the provided type. ' })
	@Post()
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
	@ApiBody({ type: NirveCreateDto })
	async create(
		@Body() dto: NirveCreateDto,
		@Req() req: any,
	): Promise<NirvePhase1Common> {
		return this.nirveCreatorService.create(dto, req.user.sub);
	}

	@ApiOperation({
		summary:
			'Search nirve objects based on a query object and/or limit and skip, with given type.',
	})
	@Post('search')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
	@ApiQuery({ name: 'limit', type: Number, required: false })
	@ApiQuery({ name: 'skip', type: Number, required: false })
	@ApiBody({ type: NirveSearchDto })
	async search(
		@Body() searchObject: NirveSearchDto,
		@Query('limit') limit: number,
		@Query('skip') skip: number,
		@Req() req: any,
	): Promise<NirvePhase1Common[]> {
		return this.nirveCreatorService.findAll(
			searchObject,
			limit,
			skip,
		);
	}

	@ApiOperation({ summary: 'Get a single Nirve object based on its ID.' })
	@Get(':id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
	@ApiParam({ name: 'id', type: String })
	async getOneById(
		@Param('id') id: string,
	): Promise<NirvePhase1Common> {
		return this.nirveCreatorService.getOneById(id);
	}

	@ApiOperation({
		summary: 'Update a single Nirve object of the provided type by id. ',
	})
	@Patch(':id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
	@ApiParam({ name: 'id', type: String })
	async updateOneById(
		@Body() dto: NirveCommonDto,
		@Param('id') id: string,
	): Promise<NirvePhase1Common> {
		return this.nirveCreatorService.updateOneById(id, dto);
	}

	@ApiOperation({
		summary: 'Delete a single Nirve object of the provided type by id. ',
	})
	@Delete(':id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
	@ApiParam({ name: 'id', type: String })
	async deleteOneById(
		@Param('id') id: string,
	): Promise<NirvePhase1Common> {
		return this.nirveCreatorService.deleteOneById(id);
	}
}
