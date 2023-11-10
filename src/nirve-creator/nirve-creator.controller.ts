import {
	Body,
	Controller,
	Delete,
	Get,
	Param,
	Patch,
	Post,
	Put,
	Query,
	Req,
	UseGuards,
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

@ApiTags('Nirve Creator')
@Controller('v1/nirve-creator')
export class NirveCreatorController {
	constructor(private nirveCreatorService: NirveCreatorService) {}

	@ApiOperation({ summary: 'Create a new Nirve of the provided type. ' })
	@Post(':type')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
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
		required: true,
	})
	async create(
		@Body() dto: NirveCreateDto,
		@Param('type') type: string,
		@Req() req: any,
	): Promise<NirveCommonDto> {
		return this.nirveCreatorService.create(dto, type, req.user.sub);
	}

	@ApiOperation({
		summary:
			'Search nirve objects based on a query object and/or limit and skip, with given type.',
	})
	@Post(':type/search')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
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
		required: true,
	})
	@ApiQuery({ name: 'limit', type: Number, required: false })
	@ApiQuery({ name: 'skip', type: Number, required: false })
	@ApiBody({ type: NirveSearchDto })
	async search(
		@Body() searchObject: NirveSearchDto,
		@Query('limit') limit: number,
		@Query('skip') skip: number,
		@Param('type') type: string,
		@Req() req: any,
	): Promise<NirveCommonDto> {
		return this.nirveCreatorService.findAll(
			type,
			searchObject,
			limit,
			skip,
		);
	}

	@ApiOperation({ summary: 'Get a single Nirve object based on its ID.' })
	@Get(':type/:id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
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
		required: true,
	})
	async getOneById(
		@Param('id') id: string,
		@Param('type') type: string,
	): Promise<NirveCommonDto> {
		return this.nirveCreatorService.getOneById(id, type);
	}

	@ApiOperation({
		summary: 'Update a single Nirve object of the provided type by id. ',
	})
	@Patch(':type/:id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
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
		required: true,
	})
	async updateOneById(
		@Body() dto: NirveCommonDto,
		@Param('id') id: string,
		@Param('type') type: string,
	): Promise<NirveCommonDto> {
		return this.nirveCreatorService.updateOneById(id, dto, type);
	}

	@ApiOperation({
		summary: 'Delete a single Nirve object of the provided type by id. ',
	})
	@Delete(':type/:id')
	@ApiBearerAuth()
	@Roles(['creator:nirve', 'admin', 'dev'])
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
		required: true,
	})
	async deleteOneById(
		@Param('id') id: string,
		@Param('type') type: string,
	): Promise<NirveCommonDto> {
		return this.nirveCreatorService.deleteOneById(id, type);
	}
}
