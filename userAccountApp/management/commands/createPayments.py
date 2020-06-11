from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from userAccountApp.models import *


class Command(BaseCommand):
    help = 'Adding payment(s) to random user(s).  You can pass an argument n - number of payments to be made'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        fake = Faker()
        userIds = User.objects.values_list('id', flat=True)
        if len(userIds) == 0:
            return "There is no users!"

        for _ in range(int(options["n"])):
            randomUserId = fake.random_int(min=1, max=len(userIds))
            randomUser = User.objects.get(pk=randomUserId)
            randomAmount = fake.pyfloat(
                min_value=0, max_value=1000, right_digits=2)
            randomUser.addPayment(randomAmount)
