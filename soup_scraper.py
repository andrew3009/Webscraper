import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.game.co.uk/webapp/wcs/stores/servlet/HubArticleView?langId=44&searchBtn=z&msg=&showResultsPage=true&DM_PersistentCookieCreated=true&sType=SimpleSearch&hubId=2646251&predictiveSearchURL=&resultCatEntryType=2&articleId=2646251&catalogId=10201&pageView=image&searchCount=1&searchTerm=ps5&storeId=10151&beginIndex=0&pageSize=48&ddkey=http%3AAjaxCatalogSearch')
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for section_tag in soup.find_all('section'):
  a_tag = section_tag.find('a')
  urls.append(a_tag.attrs['href'])
  print(a_tag.attrs['href'])