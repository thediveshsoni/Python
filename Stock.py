import re
import urllib.request
print("WELCOME TO STOCK INFORMATION APPLICATION")
stock=input("Enter the Stock name: ")
url="http://www.google.com/finance?q="+stock
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
m=re.search('meta itemprop="price"',data1)
start=m.start()
end=start+100
newString=data1[start:end]
m=re.search('content="',newString)
start=m.end()
newString1=newString[start:]
m=re.search("/",newString1)
start=0
end=m.end()-3
final=newString1[0:end]
print("The Stock Price of "+stock+" is "+final)
