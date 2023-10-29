import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { User } from './schemas/user.schema';
import { Model } from 'mongoose';
import { CreateUserDto } from './dto/create-user.dto';
import * as bcrypt from 'bcrypt';
import { UpdateUserDto } from 'src/auth/dto/update-user.dto';
import { ProfileService } from 'src/profile/profile.service';
import { SearchUserDto } from './dto/search-users.dto';
import { Profile } from 'src/profile/schemas/profile.schema';

@Injectable()
export class UserService {
  constructor(
    @InjectModel(User.name) private userModel: Model<User>,
    @InjectModel(Profile.name) private profileModel: Model<Profile>,
  ) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const createdUser = new this.userModel(createUserDto);
    const createdProfile = new this.profileModel();

    createdProfile.createdAt = new Date();
    createdProfile.updatedAt = new Date();

    const salt = await bcrypt.genSalt(10);
    createdUser.passwordHash = await bcrypt.hash(createUserDto.password, salt);
    createdUser.createdAt = new Date();
    createdUser.updatedAt = new Date();
    createdUser.roles = ['user'];

    createdUser.profile = createdProfile;
    createdProfile.owner = createdUser;

    await createdProfile.save();
    await createdUser.save();

    return this.userModel.findById(createdUser._id, { passwordHash: false });
  }

  async findOneById(id: string): Promise<User> {
    return this.userModel.findById(id, { passwordHash: false });
  }

  async updateOneById(id: string, user: UpdateUserDto): Promise<User> {
    if (user.passwordHash) {
      const salt = await bcrypt.genSalt(10);
      user.passwordHash = await bcrypt.hash(user.passwordHash, salt);
    }
    return this.userModel.findByIdAndUpdate(id, user, { new: true });
  }

  async deleteOneById(id: string): Promise<User> {
    const user = await this.userModel.findById(id);
    const profile = await this.profileModel.findById(user.profile._id);
    this.profileModel.findByIdAndDelete(user.profile._id);
    return this.userModel.findByIdAndRemove(id);
  }

  async findOneByEmail(email: string): Promise<User> {
    return this.userModel.findOne({ email: email });
  }

  async findAll(
    searchQuery: SearchUserDto,
    limit?: number,
    skip?: number,
  ): Promise<User[]> {
    return this.userModel
      .find(searchQuery, { passwordHash: false }, { limit: limit, skip: skip })
      .exec();
  }
}
