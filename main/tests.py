from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class SignUpPageTest(TestCase):
    username = 'newuser'
    email='newuser@email.com'
    
    def test_signup_test_status_code(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'sign_up.html')
        
    def test_sigup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
