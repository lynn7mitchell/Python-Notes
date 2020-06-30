from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array
# Counter
li = [1,2,3,4,5,6,7,7]
print('counter', Counter(li))

sentence = 'stuff and things'
print('counter', Counter(sentence))

# defaultdict
# give defaultdict a callable action as a default
dictionary = defaultdict(lambda: 5, {'a':1, 'b':2})
# doesn't exist so defaults to defaultdict (lambda : 5)
print(dictionary['c'])


# !!!! ORDEREDDICT is not needed anymore since python3 has made dictionaries ordered by default !!!!
print('!!!! ORDEREDDICT is not needed anymore since python3 has made dictionaries ordered by default !!!!')
# ordereddict
# retains the order that you insert
d = OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['b']=2
d2['a']=1

# false because OrderedDict() keeps the order the same as inserted
print(d2 == d)


# datetime
print('datetime', datetime.time(5,45,2))
print('datetime', datetime.date.today())


#arrays take up less memory than lists
# have to give typecode
# i = int (type)
arr = array('i', [1,2,3])
print('array',arr)

