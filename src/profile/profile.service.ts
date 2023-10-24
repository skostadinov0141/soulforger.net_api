import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Profile } from './schemas/profile.schema';
import { Model } from 'mongoose';
import { UpdateProfileDto } from './dto/update-profile.dto';

@Injectable()
export class ProfileService {
  constructor(
    @InjectModel(Profile.name) private profileModel: Model<Profile>,
  ) {}

  async create(): Promise<Profile> {
    const createdProfile = new this.profileModel();
    createdProfile.createdAt = new Date();
    createdProfile.updatedAt = new Date();
    return createdProfile.save();
  }

  async delete(id: string): Promise<Profile> {
    return this.profileModel.findByIdAndRemove(id);
  }

  async updateById(id: string, profile: UpdateProfileDto): Promise<Profile> {
    profile.updatedAt = new Date();
    console.log(profile);
    console.log(id);
    return this.profileModel.findByIdAndUpdate(id, profile, { new: true });
  }

  async findOneById(id: string): Promise<Profile> {
    return this.profileModel.findById(id);
  }
}
