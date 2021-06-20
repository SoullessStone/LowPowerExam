import unittest

from binary_to_csd import binary_to_csd
from counter import Counter
from dynamic_power_dissipation import dynamic_power_dissipation
from multiplication_csd_2 import multiplication_csd_2
from multiplication_csd_horner import multiplication_csd_horner
from multiplication_twos_complement import multiplication_twos_complement
from multiplication_twos_complement_horner import multiplication_twos_complement_horner
from static_power_dissipation import static_power_dissipation


class test_all_and_compare(unittest.TestCase):

    def test_count(self):  # main method to compare all methods
        fClock = pow(10, 6)
        vdd = 3.3
        iccTwosComplement = 0.00976
        iccTwosComplementHorner = 0.00469
        iccCsd = 0.06888
        iccCsdHorner = 0.005632
        cTotTwosComplement = 7.32 * pow(10, -11)
        cTotTwosComplementHorner = 2.89 * pow(10, -11)
        cTotCsd = 5.166 * pow(10, -10)
        cTotCsdHorner = 3.21 * pow(10, -11)

        x_array = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
        m_array = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

        resultsTwosComplement = []
        resultsCsd = []
        resultsTwosComplementHorner = []
        resultsCsdHorner = []

        countsTwosComplement = []
        countsCsd = []
        countsTwosComplementHorner = []
        countsCsdHorner = []

        staticPowerDissipationsTwosComplement = []
        staticPowerDissipationsCsd = []
        staticPowerDissipationsTwosComplementHorner = []
        staticPowerDissipationsCsdHorner = []

        dynamicPowerDissipationsTwosComplement = []
        dynamicPowerDissipationsCsd = []
        dynamicPowerDissipationsTwosComplementHorner = []
        dynamicPowerDissipationsCsdHorner = []

        i = 0
        while i < len(x_array):
            currX = x_array[i].copy()
            currM = m_array[i].copy()
            # initialize all counters
            counterTwosComplement = Counter()
            counterCsd = Counter()
            counterTwosComplementHorner = Counter()
            counterCsdHorner = Counter()

            # 2 complement
            resultTwosComplement = multiplication_twos_complement(currX, currM, counterTwosComplement)
            resultsTwosComplement.append(resultTwosComplement)
            countsTwosComplement.append(counterTwosComplement.countValue)
            staticPowerDissipationsTwosComplement.append(static_power_dissipation(iccTwosComplement, vdd))
            naTwosComplement = counterTwosComplement.countValue / 1114
            print(naTwosComplement)
            dynamicPowerDissipationsTwosComplement.append(
                dynamic_power_dissipation(naTwosComplement, fClock, cTotTwosComplement, vdd))

            # 2 complement horner
            resultTwosComplementHorner = multiplication_twos_complement_horner(currX, currM,
                                                                               counterTwosComplementHorner)
            resultsTwosComplementHorner.append(resultTwosComplementHorner)
            countsTwosComplementHorner.append(counterTwosComplementHorner.countValue)
            staticPowerDissipationsTwosComplementHorner.append(static_power_dissipation(iccTwosComplementHorner, vdd))
            naTwosComplementHorner = counterTwosComplementHorner.countValue / (95 * (sum(currM) - 1))
            print(naTwosComplementHorner)
            dynamicPowerDissipationsTwosComplementHorner.append(
                dynamic_power_dissipation(naTwosComplementHorner, fClock, cTotTwosComplementHorner, vdd))

            # csd
            x = binary_to_csd(currX.copy(), counterCsd)
            m = binary_to_csd(currM.copy(), counterCsd)
            resultCsd = multiplication_csd_2(x, m, counterCsd)
            resultsCsd.append(resultCsd)
            countsCsd.append(counterCsd.countValue)
            staticPowerDissipationsCsd.append(static_power_dissipation(iccCsd, vdd))
            naCsd = counterCsd.countValue / 2195
            print(naCsd)
            dynamicPowerDissipationsCsd.append(dynamic_power_dissipation(naCsd, fClock, cTotCsd, vdd))

            # csd horner
            resultCsdHorner = multiplication_csd_horner(currX, currM, counterCsdHorner)
            resultsCsdHorner.append(resultCsdHorner)
            countsCsdHorner.append(counterCsdHorner.countValue)
            staticPowerDissipationsCsdHorner.append(static_power_dissipation(iccCsdHorner, vdd))
            naCsdHorner = counterCsdHorner.countValue / (127 * (sum(currM) - 1))
            print(naCsdHorner)
            dynamicPowerDissipationsCsdHorner.append(dynamic_power_dissipation(naCsdHorner, fClock, cTotCsdHorner, vdd))

            print("TwosComplement count, result")
            print(counterTwosComplement.countValue)
            print(resultTwosComplement)
            print("TwosComplementHorner count, result")
            print(counterTwosComplementHorner.countValue)
            print(resultTwosComplementHorner)
            print("Csd count, result")
            print(counterCsd.countValue)
            print(resultCsd)
            print("CsdHorner count, result")
            print(counterCsdHorner.countValue)
            print(resultCsdHorner)

            i += 1

        print(staticPowerDissipationsTwosComplement)
        print(staticPowerDissipationsTwosComplementHorner)
        print(staticPowerDissipationsCsd)
        print(staticPowerDissipationsCsdHorner)
        print(dynamicPowerDissipationsTwosComplement)
        print(dynamicPowerDissipationsTwosComplementHorner)
        print(dynamicPowerDissipationsCsd)
        print(dynamicPowerDissipationsCsdHorner)

    if __name__ == '__main__':
        unittest.main()
