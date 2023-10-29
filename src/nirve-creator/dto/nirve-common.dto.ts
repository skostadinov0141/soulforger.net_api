import { ApiProperty } from '@nestjs/swagger';

export class NirveCommonDto {
  @ApiProperty()
  _id: string;
  @ApiProperty()
  name: string;
  @ApiProperty()
  description: string;
  @ApiProperty()
  location: string;
  @ApiProperty()
  createdBy: string;
  @ApiProperty()
  createdAt: Date;
  @ApiProperty()
  updatedAt: Date;
  @ApiProperty()
  creationPhase: number;
}