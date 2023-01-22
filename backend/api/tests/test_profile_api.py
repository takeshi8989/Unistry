from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import School, Profile, Event
from django.contrib.auth.models import User

class ProfileTest(APITestCase):
    def setUp(self):
        url = reverse('schools')
        data = {
            'name': 'New School',
            'location': 'Vancouver',
            'url': ''
        }
        self.client.post(url, data, format='json')
        User.objects.create(
            username='User 1',
            email='user1@gmail.com',
            password='user1password'
        )
        url = reverse('events')
        data = {
            'title': 'New Event',
            'school': School.objects.first().id,
            'description': 'new description',
            'organizers': [Profile.objects.first().id]
        }
        self.client.post(url, data, format='json')

    def test_get_profiles(self):
        url = reverse('profiles')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile(self):
        first = Profile.objects.first()
        url = reverse('profile', args=[first.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_profile(self):
        url = reverse('profiles')
        data = {
            'username': 'New User',
            'email': 'new@gmail.com',
            'password': 'newpassword',
        }
        self.assertEqual(Profile.objects.count(), 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 2)

    def test_update_profile(self):  
        first = Profile.objects.first()
        url = reverse('profile', args=[first.id])
        data = {
            'school': School.objects.first().id,
            'email': 'update@gmail.com',
            'link': 'github...',
            'info': 'my new profile is...'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.first().user.email, 'update@gmail.com')
        self.assertEqual(Profile.objects.first().school, School.objects.first())
        self.assertEqual(Profile.objects.first().chat_set.count(), 1)

    def test_delete_profile(self):
        first = Profile.objects.first()
        url = reverse('profile', args=[first.id])

        self.assertEqual(Profile.objects.count(), 1)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.count(), 0)

    def test_get_school_members(self):
        school = School.objects.first()
        url = reverse('school_members', args=[school.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_event_members(self):
        event = Event.objects.first()
        url = reverse('event_members', args=[event.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # team, chat members

    def test_add_event_member(self):
        event = Event.objects.first()
        user = Profile.objects.first()
        url = reverse('change_event_member', args=[user.id, event.id])
        self.assertEqual(Event.objects.first().members.count(), 0)
        self.assertEqual(Event.objects.first().chat.members.count(), 0)
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.first().members.count(), 1)
        self.assertEqual(Event.objects.first().chat.members.count(), 1)

    def test_remove_event_member(self):
        event = Event.objects.first()
        user = Profile.objects.first()
        url = reverse('change_event_member', args=[user.id, event.id])
        self.client.put(url, format='json')
        self.assertEqual(Event.objects.first().members.count(), 1)
        self.assertEqual(Event.objects.first().chat.members.count(), 1)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.first().members.count(), 0)
        self.assertEqual(Event.objects.first().chat.members.count(), 0)