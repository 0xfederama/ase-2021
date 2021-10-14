import unittest
import json
from flask import request, jsonify
from calc import app


class TestHome(unittest.TestCase):
    def test_my_view(self):
        tested_app = app.test_client()
        home_reply = tested_app.get("/")

        body = json.loads(str(home_reply.data, "utf8"))
        self.assertEqual(body, {})
