# О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.
import numpy as np


class Handler:
    def __init__(self, variation: np.float64, start: np.float64) -> None:
        self.variation: np.float64 = variation
        self.start: np.float64 = start
        self.run()

    def mean(self, start: np.float64, end: np.float64):
        return (start+end)/2

    def find_end(self) -> None:
        # variation = (a-b)**2/12
        # (0.2*12)**0.5 = |a-b| = +- 1,549193338482966754071706159913
        # 1) a-b = 1,549193338482966754071706159913 b = a - 1,549193338482966754071706159913 тут получится, что данное 0.5 будет правой границей, а не левой(как в условии)
        # 2) a-b = -1,549193338482966754071706159913 b = a + 1,549193338482966754071706159913 тут все норм
        a_minus_b = (self.variation*12)**0.5
        print(f"a={self.start} b={self.start + a_minus_b} mean={self.mean(start=self.start,end=(self.start + a_minus_b))}")

    def run(self) -> None:
        self.find_end()


if __name__ == '__main__':
    Handler(variation=0.2, start=0.5)
