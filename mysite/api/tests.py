from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.

class ReceiptsTests(APITestCase):
    def test_receipts_process_1(self):
        """
        Create Receipt Test
        """
        url = reverse('receipts_process')
        data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                    "shortDescription": "Mountain Dew 12PK",
                    "price": "6.49"
                }, {
                    "shortDescription": "Emils Cheese Pizza",
                    "price": "12.25"
                }, {
                    "shortDescription": "Knorr Creamy Chicken",
                    "price": "1.26"
                }, {
                    "shortDescription": "Doritos Nacho Cheese",
                    "price": "3.35"
                }, {
                    "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    "price": "12.00"
                }
            ],
            "total": "35.35"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        id = response.data['id']

        url = reverse('receipts_points', args=[id])

        response = self.client.get(url)
        self.assertEqual(response.data, {"points": 28})

    def test_receipts_process_2(self):
        """
        Create Receipt Test 2
        """
        url = reverse('receipts_process')
        data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                  "shortDescription": "Gatorade",
                  "price": "2.25"
                },{
                  "shortDescription": "Gatorade",
                  "price": "2.25"
                },{
                  "shortDescription": "Gatorade",
                  "price": "2.25"
                },{
                  "shortDescription": "Gatorade",
                  "price": "2.25"
                }
            ],
            "total": "9.00"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        id = response.data['id']

        url = reverse('receipts_points', args=[id])

        response = self.client.get(url)
        self.assertEqual(response.data, {"points": 109})
