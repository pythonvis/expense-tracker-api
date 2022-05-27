from django.test import TestCase
from restapi import models
from datetime import datetime

# Create your tests here.
class Pretest(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=499,
            shopname="Amazon",
            category="Airpod",
            description="Apple airpod purchased from Amazon",
            posted=datetime.now(),
        )
        fortest = models.Expense.objects.get(pk=expense.id)
        self.assertEqual(499, fortest.amount)
