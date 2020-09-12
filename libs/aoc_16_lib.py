"""aoc_16_lib"""

# import time
# import resource
#
# time_start = time.perf_counter()
#
# time_elapsed = (time.perf_counter() - time_start)
# memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
# print("%5.1f secs %5.1f MByte" % (time_elapsed, memMb))

import itertools
from typing import Iterator, List


class FFT:
    """"""
    basic_pattern: List[int] = [0, 1, 0, -1]

    def __init__(self, signal: List[int]) -> None:
        """"""
        self.signal = signal
        self.phase_count: int = 0

    # def construct_pattern(self, index) -> Iterator:
    #     """"""
    #     return itertools.chain.from_iterable((itertools.repeat(number, index+1) for number in self.basic_pattern))

    # def construct_pattern(self, index):
    #     """"""
    #     pattern = [element for element in [0,1,0,-1] for _ in range(index)]
    #     pattern_shifted = pattern[1:] + pattern[0]
    #     amount =

    def phase(self) -> None:
        """"""
        basic_pattern_length: int = len(self.basic_pattern)
        plus_index: int = self.basic_pattern.index(1)
        minus_index: int = self.basic_pattern.index(-1)
        shift: int = -1
        new_signal: List[int] = []

        for index, _ in enumerate(self.signal):
            iterator_plus: Iterator = create_pattern_iter(self.signal, plus_index, index + 1, basic_pattern_length, shift)
            iterator_minus: Iterator = create_pattern_iter(self.signal, minus_index, index + 1, basic_pattern_length, shift)
            new_element: int = abs(sum(self.signal[i] for i in iterator_plus) - sum(self.signal[i] for i in iterator_minus)) % 10
            new_signal.append(new_element)
            # print(index)
            # pattern: List[int] = list(self.construct_pattern(index))
            # pattern_iter = iter(pattern)
            # next(pattern_iter)
            # new_element = 0
            # for ind, elem in enumerate(self.signal):
            #     try:
            #         new_element += elem * next(pattern_iter)
            #     except StopIteration:
            #         pattern_iter = iter(pattern)
            #         new_element += elem * next(pattern_iter)
            # new_signal.append(abs(new_element) % 10)
        self.signal = new_signal
        self.phase_count += 1


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read()]


def create_pattern_iter(lst: list, index_lst: int, repetitions: int, pattern_length: int, shift: int) -> Iterator:
    """"""
    step = pattern_length * repetitions
    return (i + j for i, j in itertools.product(range(repetitions*index_lst + shift, len(lst), step), range(repetitions)) if i + j < len(lst))


def list_int_to_int(lst: List[int]) -> int:
    """"""
    return int("".join(str(number) for number in lst)) if lst else 0
    # if lst:
    #     return int("".join(str(number) for number in lst))
    # else:
    #     return 0


def constructor(signal: List[int], phases_amount: int, offset: int = 0, signal_repetitions: int = 1):
    """"""
    message_offset: int = list_int_to_int(signal[:offset])
    real_signal: List[int] = signal * signal_repetitions
    fft: FFT = FFT(real_signal)
    while fft.phase_count < phases_amount:
    # for _ in range(phases_amount):
        fft.phase()
        # print(fft.phase_count)
    return list_int_to_int(fft.signal[message_offset:message_offset + 8])


def part_1(signal: List[int], phases_amount: int = 100) -> int:
    """"""
    return constructor(signal, phases_amount)
    # fft: FFT = FFT(signal)
    # for i in range(phases_amount):
    #     fft.phase()
    # return list_int_to_int(fft.signal[:8])


def part_2(signal: List[int], phases_amount: int = 100):
    """"""
    return constructor(signal, phases_amount, offset=7, signal_repetitions=10_000)
#     message_offset: int = list_int_to_int(signal[:offset])
#     real_signal: List[int] = signal * 10_000
#     fft: FFT = FFT(real_signal)
#     for i in range(phases_amount):
#         fft.phase()
#         print(i)
#     return list_int_to_int(fft.signal[message_offset:message_offset+8])
