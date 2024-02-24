import { Test, TestingModule } from '@nestjs/testing';
import { NirveCreatorService } from './nirve-creator.service';

describe('NirveCreatorService', () => {
	let service: NirveCreatorService;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			providers: [NirveCreatorService],
		}).compile();

		service = module.get<NirveCreatorService>(NirveCreatorService);
	});

	it('should be defined', () => {
		expect(service).toBeDefined();
	});
});
