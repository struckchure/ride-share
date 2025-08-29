import { Injectable } from '@nestjs/common';
import { PaymentDto } from './app.dto';

@Injectable()
export class AppService {
  async list() {}

  async payment(dto: PaymentDto) {
    return 'Hello World!';
  }
}
