import random
import string

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate SECRET_KEY for project'

    def add_arguments(self, parser):
        parser.add_argument(
            'secret_length',
            nargs='?',
            default=50,
            type=int,
            help="Set length of SECRET_KEY"
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            "".join(
                [random.SystemRandom().choice(
                    string.digits + string.ascii_letters + string.punctuation
                    ) for i in range(options['secret_length'])]
                )
            )
        )
