from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.main_bot import start, unknown



class Command(BaseCommand):
    help = "Запускаем бота"
    def handle(self, *args, **options):
        try:
            application = ApplicationBuilder().token(settings.TOKEN_BOT).build()

            start_handler = CommandHandler('start', start)
            application.add_handler(start_handler)

            unknown_handler = MessageHandler(filters.COMMAND, unknown)
            application.add_handler(unknown_handler)

            self.stdout.write(self.style.SUCCESS('Бот успешно запущен'))
            application.run_polling()
        except Exception as e:
            raise CommandError(f"Ошибка запуска бота: {e}")
