import unittest

from views import computeResults


class ComputeResultsTests(unittest.TestCase):

  def testComputeResultsOnBadValue(self):
    self.assertRaises(ZeroDivisionError, computeResults, 0, 0, '', '', 100)


if __name__ == "__main__":
  unittest.main()
