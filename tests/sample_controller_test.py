import sys
import mock
import unittest
from pathlib import Path
from unittest import TestCase
from fastapi.testclient import TestClient
from alchemy_mock.mocking import AlchemyMagicMock

test_dir = Path(__file__).parent.parent / 'server'
sys.path.insert(0, str(test_dir))

mock_db_session = AlchemyMagicMock()

def get_mock_session():
    return mock_db_session

class SampleControllerTest(TestCase):
    @mock.patch('utils.db_connection.get_db_session', new=get_mock_session)
    def setUp(self):
        from main import app
        self.client = TestClient(app)

    def test_get_sample_object_exists(self):
        expected_id = '1234'

        mock_db_session.query.return_value.get.return_value = { 'id': expected_id }
        response = self.client.get('/sample-controller?id={}'.format(expected_id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], expected_id)

    def test_get_sample_object_not_exists(self):
        expected_id = '12345'

        mock_db_session.query.return_value.get.return_value = None
        response = self.client.get('/sample-controller?id={}'.format(expected_id))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Content not found on DB')

    
    def test_get_sample_object_invalid_input(self):
        response = self.client.get('/sample-controller')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Validation error: query.id field required')

    def test_add_sample_object(self):
        expected_object = { 'id': '123' }
        response = self.client.post('/sample-controller', json=expected_object)

        mock_db_session.add.assert_called_once()
        mock_db_session.commit.assert_called_once()
        mock_db_session.refresh.assert_called_once()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), None)

    def test_add_sample_object_invalid_input(self):
        expected_object = {}
        response = self.client.post('/sample-controller', json=expected_object)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Validation error: body.id field required')
