from collections import Counter
from random import sample


def recent_less_picked_first(data, pool, iterations=4, portion=0.13, recent=100, console_log=False):

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

    idx = len(data)

    recent_d = []
    for x in data[idx-recent+1:idx]:
        recent_d += x
    new_counter = numbers_counter + Counter(recent_d)
    
    least_commons = [x[0] for x in new_counter.most_common()[-1*least_common_size:]]

    guess_list = []
    for i in range(0, iterations):
        guess = sample(least_commons, 6)
        guess_list.append(guess)

    if console_log:
        print('================================')
        print('guess_list: %s' % guess_list)

    return guess_list