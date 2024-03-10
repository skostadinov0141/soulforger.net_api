import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { User } from './schemas/user.schema';
import { Model } from 'mongoose';
import { CreateUserDto } from './dto/create-user.dto';
import * as bcrypt from 'bcrypt';
import { SearchUserDto } from './dto/search-users.dto';
import { Profile } from 'src/user/schemas/profile.schema';
import { UpdateProfileDto } from './dto/update-profile.dto';
import { CloudinaryService } from '../cloudinary/cloudinary.service';

@Injectable()
export class UserService {
	constructor(
		@InjectModel(User.name) private userModel: Model<User>,
		@InjectModel(Profile.name) private profileModel: Model<Profile>,
		private cloudinary: CloudinaryService,
	) {}

	async create(createUserDto: CreateUserDto): Promise<User> {
		const createdUser = new this.userModel(createUserDto);
		const createdProfile = new this.profileModel();

		const salt = await bcrypt.genSalt(10);
		createdUser.passwordHash = await bcrypt.hash(
			createUserDto.password,
			salt,
		);
		createdUser.roles = ['user'];

		createdUser.profile = createdProfile;
		createdProfile.owner = createdUser;

		await createdProfile.save();
		await createdUser.save();

		return this.userModel.findById(createdUser._id, {
			passwordHash: false,
		});
	}

	async findOneById(id: string): Promise<User> {
		return this.userModel.findById(id, { passwordHash: false });
	}

	async deleteOneById(id: string): Promise<User> {
		return this.userModel.findOneAndDelete({ _id: id });
	}

	async findOneByEmail(email: string): Promise<User> {
		return this.userModel.findOne({ email: email });
	}

	async updatePassword(id: string, newPw: string): Promise<User> {
		const user = await this.userModel.findById(id);
		const salt = await bcrypt.genSalt(10);
		user.passwordHash = await bcrypt.hash(newPw, salt);
		user.save();
		return this.userModel.findById(id, { passwordHash: false });
	}

	async updateEMail(id: string, newEmail: string): Promise<User> {
		return this.userModel.findByIdAndUpdate(
			id,
			{ email: newEmail },
			{ new: true, passwordHash: false },
		);
	}

	async findAll(
		searchQuery: SearchUserDto,
		limit?: number,
		skip?: number,
	): Promise<User[]> {
		return this.userModel
			.find(
				searchQuery,
				{ passwordHash: false },
				{ limit: limit, skip: skip },
			)
			.exec();
	}

	async getUserProfile(id: string): Promise<Profile> {
		const user = await this.userModel.findById(id);
		if (!user) throw new Error('User not found');
		return this.profileModel.findById(user.profile._id);
	}

	async updateProfile(id: string, dto: UpdateProfileDto): Promise<Profile> {
		const profile = await this.profileModel.findOne({ owner: id }).exec();
		if (!profile) throw new Error('User not found');
		return this.profileModel.findByIdAndUpdate(profile._id, dto, {
			new: true,
		});
	}

	async updateAvatar(
		id: string,
		avatar: Express.Multer.File,
	): Promise<Profile> {
		const profile = await this.profileModel
			.findOneAndUpdate({ owner: id })
			.exec();
		if (!profile) throw new Error('User not found');
		const request = await this.cloudinary.uploadUserAvatarImage(avatar, id);
		profile.avatarUrl = request.secure_url;
		return profile.save();
	}
}
