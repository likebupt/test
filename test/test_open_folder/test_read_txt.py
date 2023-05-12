from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame

future = list()
for i in range(1, 13):
	date = '1968-%02d' % i
	future.append([date])
future = DataFrame(future)
print("future:", future)
future.columns = ['ds']
future['ds']= to_datetime(future['ds'])
print("update future:", future)