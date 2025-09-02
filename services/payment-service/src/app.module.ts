import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma.service';

@Module({
  imports: [
    ConfigModule.forRoot(),
    ClientsModule.registerAsync([
      {
        imports: [ConfigModule],
        name: 'RMQ_SERVICE',
        useFactory: async (configService: ConfigService) => ({
          transport: Transport.RMQ,
          options: {
            urls: [configService.get('RMQ_URL') as string],
            queue: 'cats_queue',
          },
        }),
        inject: [ConfigService],
      },
    ]),
  ],
  controllers: [AppController],
  providers: [AppService, PrismaService],
})
export class AppModule {}
