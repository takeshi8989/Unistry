from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import School, Event, Profile, Team

class EventTest(APITestCase):
    def setUp(self):
        # school
        url = reverse('schools')
        school_data = {
            'name': 'New School',
            'location': 'Vancouver',
            'url': ''
        }
        self.client.post(url, school_data, format='json')
        # profile
        url = reverse('profiles')
        profile_data = {
            'username': 'New User',
            'email': 'new@gmail.com',
            'password': 'newpassword',
        }
        self.client.post(url, profile_data, format='json')
        # event
        url = reverse('events')
        event_data = {
            'title': 'New Event',
            'school': School.objects.first().id,
            'description': 'new description',
            'organizers': [Profile.objects.first().id]
        }
        self.client.post(url, event_data, format='json')
        

        Team.objects.create(
            name = 'Team 1',
            event = Event.objects.first(),
        )

    def test_get_teams(self):
        url = reverse('teams')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team(self):
        first = Team.objects.first()
        url = reverse('team', args=[first.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_team(self):
        url = reverse('teams')
        data = {
            'name': 'New Team',
            'event': Event.objects.first().id,
        }
        self.assertEqual(Team.objects.count(), 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

    def test_update_team(self):
        first = Team.objects.first()
        url = reverse('team', args=[first.id])
        data = {
            'name': 'Updated team name',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.first().name, 'Updated team name')

    def test_delete_team(self):
        first = Team.objects.first()
        url = reverse('team', args=[first.id])

        self.assertEqual(Team.objects.count(), 1)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.count(), 0)


    def test_get_event_teams(self):
        event = Event.objects.first()
        url = reverse('event_teams', args=[event.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
