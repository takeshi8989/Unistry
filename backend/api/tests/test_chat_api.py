from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import School, Event, Chat, Profile

class ChatTest(APITestCase):

    def setUp(self):
        url = reverse('profiles')
        profile_data = {
            'username': 'New User',
            'email': 'new@gmail.com',
            'password': 'newpassword',
        }
        self.client.post(url, profile_data, format='json')
        Chat.objects.create(is_public=True)

    def test_get_chats(self):
        url = reverse('chats')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_chat(self):
        first = Chat.objects.first()
        url = reverse('chat', args=[first.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_chat(self):
        first = Chat.objects.first()
        url = reverse('chat', args=[first.id])
        data = {
            'is_public': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Chat.objects.first().is_public, False)

    def test_get_user_chats(self):
        user = Profile.objects.first()
        url = reverse('user_chats', args=[user.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_messages(self):
        chat = Chat.objects.first()
        url = reverse('chat_messages', args=[chat.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_chat(self):
        url = reverse('schools')
        data = {
            'name': 'New School',
            'location': 'Vancouver',
            'url': ''
        }
        self.client.post(url, data, format='json')
        self.assertEqual(Chat.objects.count(), 2)
        url = reverse('events')
        data = {
            'title': 'New Event',
            'school': School.objects.first().id,
            'description': 'new description',
            'organizers': [Profile.objects.first().id]
        }
        self.client.post(url, data, format='json')
        self.assertEqual(Chat.objects.count(), 3)
        url = reverse('teams')
        data = {
            'name': 'New Team',
            'event': Event.objects.first().id,
        }
        self.client.post(url, data, format='json')
        self.assertEqual(Chat.objects.count(), 4)