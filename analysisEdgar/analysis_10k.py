

import os

location_10k = '/Users/nanditadwivedi/Documents/courses/Term2/bigProject/portfolio-risk-assessment-using-ml/data/scraped_10k'

os.chdir(location_10k)
file_list = [fname for fname in os.listdir()]

if '.DS_Store' in file_list:
	file_list.remove('.DS_Store')

for cikdir in file_list:
	file_list1 = [fname for fname in os.listdir(location_10k + '/' + cikdir + '/clean_data/')]
	count=0
	for file in file_list1:
		date = file.split('_')[1].split('.')[0]
		if (date>'2008-01-01'):
			count+=1
	if (count>=12):
		print('include')




