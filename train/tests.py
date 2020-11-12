from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestTrainTests(APITestCase):
    def test_simple_2_train(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('train')
        data = {'leftTrain': 100, 'rightTrain': 200}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'{"sumTrain": 300}')
