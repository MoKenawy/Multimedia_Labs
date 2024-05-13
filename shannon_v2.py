# input (source_stats , data)
# steps:
# 1.sort desc by freq
# 2.divide when accumulated freq = total/2
# 3. for each division go back to (2)
## output (encoded data)


def shannon_encode(source_stats, data):
    # sort desc
    list = []
    # list.sort(key= lambda x : , reverse=True)
    source_stats.sort()



def divide(source_stats, code = "" , code_table = []):
    if len(source_stats) <= 1:
        symbol = source_stats[0][0]
        code_table.append((symbol, code))
        return code_table
    acc = 0
    total = 0
    for symbol, freq in source_stats:
        total += freq
    i = 0
    for symbol, freq in source_stats:
        acc += freq
        i += 1
        if acc >= total/2:
            return divide(source_stats[i:], code + "0", code_table[:]) + divide(source_stats[:i], code + "1", code_table[:])

if __name__ == "__main__":
    data = "AAABBFFGD"
    source_stats = [
        ('E', 1000),
        ('D',800),
        ('C', 400),
        ('G', 400),
        ('B', 200),
        ('A', 100),
        ('F', 100)
    ]


    code_table =  divide(source_stats)
    print(code_table)

    encoded_data = []
    #encode
    for char in data:
        for symbol, code in code_table:
            if char == symbol:
                encoded_data.append(code)
    print(f"encoded data: {encoded_data}")