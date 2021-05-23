from database import load_649
from strategy.less_picked_first import less_picked_first
from strategy.random_pick import random_pick
from strategy.continues_pick import continues_pick
from strategy.exclude_last import exclude_last

data = load_649()
data_list = [x['ordered_numbers'] for x in data]
#data_list = data_list[int(len(data_list)*0.75):]

pool = [str(x).zfill(2) for x in range(1, 50)]
print('pool: %s' % pool)

print('=========================')
avg = random_pick(data_list, pool)
print('random_pick: %s' % avg)

print('=========================')
avg = less_picked_first(data_list, pool)
print('less_picked_first: %s' % avg)

print('=========================')
avg = continues_pick(data_list, pool)
print('continues_pick: %s' % avg)

print('=========================')
avg = exclude_last(data_list, pool)
print('exclude_last: %s' % avg)