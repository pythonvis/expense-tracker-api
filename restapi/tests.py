from django.test import TestCase
from unittest import TestCase

# Create your tests here.
def sumofint(a, b):
    return a + b


class Testsum(TestCase):
    def test_sum(self):
        self.assertEqual(sumofint(1, 2), 3)
