from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Matheus Fernandes', cpf='12345678901',
        email='matpfernandes@gmail.com', phone='14-99605-5972')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'matpfernandes@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        contents = [
            'Matheus Fernandes',
            '12345678901',
            'matpfernandes@gmail.com',
            '14-99605-5972'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
                
