import unittest

from counter import Counter
from multiplication_twos_complement import multiplication_twos_complement


class test_all_and_compare(unittest.TestCase):

    def test_count(self):  # main method to compare all methods

        x_array = [[1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]]
        m_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
        resultsTwosComplement = []
        resultsCsd = []
        resultsTwosComplementHorner = []
        resultsCsdHorner = []

        i = 0
        while i < len(x_array):
            # initialize all counters
            counterTwosComplement = Counter()
            counterCsd = Counter()
            counterTwosComplementHorner = Counter()
            counterCsdHorner = Counter()

            resultTwosComplement = multiplication_twos_complement(x_array[i], m_array[i], counterTwosComplement)

            print("counterTwosComplement.countValue:")
            print(counterTwosComplement.countValue)

            i += 1


if __name__ == '__main__':
    unittest.main()
