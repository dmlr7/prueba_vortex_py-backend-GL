
# rest framework
from rest_framework import status
from rest_framework.test import APITestCase
# models
from api.serializers import ConductorSerializer


class ConductoresAPITestCase(APITestCase):
    """Conductores APITest case"""

    def setUp(self) -> None:
        """Test case Setup"""
        # self.token = ""
        # self.client.credentials(self.token)
        pass

    def test_API_list_conductor(self):
        url = "conductor//conductor"
        request = self.client.get(url)
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_API_insert_conductor(self):
        url = "conductor//conductor//"
        conductor = ConductorSerializer(data={
          "id": 3,
          "identificacion": 2,
          "nombre": "Bogota",
          "apellido": "somewhere",
          "telefono": 1111111111,
          "direccion": "asdfsad asdasds3"
        })
        request = self.client.post(url, conductor)
        self.assertEquals(request.status_code, status.HTTP_202_ACCEPTED)
