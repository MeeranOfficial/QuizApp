from django.test import TestCase, Client
from django.urls import reverse
from quiz.models import Quiz
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.welcome_url = reverse('welcome')
        self.quiz_url = reverse('quiz')
        self.result_url = reverse('result')
    
    def test_welcome_GET(self):
        response = self.client.get(self.welcome_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')


    def test_quiz_GET(self):
        response = self.client.get(self.quiz_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz.html')


    def test_result_GET(self):
        response = self.client.get(self.result_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')    

