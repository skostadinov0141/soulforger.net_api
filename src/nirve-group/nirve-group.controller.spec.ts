import { Test, TestingModule } from '@nestjs/testing';
import { NirveGroupController } from './nirve-group.controller';

describe('NirveGroupController', () => {
	let controller: NirveGroupController;

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			controllers: [NirveGroupController],
		}).compile();

		controller = module.get<NirveGroupController>(NirveGroupController);
	});

	it('should be defined', () => {
		expect(controller).toBeDefined();
	});
});
