import { ApiHideProperty } from "@nestjs/swagger";

export class NirveCreateDto {
  name: string;
  description: string;
  @ApiHideProperty()
  updatedAt: Date;
}
