import unittest

from counter import Counter
from multiplication_twos_complement import multiplication_twos_complement
from multiplication_twos_complement_horner import multiplication_twos_complement_horner


class test_all_and_compare(unittest.TestCase):

    def test_count(self):  # main method to compare all methods

        x_array = [[1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]]
        m_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]]

        resultsTwosComplement = []
        resultsCsd = []
        resultsTwosComplementHorner = []
        resultsCsdHorner = []

        countsTwosComplement = []
        countsCsd = []
        countsTwosComplementHorner = []
        countsCsdHorner = []

        i = 0
        while i < len(x_array):
            # initialize all counters
            counterTwosComplement = Counter()
            counterCsd = Counter()
            counterTwosComplementHorner = Counter()
            counterCsdHorner = Counter()

            resultTwosComplement = multiplication_twos_complement(x_array[i], m_array[i], counterTwosComplement)
            resultsTwosComplement.append(resultTwosComplement)
            countsTwosComplement.append(counterTwosComplement.countValue)

            resultTwosComplementHorner = multiplication_twos_complement_horner(x_array[i], m_array[i],
                                                                               counterTwosComplementHorner)
            resultsTwosComplementHorner.append(resultTwosComplementHorner)
            countsTwosComplementHorner.append(counterTwosComplementHorner.countValue)

            print("counterTwosComplement count, result")
            print(counterTwosComplement.countValue)
            print(resultTwosComplement)
            print("counterTwosComplementHorner count, result")
            print(counterTwosComplementHorner.countValue)
            print(resultTwosComplementHorner)

            i += 1


if __name__ == '__main__':
    unittest.main()
