from collections import Counter
from random import sample, randint
from difflib import SequenceMatcher
import statistics


def continues_pick(data, pool, iterations=1000, console_log=False):
    '''
    @param data [(n1,n2,n3,n4,n5,n6), ...]
    @param pool [n1,n2,.......nx]
    '''

    extended_pool = pool + pool[0:5]
    global_hit_rates = []
    for idx in range(0, len(data)):
        d = data[idx]
        #
        local_hit_rates = []
        for i in range(0, iterations):
            start = randint(0, 49)
            guess = extended_pool[start:start+6]
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
