from unittest.case import TestCase
from woorism.tools import jsend

class TestJsend(TestCase):
	def test_success(self):
		ret = jsend.success(data={'key': 'value'})
		self.assertTrue(jsend.is_success(ret))
		self.assertEqual(ret['data']['key'], 'value')

	def test_success_data_must_be_dict(self):
		try:
			jsend.success(data=1)
		except ValueError:
			return
		self.fail()

	def test_fail(self):
		ret = jsend.fail(data={'key': 'value'})
		self.assertTrue(jsend.is_fail(ret))
		self.assertEqual(ret['data']['key'], 'value')

	def test_fail_data_must_be_dict(self):
		try:
			jsend.fail(data=1)
		except ValueError:
			return
		self.fail()

	def test_error(self):
		ret = jsend.error(message='error message')
		self.assertTrue(jsend.is_error(ret))
		self.assertEqual(ret['message'], 'error message')

	def test_error_message_must_be_str(self):
		try:
			jsend.error(message=1)
		except ValueError:
			return
		self.fail()

	def test_error_code_must_be_number(self):
		try:
			jsend.error(code='1')
		except ValueError:
			return
		self.fail()

	def test_error_data_must_be_dict(self):
		try:
			jsend.error(data=1)
		except ValueError:
			return
		self.fail()