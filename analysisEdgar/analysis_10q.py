import os
location_10k = '/Users/nanditadwivedi/Documents/courses/Term2/bigProject/portfolio-risk-assessment-using-ml/data/scraped_10k'

os.chdir(location_10k)
file_list = [fname for fname in os.listdir()]

if '.DS_Store' in file_list:
	file_list.remove('.DS_Store')

k_filtered = []

for cikdir in file_list:
	file_list1 = [fname for fname in os.listdir(location_10k + '/' + cikdir + '/clean_data/')]
	count=0
	for file in file_list1:
		date = file.split('_')[1].split('.')[0]
		if (date>'2008-01-01'):
			count+=1
	if (count>=12):
		k_filtered.append(cikdir)
print(len(k_filtered))


location_10q = '/Users/nanditadwivedi/Documents/courses/Term2/bigProject/portfolio-risk-assessment-using-ml/data/scraped_10q'

os.chdir(location_10q)
file_list = [fname for fname in os.listdir()]

if '.DS_Store' in file_list:
	file_list.remove('.DS_Store')

q_filtered = []

for cikdir in file_list:
	file_list1 = [fname for fname in os.listdir(location_10q + '/' + cikdir + '/clean_data/')]
	count=0
	for file in file_list1:
		date = file.split('_')[1].split('.')[0]
		if (date>'2008-01-01'):
			count+=1
	if (count>=33):
		q_filtered.append(cikdir)
print(len(q_filtered))

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))

import pandas as pd 

filtered_cik = intersection(k_filtered, q_filtered)
filtered_cik = pd.DataFrame(filtered_cik,columns=['cik']).astype('int64')

cik_tickers = '/Users/nanditadwivedi/Documents/courses/Term2/bigProject/portfolio-risk-assessment-using-ml/AllSecTickers.csv'
cikListFile = pd.read_csv(cik_tickers)
result = pd.merge(filtered_cik, cikListFile, on='cik')

result.to_csv('/Users/nanditadwivedi/Documents/courses/Term2/bigProject/Edgar_filter_cik_ticker_map.csv')






