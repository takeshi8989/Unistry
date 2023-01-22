from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import School, Event, Profile

class EventTest(APITestCase):
    def setUp(self):
        url = reverse('schools')
        school_data = {
            'name': 'New School',
            'location': 'Vancouver',
            'url': ''
        }
        self.client.post(url, school_data, format='json')
        url = reverse('profiles')
        profile_data = {
            'username': 'New User',
            'email': 'new@gmail.com',
            'password': 'newpassword',
        }
        self.client.post(url, profile_data, format='json')

        Event.objects.create(
            title = 'Event 1',
            school = School.objects.first(),
            description = 'Good event'
        )

    def test_get_events(self):
        url = reverse('events')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_event(self):
        first = Event.objects.first()
        url = reverse('event', args=[first.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_event(self):
        url = reverse('events')
        data = {
            'title': 'New Event',
            'school': School.objects.first().id,
            'description': 'new description',
            'organizers': [Profile.objects.first().id]
        }
        self.assertEqual(Event.objects.count(), 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.get(title='New Event').school, School.objects.first())
        self.assertEqual(Event.objects.get(title='New Event').organizers.first(), Profile.objects.first())

    def test_update_event(self):
        first = Event.objects.first()
        url = reverse('event', args=[first.id])
        data = {
            'title': 'Updated title',
            'description': 'new description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.first().title, 'Updated title')

    def test_delete_event(self):
        first = Event.objects.first()
        url = reverse('event', args=[first.id])

        self.assertEqual(Event.objects.count(), 1)

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.count(), 0)


    def test_get_school_events(self):
        school = School.objects.first()
        url = reverse('school_events', args=[school.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_school_events(self):
        user = Profile.objects.first()
        url = reverse('user_events', args=[user.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)