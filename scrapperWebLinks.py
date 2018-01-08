#importing re, urllib and bs4 makes our task easy
import re                                          #Regular Expressions - for string search
import urllib.request, urllib.parse, urllib.error  #For talking to webpages and returning nicely structred data
from bs4 import BeautifulSoup                      #For scraping HTML or XML tags
import ssl                                         #To avoid error due to SSL certificates

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Requires little modifications for more personalization- but basic framework is developed here
url = input("Enter the URL: ")                     #Sample URL input: http://py4e-data.dr-chuck.net/known_by_Riham.html 
for i in range(7):
	html = urllib.request.urlopen(url, context= ctx).read() #reading the webpage data as a string with \n characters
	soup = BeautifulSoup(html, "lxml")             #building tree to extract tags
	tags = soup('a')                               #All Anchor tags(<a href=''></a>) will be returned 
#	print(tags)
	url = tags[17].get('href', None)

#	print(url)
#	for tag in tags:
#		print(tag.get('href', None))
#print(url)
print(re.findall(('_\S+_(\S+).html'), url)[0], end='')

#Returning the last name at the end of 7 iterations on opening 18th link each time from the webpage retrieved