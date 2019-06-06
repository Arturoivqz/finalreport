import unittest
import operations

class Testoperations(unittest.TestCase):
	
	def test_add(self):
		result = operations.add(10,5)
		self.assertEqual(result,15)

	def test_substract(self):
		result = operations.substract(10,5)
		self.assertEqual(result,5)
	def test_multiply(self):
		result = operations.multiply(10,5)
		self.assertEqual(result,50)
	def test_divide(self):
		result = operations.divide(10,5)
		self.assertEqual(result,2.5)

if __name__ == '__main__':
	unittest.main()
