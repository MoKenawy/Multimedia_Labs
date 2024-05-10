import heapq
from collections import Counter
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def build_codes( node, prefix="", code_book={}):
    if node is not None:
        if node.char is not None:
            code_book[node.char] = prefix
        build_codes(node.left, prefix + "0", code_book)
        build_codes(node.right, prefix + "1", code_book)
    return code_book

def huffman_encode(data):
    if not data:
        return "", None
    frequencies = Counter(data)
    tree = build_huffman_tree(frequencies)
    code_book = build_codes(tree)
    encoded_output = ''.join(code_book[char] for char in data)
    return encoded_output, tree

def huffman_decode(encoded_data, tree):
    if not encoded_data or tree is None:
        return ""
    decoded_output = []
    node = tree
    for bit in encoded_data:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded_output.append(node.char)
            node = tree
    return ''.join(decoded_output)
# Example
data = "BCCADE"
encoded_data, tree = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, tree)
print("Original:", data)
print("Encoded:", encoded_data)
print("Decoded:", decoded_data)
