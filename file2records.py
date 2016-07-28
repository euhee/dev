import json
from collections import Counter
import matplotlib.pyplot as plt
from pandas import DataFrame, Series 
import pandas as pd

path='C:/Users/USER/Documents/github/Python/Data_Analysis/Data/sample02.txt'
records=[json.loads(line) for line in open(path)]
print(len(records))
print("")
print(records[0])
print("")
print(records[0]['tz'])
print("")
time_zones=[record['tz'] for record in records if 'tz' in record]
print(time_zones[:10])
def get_counts(mylist):
    counts={}
    for x in mylist:
        if x in counts:
            counts[x] += 1
        else:
            counts[x]=1
    return counts
counts=get_counts(time_zones)
print(counts['America/New_York'])

#########word counts
counts=Counter(time_zones)
print(counts.most_common(10))

########plotting
frame = DataFrame(records) 
print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts() 
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing') 
clean_tz[clean_tz == ''] = 'Unknown' 
tz_counts = clean_tz.value_counts() 
print(tz_counts[:10])

fig=plt.figure()
tz_counts[:10].plot(kind='barh')
plt.show()
fig.savefig('figpath.png', dpi=400, bbox_inches='tight')







