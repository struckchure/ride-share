-- CreateEnum
CREATE TYPE "public"."TransactionStatus" AS ENUM ('Pending', 'Failed', 'Successful');

-- CreateTable
CREATE TABLE "public"."Transaction" (
    "id" SERIAL NOT NULL,
    "amount" MONEY NOT NULL,
    "user" INTEGER NOT NULL,
    "rider" INTEGER NOT NULL,
    "status" "public"."TransactionStatus" NOT NULL DEFAULT 'Pending',

    CONSTRAINT "Transaction_pkey" PRIMARY KEY ("id")
);
