
# Pixel packing
# input : sequence of symbols
# Steps:
#   1. get unique symbols
#   2. sort them
#   3. Get number of bits needed (fixed length)
#   3. give each symbol a unique code corresponding to index
#   4. encode the input based on the constructed table.
#   5. write output as indices.
#   6. write output as binary codes.
# output : sequence of coded symbols


import numpy as np
import math
x = input()
x = x.split(' ')
x = [int(symbol) for symbol in x]

# getting unique symbols & sorting
symbols = list(set(x))
symbols.sort()
print(f"Unique symbols : {symbols}")

# 4. encode file
indices = []
codewords = []
for i in range (len(x)):
    for j in range(len(symbols)):
        if x[i] == symbols[j]:
            index = j
            indices.append(index)
            number_of_bits = math.ceil(math.log2(len(symbols)))
            codeword = format(index, f"0{number_of_bits}b")
            codewords.append(codeword)

print(f"symbols indices : {indices}")
print(f"symbols codewords : {codewords}")


