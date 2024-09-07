from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = "Lists all models"

    def handle(self, *args, **kwargs):
        for model in apps.get_models():
            self.stdout.write(model._meta.db_table)
