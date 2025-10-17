#!/usr/bin/env python3
from z3 import *

s = Solver()
PIN_LENGTH = 38
pin = [Int(f'pin_{i}') for i in range(PIN_LENGTH)]

for i in range(PIN_LENGTH):
    s.add(pin[i] >= 32)
    s.add(pin[i] <= 126)

s.add(pin[0] == ord('E'))
s.add(pin[1] == ord('L'))
s.add(pin[2] == ord('I'))
s.add(pin[3] == ord('T'))
s.add(pin[4] == ord('E'))
s.add(pin[5] == ord('S'))
s.add(pin[6] == ord('E'))
s.add(pin[7] == ord('C'))
s.add(pin[8] == ord('{'))
s.add(pin[37] == ord('}'))

s.add(pin[0] * 3 - pin[1] * 2 == 55)
s.add(pin[1] + pin[2] - pin[3] == 65)
s.add(pin[2] * pin[3] - pin[4] * 5 == 5787)
s.add(pin[5] * 2 + pin[6] * 3 - pin[7] == 306)
s.add(pin[7] - pin[8] + pin[9] * 2 == 80)
s.add(pin[8] * pin[9] - pin[10] == 8316)
s.add(pin[10] + pin[11] * 2 - pin[12] == 189)
s.add(pin[11] * 5 - pin[12] * 3 + pin[13] == 383)
s.add(pin[13] + pin[14] - pin[15] * 2 == 54)
s.add(pin[14] * pin[15] - pin[16] * 3 == 4218)
s.add(pin[16] + pin[17] * 4 - pin[18] == 419)
s.add(pin[17] * 2 - pin[18] + pin[19] * 3 == 262)
s.add(pin[19] - pin[20] * 2 + pin[21] == 0)
s.add(pin[20] * 3 + pin[21] - pin[22] * 2 == 6)
s.add(pin[22] + pin[23] * 5 - pin[24] == 492)
s.add(pin[23] * pin[24] - pin[25] * 4 == 3932)
s.add(pin[25] * 2 - pin[26] + pin[27] * 3 == 341)
s.add(pin[26] + pin[27] - pin[28] * 2 == 103)
s.add(pin[28] * 4 - pin[29] * 3 + pin[30] == 108)
s.add(pin[29] * pin[30] - pin[31] * 5 == 2149)
s.add(pin[30] + pin[31] * 2 - pin[32] == 94)
s.add(pin[31] - pin[32] + pin[33] * 4 == 287)
s.add(pin[32] * 3 - pin[33] + pin[34] * 2 == 303)
s.add(pin[33] * pin[34] - pin[35] * 4 == 3552)
s.add(pin[34] + pin[35] * 2 - pin[36] == 88)
s.add(pin[35] - pin[36] + pin[37] * 3 == 367)
s.add(pin[36] * 2 + pin[37] == 237)
s.add(pin[0] + pin[10] + pin[20] + pin[30] == 215)
s.add(pin[5] + pin[15] + pin[25] + pin[35] == 264)
s.add(pin[1] + pin[11] + pin[21] + pin[31] == 290)
s.add(Sum([pin[i] for i in range(0, PIN_LENGTH, 2)]) == 1391)
s.add(Sum([pin[i] for i in range(1, PIN_LENGTH, 2)]) == 1410)

if s.check() == sat:
    m = s.model()
    print(''.join([chr(m[pin[i]].as_long()) for i in range(PIN_LENGTH)]))
