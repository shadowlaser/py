from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if tag== 'a':
			print('<%s>'%tag)
			print('%s'%attrs)

	def handle_endtag(self,tag):
		# print('</%s>'%tag)
		pass
	def handle_startendtag(self, tag, attrs):
		# print('<%s/>' % tag)
		pass
	def handle_data(self, data):
		print(data)
		pass
	def handle_comment(self, data):
		print('<!--', data,	 '-->')
		pass
	def handle_entityref(self, name):
		# print('&%s;' % name)
		pass
	def handle_charref(self, name):
		# print('&#%s;' % name)
		pass




with request.urlopen('http://xx/ht.html') as f:
	print('Status:',f.status,f.reason)
	
	data=f.read().decode('GBK')
	print('Data: %s'%data)
	parser = MyHTMLParser()
	parser.feed(data)

	

