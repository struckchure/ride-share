import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';
import { Prisma } from 'generated/prisma';
import { firstValueFrom } from 'rxjs';
import { PaymentDto } from './app.dto';
import { PrismaService } from './prisma.service';

@Injectable()
export class AppService {
  constructor(
    private prismaService: PrismaService,
    @Inject('RMQ_SERVICE') private client: ClientProxy,
  ) {}

  async list() {
    return await this.prismaService.transaction.findMany();
  }

  async payment({ amount, ...dto }: PaymentDto) {
    const transaction = await this.prismaService.transaction.create({
      data: { ...dto, trip: +dto.trip, amount: Prisma.Decimal(amount) },
    });

    setTimeout(async () => {
      const newTransaction = await this.prismaService.transaction.update({
        where: { id: transaction.id },
        data: { status: 'Successful' },
      });
      await firstValueFrom(
        this.client.emit('transaction', JSON.stringify(newTransaction)),
      );
    }, 30_000);

    return transaction;
  }
}
