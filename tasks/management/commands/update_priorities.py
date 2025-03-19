from django.core.management.base import BaseCommand
from tasks.services import update_task_priorities

class Command(BaseCommand):
    help = "Uuendab AI prioriteedid kõigi ülesannete jaoks."

    def handle(self, *args, **kwargs):
        update_task_priorities()
        self.stdout.write(self.style.SUCCESS("✅ Kõigi ülesannete prioriteedid on edukalt uuendatud!"))
