from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        workout = Workout.objects.create(name='Pushups', description='20 Pushups', difficulty='Easy')
        activity = Activity.objects.create(user=user, type='Pushups', duration=10, date='2026-04-10')
        Leaderboard.objects.create(user=user, points=100)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
