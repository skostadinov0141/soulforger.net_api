import { NestFactory } from '@nestjs/core';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { ConfigService } from '@nestjs/config';
import * as basicAuth from 'express-basic-auth';

async function bootstrap() {
	const app = await NestFactory.create(AppModule);

	const configService = app.get(ConfigService);

	app.use(
		'/docs*',
		basicAuth({
			challenge: true,
			users: { doc: configService.get<string>('SWAGGER_PW') },
		}),
	);

	app.enableCors({
		origin: (): string[] => {
			if (configService.get<string>('NODE_ENV') === 'development') {
				return ['http://localhost:3001'];
			}
			return ['https://soulforger.net', 'https://api.soulforger.net'];
		},
	});

	const config = new DocumentBuilder()
		.addBearerAuth()
		.setTitle('Soulforger API')
		.setDescription('The backend API for the Soulforger web app')
		.setVersion('0.0.1')
		.build();
	const document = SwaggerModule.createDocument(app, config);
	SwaggerModule.setup('docs', app, document);

	await app.listen(
		configService.get<string>('NODE_ENV') === 'development' ? 3000 : 8080,
		configService.get<string>('NODE_ENV') === 'development'
			? 'localhost'
			: '0.0.0.0',
		() => {
			console.log(
				`Server is running on ${
					configService.get<string>('NODE_ENV') === 'development'
						? 'localhost:3000'
						: '0.0.0.0:8080'
				}`,
			);
		},
	);
}

bootstrap();
