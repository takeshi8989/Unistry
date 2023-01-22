from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import School

class SchoolTest(APITestCase):
    def setUp(self):
        School.objects.create(
            name='School 1',
            location='Tokyo',
        )

    def test_get_schools(self):
        url = reverse('schools')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_school(self):
        first = School.objects.first()
        url = reverse('school', args=[first.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_school(self):
        url = reverse('schools')
        data = {
            'name': 'New School',
            'location': 'Vancouver',
            'url': ''
        }
        self.assertEqual(School.objects.count(), 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2)

    def test_update_school(self):
        first = School.objects.first()
        url = reverse('school', args=[first.id])
        data = {
            'name': 'Updated Name',
            'location': 'Vancouver',
            'url': 'https...'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(School.objects.first().name, 'Updated Name')

    def test_delete_school(self):
        first = School.objects.first()
        url = reverse('school', args=[first.id])

        self.assertEqual(School.objects.count(), 1)

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(School.objects.count(), 0)