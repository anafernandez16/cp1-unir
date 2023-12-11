import http.client
import os
import unittest
import json
from urllib.request import urlopen


import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 5  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
        
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/8"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "16", "ERROR ADD"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/4/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "2.0", "ERROR ADD"
        )

    def test_api_divide_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.NOT_ACCEPTABLE, f"Error en la petición API a {url}"
            )

        except Exception as e:
            self.fail(f"Fallo al realizar la petición a {url}: {e}")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
