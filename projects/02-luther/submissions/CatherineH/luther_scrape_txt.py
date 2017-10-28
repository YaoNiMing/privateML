# Best value films to produce
# -regress cost/grossed for a few genres and compare
# earning by genres over time
# pull top 100 for last 16 years
# genre over time
# 1000 films
# economic status of us? unemployment?
#	look at median income, control for movie funding
#	also pull # of movies release by year maybe
#of best earning genres by time can look at best value (e.g. gross-cost)

#numpy and pandas
#focus on linear regression rn
#make it work, then try pickling
#for mining data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import re
from time import sleep
import codecs
# %matplotlib inline
urllist = [2011, 2012, 2013, 2014, 2015, 2016]
#to be added to urllist after it's working
#2016-2000
#2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000]
url_top = []
for item in urllist:
	item = str(item)
	url_top.append(item)

count = 1112

for url in url_top:
	url_temp_meta= 'http://www.boxofficemojo.com/yearly/chart/?yr=' + url + '&adjust_yr=2016&p=.htm'
	print url_temp_meta
	response = requests.get(url_temp_meta)
	print response.status_code
	soup = BeautifulSoup(requests.get(url_temp_meta).text,'html.parser')
	all_links = soup.findAll('a',href = re.compile('/movies/\?*id='))
	for item in all_links:
		item = (item['href'])
		url_temp = 'http://www.boxofficemojo.com' + item
		print url_temp
		sleep(.5)
		response = requests.get(url_temp)
		soup_temp = BeautifulSoup(requests.get(url_temp).text)
		soup_temp = str(soup_temp)
		count = count + 1
		countx = str(count)
		file_name = item
		with open(countx, 'w') as f:
			f.write(soup_temp)
			print(file_name)


		# count1 = str(count)
		# with (open(count1,'.html'))as savefile:
		# 	savefile.write(soup_temp.prettify())
		# 	savefile.close()
		# fp = codecs.open('lutherhtml.txt','a', 'utf-8')
		# fp.write(soup_temp.prettify())
		# fp.close()