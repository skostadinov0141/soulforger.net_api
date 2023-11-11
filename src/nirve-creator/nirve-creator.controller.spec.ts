import { Test, TestingModule } from '@nestjs/testing';
import { NirveCreatorController } from './nirve-creator.controller';

describe('NirveCreatorController', () => {
	let controller: NirveCreatorController;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			controllers: [NirveCreatorController],
		}).compile();

		controller = module.get<NirveCreatorController>(NirveCreatorController);
	});

	it('should be defined', () => {
		expect(controller).toBeDefined();
	});
});
