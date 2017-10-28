import time
import requests as rq
from bs4 import BeautifulSoup
import re
import dateutil
import dateutil.parser


# Adding Headers to Requests (To pretend you are not a bot)
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5)'}
# url = "http://boxofficemojo.com/movies/?id=biglebowski.htm"
# resp = requests.get(url, headers=headers)
# if r.ok:
#     soup = BeautifulSoup(r.text, 'lxml')



# helpers
def get_movie_value(soup, field_name):
    '''Grab a value from boxofficemojo HTML

    Takes a string attribute of a movie on the page and
    returns the string in the next sibling object
    (the value for that attribute)
    or None if nothing is found.
    '''
    obj = soup.find(text=re.compile(field_name))
    if not obj:
        return None
    # this works for most of the values
    next_sibling = obj.findNextSibling()
    if next_sibling:
        return next_sibling.text
    else:
        return None


def to_date(datestring):
    try:
        date = dateutil.parser.parse(datestring)
        return date
    except:
        return None


def money_to_int(moneystring):
    try:
        moneystring = moneystring.replace('$', '').replace(',', '')
        return int(moneystring)
    except:
        return None


def runtime_to_minutes(runtimestring):
    try:
        runtime = runtimestring.split()
        minutes = int(runtime[0]) * 60 + int(runtime[2])
        return minutes
    except:
        return 0


# variables year and number of pages to construct url
year = range(2000, 2011, 1) #marked out to add 2016 data
# year = '2016'
num_pages = range(1,8)

# loop through variables above and create urls
list_by_year_by_page = []
for i in year:
    for j in num_pages:
        year_url = 'http://www.boxofficemojo.com/yearly/chart/?page=' + str(j) + '&view=releasedate&view2=domestic&yr='+ str(i) + '&adjust_mo=&adjust_yr=2016&p=.htm'
        time.sleep(0.25)
        list_by_year_by_page.append(year_url)

###
# c_url = 'http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2014&adjust_mo=&adjust_yr=2016&p=.htm'
#
# response = rq.get(c_url)
# page = response.text
# soup = BeautifulSoup(page)
# all_links = soup.findAll('a',href = re.compile('/movies/\?*id='))
# links_list=[]
# for link in all_links:
#     links_list.append(link['href'])

# loop through urls and extract hyperlinks:

links_list = []
for l in list_by_year_by_page:
    response = rq.get(l)
    page = response.text
    soup = BeautifulSoup(page)
    all_links = soup.findAll('a', href=re.compile('/movies/\?*id='))
    for link in all_links:
        links_list.append(link['href'])
        # time.sleep(.50)



movie_data = []  # list of movie dictionary
for l in set(links_list):
    i = 'http://www.boxofficemojo.com' + l + '&adjust_yr=2016&p=.htm'
    response = rq.get(i)
    page = response.text
    soup = BeautifulSoup(page)

    raw_title_string = soup.find('title').text
    try:
        title = raw_title_string.split('(')[0].strip()
    except:
        title = 'na'
    rating = get_movie_value(soup, 'MPAA Rating')
    raw_release_date = get_movie_value(soup, 'Release Date')
    release_date = to_date(raw_release_date)
    raw_domestic_total_gross = get_movie_value(soup, 'Domestic Total')
    domestic_total_gross = money_to_int(raw_domestic_total_gross)
    raw_runtime = get_movie_value(soup, 'Runtime')
    runtime = runtime_to_minutes(raw_runtime)
    production_budget = get_movie_value(soup, 'Production Budget:')
    genre = get_movie_value(soup, 'Genre:')

    headers = ['movie title', 'domestic total gross',
               'release date', 'runtime (mins)', 'rating', 'production_budget', 'genre']

    movie_dict = dict(zip(headers, [title,
                                    domestic_total_gross,
                                    release_date,
                                    runtime,
                                    rating,
                                    production_budget,
                                    genre]))
    movie_data.append(movie_dict)
    time.sleep(0.13)

import pandas as pd
movie_data2 = pd.DataFrame(movie_data)
# movie_data1.to_csv('movie_data_2016.csv')


#
# movie_links = open('movie_links.txt', 'w')
# for item in links_list:
#     movie_links.write("%s\n" % item)
#

#movie_data = pd.read_csv('movie_data.csv')
#
#
#
#

#

#
# with open('movie_links.txt') as f:
#     links_list = f.read().splitlines()