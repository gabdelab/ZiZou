import unittest

from views import computeResults


class ComputeResultsTests(unittest.TestCase):

  def testComputeResultsOnBadValue(self):
    # computeResults produces a generator, so it is only the conversion to list that makes it raise
    self.assertRaises(ZeroDivisionError, list, computeResults(0, 0, '', '', 100))


if __name__ == "__main__":
  unittest.main()
