from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {"name": "Team Marvel", "description": "Marvel superheroes"},
            {"name": "Team DC", "description": "DC superheroes"}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Team Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Team Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "Team DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "Team DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"user": "Spider-Man", "activity": "Running", "duration": 30},
            {"user": "Iron Man", "activity": "Cycling", "duration": 45},
            {"user": "Wonder Woman", "activity": "Swimming", "duration": 60},
            {"user": "Batman", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {"name": "Morning Cardio", "suggested_for": "Team Marvel"},
            {"name": "Strength Training", "suggested_for": "Team DC"}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"user": "Spider-Man", "points": 100},
            {"user": "Iron Man", "points": 90},
            {"user": "Wonder Woman", "points": 110},
            {"user": "Batman", "points": 95}
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
