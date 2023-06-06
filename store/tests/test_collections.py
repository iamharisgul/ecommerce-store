from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.


class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):

        #Act
        client = APIClient()
        response = client.post('/store/collections/', {'title' : 'a'})


        assert response.status_code == status.HTTP_401_UNAUTHORIZED