import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './user/user.module';
import { AuthModule } from './auth/auth.module';
import { ProfileModule } from './profile/profile.module';
import { NirveCreatorModule } from './nirve-creator/nirve-creator.module';

@Module({
  imports: [
    ConfigModule.forRoot({ envFilePath: '.env' }),
    MongooseModule.forRoot(
      `mongodb+srv://${process.env.MONGO_TESTING_UNAME}:${process.env.MONGO_TESTING_PW}@soulforgerdb.hmyeqw0.mongodb.net/soulforger_testing?retryWrites=true&w=majority`,
    ),
    UserModule,
    AuthModule,
    ProfileModule,
    NirveCreatorModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
