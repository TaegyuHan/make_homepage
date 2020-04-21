import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from languages import models as languages_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        language = languages_models.Language_note.objects.all()
        seeder.add_entity(
            languages_models.Language_notes_text,
            number,
            {"title_text": lambda X: random.choice(language)},
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviwes created!"))
