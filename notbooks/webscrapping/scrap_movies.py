import bs4,requests
import sys

url = "http://www.imdb.com/title/tt"
start = int(sys.argv[1])
end = int(sys.argv[2])
print start,end

def extractMovieTitle(mfile,start,n):
	i=start
	print i,n
	while i<=n:
		
		try:
			r = requests.get(url+str(i))
			rsoup = bs4.BeautifulSoup(r.text,from_encoding="utf-8")
			title = rsoup.find('h1',{'itemprop':'name'})
			mfile.write((title.getText()+"\n").encode('utf-8'))
			print "fetching "+str(i)
			print title.getText().encode('utf-8')
			i += 1
		except Exception as e:
			print str(e)+""
			i += 1
			continue

with open("movie_name_db_new.txt","a") as mfile:
    extractMovieTitle(mfile,start,end)
