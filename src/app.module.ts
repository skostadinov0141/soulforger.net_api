import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './user/user.module';
import { AuthModule } from './auth/auth.module';
import { NirveCreatorModule } from './nirve-creator/nirve-creator.module';
import { NirveTagModule } from './nirve-tag/nirve-tag.module';
import { NirveGroupModule } from './nirve-group/nirve-group.module';
import * as process from 'process';
import { CloudinaryService } from './cloudinary/cloudinary.service';
import { CloudinaryModule } from './cloudinary/cloudinary.module';

@Module({
	imports: [
		ConfigModule.forRoot({
			envFilePath: ['.env', 'secret.env'],
			isGlobal: true,
		}),
		MongooseModule.forRoot(
			`${
				process.env.NODE_ENV === 'development'
					? 'mongodb'
					: 'mongodb+srv'
			}://${process.env.DB_ADMIN_UNAME}:${process.env.DB_ADMIN_PW}@${
				process.env.DB_IP
			}/${
				process.env.NODE_ENV === 'production'
					? process.env.LINE === 'stable'
						? 'soulforger-stable'
						: 'soulforger-beta'
					: 'soulforger'
			}?retryWrites=true&w=majority&authSource=admin`,
		),
		UserModule,
		AuthModule,
		NirveCreatorModule,
		NirveTagModule,
		NirveGroupModule,
		CloudinaryModule,
	],
	controllers: [AppController],
	providers: [AppService, CloudinaryService],
})
export class AppModule {}
