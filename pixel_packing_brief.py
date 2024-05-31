
# Pixel packing Encoding
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

import math

def pixel_packing_encode(x):
    # getting unique symbols & sorting
    symbols = list(set(x))
    symbols.sort()
    # 4. encode file
    indices = []
    codewords = []
    number_of_bits = math.ceil(math.log2(len(symbols)))
    for i in range (len(x)):
        for j in range(len(symbols)):
            if x[i] == symbols[j]:
                index = j
                indices.append(index)
                codeword = format(index, f"0{number_of_bits}b")
                codewords.append(codeword)
    return symbols,indices,codewords

def pixel_packing_decode(symbols, code_sequence):

    seq_indices = [int(code, 2) for code in code_sequence]
    # getting unique symbols & sorting
    symbols = list(set(x))
    symbols.sort()
    
    # decode file
    original_seq = []
    for index in seq_indices:
        original_seq.append(symbols[index])
    return original_seq

if __name__ == "__main__":
    x = input()
    x = x.split(' ')
    x = [int(symbol) for symbol in x]

    symbols, indices , code_sequence = pixel_packing_encode(x)
    print(f"Unique symbols : {symbols}")
    print(f"symbols indices : {indices}")
    print(f"Endoded symbols: {code_sequence}")


    original_seq = pixel_packing_decode(symbols, code_sequence)
    print(f"Decoded symbols : {original_seq}")


