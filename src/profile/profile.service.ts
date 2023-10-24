import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Profile } from './schemas/profile.schema';
import { Model } from 'mongoose';
import { User } from 'src/user/schemas/user.schema';

@Injectable()
export class ProfileService {
    constructor(@InjectModel(Profile.name) private profileModel: Model<Profile>) {}

    async create(owner: User): Promise<Profile> {
        const createdProfile = new this.profileModel();
        createdProfile.createdAt = new Date();
        createdProfile.updatedAt = new Date();
        return createdProfile.save();
    }

    async delete(id: string): Promise<Profile> {
        return this.profileModel.findByIdAndRemove(id);
    }
}
