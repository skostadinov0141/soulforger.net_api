import { NestFactory } from '@nestjs/core';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';
import { ConfigService } from '@nestjs/config';
import * as basicAuth from 'express-basic-auth';
import { ValidationPipe } from '@nestjs/common';

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
	// if in development, allow all cors origins, if not disable cors
	if (configService.get<string>('NODE_ENV') === 'development') {
		app.enableCors({ origin: '*' });
	} else {
		app.enableCors({
			origin: ['https://beta.soulforger.net', 'https://soulforger.net'],
		});
	}
	// enable validationPipe
	app.useGlobalPipes(new ValidationPipe());
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
	);
}

bootstrap();
