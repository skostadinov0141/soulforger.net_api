import { Test, TestingModule } from '@nestjs/testing';
import { NirveTagService } from './nirve-tag.service';

describe('NirveTagService', () => {
	let service: NirveTagService;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			providers: [NirveTagService],
		}).compile();

		service = module.get<NirveTagService>(NirveTagService);
	});

	it('should be defined', () => {
		expect(service).toBeDefined();
	});
});
