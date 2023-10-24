import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { User } from './schemas/user.schema';
import { Model } from 'mongoose';
import { CreateUserDto } from './dto/create-user.dto';
import * as bcrypt from 'bcrypt';
import { UpdateUserDto } from 'src/auth/dto/update-user.dto';

@Injectable()
export class UserService {
  constructor(@InjectModel(User.name) private userModel: Model<User>) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const createdUser = new this.userModel(createUserDto);
    const salt = await bcrypt.genSalt(10);
    createdUser.passwordHash = await bcrypt.hash(createUserDto.password, salt);
    createdUser.createdAt = new Date();
    createdUser.updatedAt = new Date();
    return createdUser.save();
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
    return this.userModel.findByIdAndRemove(id);
  }

  async findOneByEmail(email: string): Promise<User> {
    return this.userModel.findOne({ email: email });
  }

  async findAll(): Promise<User[]> {
    return this.userModel.find({}, { passwordHash: false }).exec();
  }
}
