from unittest import TestCase
from main import create_paddle

class TestingPingPong(TestCase):

    def test_paddle(self):
        paddle = create_paddle()
        
        self.assertEqual(paddle.shape(), "square")
        self.assertEqual(paddle.color(), ('white', 'white'))
        self.assertTrue(False)
