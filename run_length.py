
def compress_rle(text,RUN_LENGTH):
    compressed_text = []
    count = 0
    for i in range(1, len(text)):
        if text[i] == text[i - 1] and count < RUN_LENGTH:
            count += 1
        else:
            compressed_text.append((text[i - 1], count ))  # Length starts from 0
            count = 0
    # Append the last symbol with its count
    compressed_text.append((text[-1], count))
    return compressed_text

def decompress_rle(compressed_text):
    decompressed_text = ''
    for symbol, length in compressed_text:
        decompressed_text += symbol * (length + 1)  # Increment length to match RLE format
    return decompressed_text

if __name__ == "__main__":

    RUN_BITS = 2
    RUN_LENGTH = 2**RUN_BITS

    text = "AAABBBCCDAA"

    
    compressed_text = compress_rle(text,RUN_LENGTH)
    print("Compressed text:", compressed_text)

    decompressed_text = decompress_rle(compressed_text)
    print("Decompressed text:", decompressed_text)