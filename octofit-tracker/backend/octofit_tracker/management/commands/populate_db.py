from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Lösche alte Daten...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Lege Teams an...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Lege Benutzer an...')
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        self.stdout.write('Lege Workouts an...')
        workouts = [
            Workout.objects.create(name='Pushups', description='20 Pushups', difficulty='Easy'),
            Workout.objects.create(name='Running', description='5km Lauf', difficulty='Medium'),
        ]

        self.stdout.write('Lege Aktivitäten an...')
        Activity.objects.create(user=users[0], type='Pushups', duration=10, date=timezone.now())
        Activity.objects.create(user=users[1], type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=users[2], type='Pushups', duration=15, date=timezone.now())
        Activity.objects.create(user=users[3], type='Running', duration=25, date=timezone.now())

        self.stdout.write('Lege Leaderboard an...')
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=80)
        Leaderboard.objects.create(user=users[2], points=120)
        Leaderboard.objects.create(user=users[3], points=90)

        self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich angelegt!'))
