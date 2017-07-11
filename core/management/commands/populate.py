import random

from django.core.management.base import BaseCommand
from faker import Factory

from core.models import UserAccount, Activity


fake = Factory.create()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-n', type=int, dest='number',
            help='Number of users to populate',
        )

    def handle(self, *args, **options):
        number = options.get('number', 1)
        for _ in range(number):
            user_data = {
                'name': fake.first_name(),
                'surname': fake.last_name(),
                'sex': random.randint(0, 1),
                'age': random.randint(0, 99),
            }
            user = UserAccount.objects.create(**user_data)
            for _ in range(random.randint(0, 10)):
                Activity.objects.create(user=user, name=fake.word())

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated {} user(s).'.format(number)
        ))
