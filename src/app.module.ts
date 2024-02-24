import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './user/user.module';
import { AuthModule } from './auth/auth.module';
import { ProfileModule } from './profile/profile.module';
import { NirveCreatorModule } from './nirve-creator/nirve-creator.module';
import { NirveTagModule } from './nirve-tag/nirve-tag.module';
import { NirveGroupModule } from './nirve-group/nirve-group.module';
import * as process from 'process';

@Module({
	imports: [
		ConfigModule.forRoot({ envFilePath: '.env' }),
		MongooseModule.forRoot(
			`${
				process.env.NODE_ENV === 'development'
					? 'mongodb'
					: 'mongodb+srv'
			}://${process.env.DB_ADMIN_UNAME}:${process.env.DB_ADMIN_PW}@${
				process.env.DB_IP
			}/soulforger?retryWrites=true&w=majority&authSource=admin`,
		),
		UserModule,
		AuthModule,
		ProfileModule,
		NirveCreatorModule,
		NirveTagModule,
		NirveGroupModule,
	],
	controllers: [AppController],
	providers: [AppService],
})
export class AppModule {}
