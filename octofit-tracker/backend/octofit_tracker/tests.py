from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", description="A test team")
        self.assertEqual(str(team), "Test Team")

    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="Test Team")
        self.assertEqual(str(user), "Test User")

    def test_create_activity(self):
        activity = Activity.objects.create(user="Test User", activity="Running", duration=30)
        self.assertEqual(str(activity), "Test User - Running")

    def test_create_workout(self):
        workout = Workout.objects.create(name="Test Workout", suggested_for="Test Team")
        self.assertEqual(str(workout), "Test Workout")

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user="Test User", points=100)
        self.assertEqual(str(leaderboard), "Test User: 100")
