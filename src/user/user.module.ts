import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { getModelToken, MongooseModule } from '@nestjs/mongoose';
import { User, UserSchemaFactory } from './schemas/user.schema';
import { Profile, ProfileSchema } from 'src/user/schemas/profile.schema';
import { CloudinaryModule } from '../cloudinary/cloudinary.module';

@Module({
	imports: [
		CloudinaryModule,
		MongooseModule.forFeatureAsync([
			{
				name: User.name,
				useFactory: UserSchemaFactory,
				inject: [getModelToken(Profile.name)],
			},
			{
				name: 'Profile',
				useFactory: () => ProfileSchema,
			},
		]),
	],
	exports: [UserService],
	controllers: [UserController],
	providers: [UserService],
})
export class UserModule {}
