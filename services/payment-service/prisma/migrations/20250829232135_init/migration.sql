-- AlterTable
ALTER TABLE "public"."Transaction" ALTER COLUMN "user" DROP NOT NULL,
ALTER COLUMN "user" SET DATA TYPE TEXT;
