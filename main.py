from database import load_649
from strategy.less_picked_first import less_picked_first
from strategy.recent_less_picked_first import recent_less_picked_first
from strategy.most_picked_first import most_picked_first
from strategy.random_pick import random_pick
from strategy.continues_pick import continues_pick
from strategy.exclude_last import exclude_last

import forcast

data = load_649()
data_list = [x['ordered_numbers'] for x in data]
#data_list = data_list[int(len(data_list)*0.5):]

pool = [str(x).zfill(2) for x in range(1, 50)]
print('pool: %s' % pool)


print('=========================')
guess_list = forcast.recent_less_picked_first(
    data_list, pool, iterations=1, portion=0.13, recent=100)
print('guess_list: %s' % guess_list)

print('=========================')
guess_list = forcast.recent_less_picked_first(
    data_list, pool, iterations=1, portion=0.13, recent=10)
print('guess_list: %s' % guess_list)

'''
print('=========================')
avg = random_pick(data_list, pool)
print('random_pick: %s' % avg)

print('=========================')
avg = less_picked_first(data_list, pool, portion=0.5)
print('less_picked_first (portion 0.5): %s' % avg)

print('=========================')
avg = less_picked_first(data_list, pool, portion=0.33)
print('less_picked_first (portion 0.33): %s' % avg)

print('=========================')
avg = less_picked_first(data_list, pool, portion=0.13)
print('less_picked_first (portion 0.13): %s' % avg)

print('=========================')
avg = recent_less_picked_first(data_list, pool, portion=0.13, recent=250)
print('recent_less_picked_first (portion 0.13, recent 250): %s' % avg)

print('=========================')
avg = recent_less_picked_first(data_list, pool, portion=0.13, recent=100)
print('recent_less_picked_first (portion 0.13, recent 100): %s' % avg)

print('=========================')
avg = recent_less_picked_first(data_list, pool, portion=0.13, recent=50)
print('recent_less_picked_first (portion 0.13, recent 50): %s' % avg)

print('=========================')
avg = recent_less_picked_first(data_list, pool, portion=0.13, recent=25)
print('recent_less_picked_first (portion 0.13, recent 25): %s' % avg)

print('=========================')
avg = recent_less_picked_first(data_list, pool, portion=0.13, recent=10)
print('recent_less_picked_first (portion 0.13, recent 10): %s' % avg)

print('=========================')
avg = most_picked_first(data_list, pool, portion=0.5)
print('most_picked_first (portion 0.5): %s' % avg)

print('=========================')
avg = most_picked_first(data_list, pool, portion=0.33)
print('most_picked_first (portion 0.33): %s' % avg)

print('=========================')
avg = most_picked_first(data_list, pool, portion=0.13)
print('most_picked_first (portion 0.13): %s' % avg)

print('=========================')
avg = continues_pick(data_list, pool)
print('continues_pick: %s' % avg)

print('=========================')
avg = exclude_last(data_list, pool)
print('exclude_last: %s' % avg)
'''
print('=========================')