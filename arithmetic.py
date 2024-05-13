## input: data, source_stats
### steps:
    #    1. Calculate cumulative
    #    2.for each symbol in source_stats
    #       2.1: calculate range
    #    3.for every symbol in data:
    #       3.1:see which range does it belong to.
    #       3.2:update ranges
    #    4. get repersentative from range of last symbol in data
    #    5. return binary(represntative)

## output encoded data





def arithmetic_encoding(data, source_stats):
    total_freq = 0
    for i in range(len(source_stats)):
        freq = source_stats[i][1]
        total_freq += freq

    # additional: calc probalities
    for i in range(len(source_stats)):
        source_stats[i][1] /= total_freq

    # 1,2
    cumulative = 0
    ranges = []
    for i in range(len(source_stats)):
        symbol = source_stats[i][0]
        prob = source_stats[i][1]
        start_range = cumulative
        cumulative += prob
        end_range = cumulative
        ranges.append([start_range,end_range])
        source_stats[i].append(cumulative)
        source_stats[i].append(start_range)
        source_stats[i].append(end_range)

    # 3
    for symbol in data:
            for record in source_stats:
                 record_symbol = record[0]
                 if symbol == record_symbol:
                    start_range = record[3]
                    end_range = record[4]
                    source_stats = update_ranges(source_stats, start_range, end_range)
    # 4
    choosen_start = source_stats[-1][3]
    choosen_end = source_stats[-1][4]
    repr = (choosen_start + choosen_end) / 2
    return repr

def update_ranges(source_stats, min, max):
    delta = max - min
    previous_start = min
    for record in source_stats:
        cumulative = record[2]
        new_max = min + delta * cumulative
        record[3] = previous_start
        record[4] = new_max
        previous_start = new_max
    return source_stats


source_stats = [
    ['A',100],
    ['B', 100],
    ['C',100],
    ['D',800],
    ['E',200] ,
    ['F',100], 
    ['G',50],
    ['H',50]
]

data = "DFG"

result = arithmetic_encoding(data, source_stats)
print(result)