import { Body, Controller, Get, Post } from '@nestjs/common';
import { PaymentDto } from './app.dto';
import { AppService } from './app.service';
import { User } from './user.decorator';

@Controller('transactions')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async list() {
    return await this.appService.list();
  }

  @Post('payment')
  async payment(@Body() dto: PaymentDto, @User() user: string) {
    dto.user = user;

    return await this.appService.payment(dto);
  }
}
