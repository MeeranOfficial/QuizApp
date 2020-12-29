from django.test import SimpleTestCase
from django.urls import reverse, resolve
from quiz.views import welcome, quiz, result, save_ans


class TestUrls(SimpleTestCase):
    
    def test_welcome_url_resolves(self):
        url = reverse('welcome')    
        self.assertEquals(resolve(url).func, welcome) #func.view_class (if class)


    def test_quiz_url_resolves(self):
        url = reverse('quiz')    
        self.assertEquals(resolve(url).func, quiz)


    def test_result_url_resolves(self):
        url = reverse('result')    
        self.assertEquals(resolve(url).func, result)

    
    def test_save_ans_url_resolves(self):
        url = reverse('saved_answer')    
        self.assertEquals(resolve(url).func, save_ans)