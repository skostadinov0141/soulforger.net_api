import { Test, TestingModule } from '@nestjs/testing';
import { NirveTagController } from './nirve-tag.controller';
import { NirveTagService } from './nirve-tag.service';

describe('NirveTagController', () => {
	let controller: NirveTagController;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			controllers: [NirveTagController],
			providers: [NirveTagService],
		}).compile();

		controller = module.get<NirveTagController>(NirveTagController);
	});

	it('should be defined', () => {
		expect(controller).toBeDefined();
	});
});
