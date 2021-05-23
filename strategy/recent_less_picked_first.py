from collections import Counter
from random import sample
from difflib import SequenceMatcher
import statistics


def recent_less_picked_first(data, pool, iterations=1000, portion=0.33, recent=20, console_log=False):
    '''
    @param data [(n1,n2,n3,n4,n5,n6), ...]
    @param pool [n1,n2,.......nx]
    '''
    if portion > 1 or portion < 0.13:
        raise Exception('make sure 0.13 <= portion < 1')

    if recent < 0 or recent > len(data):
        raise Exception('recent out of bound')

    numbers_counter = Counter(pool)
    least_common_size = int(len(pool) * portion)

    global_hit_rates = []
    for idx in range(recent, len(data)):
        # prepare counter from recent data items
        recent_d = []
        for x in data[idx-recent:idx-1]:
            recent_d += x
        new_counter = numbers_counter + Counter(recent_d)

        d = data[idx]
        least_commons = [x[0] for x in new_counter.most_common()[-1*least_common_size:]]

        #
        local_hit_rates = []
        for i in range(0, iterations):
            guess = sample(least_commons, 6)
            hit_rate = len(list(set(guess) & set(d)))/len(d)
            local_hit_rates.append(hit_rate)
        local_avg_rate = statistics.mean(local_hit_rates)

        global_hit_rates.append(local_avg_rate)

        if console_log:
            print('stage %s, avg rate: %s' % (idx, local_avg_rate))

    
    # print global rate
    global_avg_rate = statistics.mean(global_hit_rates)

    if console_log:
        print('================================')
        print('globally, avg rate: %s' % global_avg_rate)

    return global_avg_rate
