import { Test, TestingModule } from '@nestjs/testing';
import { NirveGroupService } from './nirve-group.service';

describe('NirveGroupService', () => {
	let service: NirveGroupService;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			providers: [NirveGroupService],
		}).compile();

		service = module.get<NirveGroupService>(NirveGroupService);
	});

	it('should be defined', () => {
		expect(service).toBeDefined();
	});
});
