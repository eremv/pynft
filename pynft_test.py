import unittest
import pynft

class nftTest(unittest.TestCase):
	def test_get_stat_from_empty_file(self):
		pass

	def test_get_stat_from_file(self):
		stat = pynft.get_stat_from_file('correct.csv')
		self.assertEquals(40.5, stat["cpu_max"])
		self.assertEquals(27.6875, stat["cpu_avg"])
		self.assertEquals(151.6, stat["mem_max"])
		self.assertEquals(116.6875, stat["mem_avg"])

	def test_get_stat_from_incorrect_file(self):
		pass

	def test_get_stat_from_missing_file(self):
		pass

if __name__ == "__main__":
	unittest.main()