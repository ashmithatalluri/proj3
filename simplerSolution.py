def get_page(url,soupify=False):
	from bs4 import BeautifulSoup as soup
	import html5lib 
	import requests
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	rawtext=requests.get(url,headers=headers).text
	if soupify==True:
		return soup(rawtext,'html5lib')
	else:
		return rawtext
	

url="https://www.w3schools.com/"
pagesoup=get_page(url,soupify=True)
print(soup)