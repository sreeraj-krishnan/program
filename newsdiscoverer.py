#!/usr/bin/python3.4
import sys
import oauth2 as oauth
import json
import httplib2
import os

def process_all( n ):
	n = 0 # not implemented
	process_all_handles( [ 'NewIndianXpress', 'thehindu' ])
	

def write_to_file( source, filename, content,date ):
	try:
		fullpath = source+'/'+date+'/'+filename+'.txt'
		print (fullpath)
		os.makedirs(os.path.dirname(fullpath), exist_ok=True)
		file = open(fullpath,'w+')
		file.write(content)
		file.close()
	except Exception as e:
		print( 'in write_to_file' , e )
		
def get_url_content( url ):
	http = httplib2.Http()
	#print(url)
	headers, body = http.request( url )
	return str(body)

def process_all_handles( handles ):
	for handle in handles:
		handledata =  get_title_content(handle) 
		for each in handledata:
			try:
				urlcontent = get_url_content( each.get('contenturl'))
				title = each.get('title')
				d= each.get('date')
				#print( title )
				#print( d )
				filename = title.replace(' ','').replace('/','').replace(':','').replace('.','').replace(',','').split('http')[0]
				
				write_to_file(source=handle, filename=filename, content=urlcontent,date=d)
			except Exception as e:
				print('exception in process_all_handles',e )

def get_title_content( twitterhandle ):
	consumer = oauth.Consumer(key="5low1XEYPhugHUpn0zyhdYHgj", secret="DfDofxgrjzJHCtM23MKlZ5YQV8W87ALSnnEKAR52RnBorI0drK")
	request_token_url = str("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=") + twitterhandle + str("&count=100")

	request_token_url.replace('\{handle\}', twitterhandle)
	#print( request_token_url)
	client = oauth.Client(consumer)

	header = { 'Accept': 'application/json' , 'Content-Type' : 'application/json' }

	resp, content = client.request(request_token_url, "GET", headers=header)
	jsonout = json.loads( content.decode('utf-8') )
	contents=[]
	#print(  twitterhandle )
	for obj in jsonout:
		try:
			title = obj.get('text')
			contenturls=''
			entities = obj.get('entities')
			for url in entities.get('urls' ):
				contenturls = url.get('url')
				 
			#print( contenturls )
			d = obj.get('created_at')
			n = len(d.split(' '))
			year = d.split(' ')[n-1]
			month = d.split(' ')[1]
			day = d.split(' ')[2]
			combineddate=day+'-'+month+'-'+year
			#print( combineddate )
			contents.append( {'date' : combineddate, 'title': title, 'contenturl' : contenturls} )
		except Exception as e:
			print( 'in get_title_content' , e)
			
	return contents
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage : newsdiscoverer.py <last_n_hours>')
		sys.exit(0)
	process_all( int ( sys.argv[1] ) )
