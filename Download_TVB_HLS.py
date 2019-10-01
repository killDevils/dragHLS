url = 'http://news.tvb.com/story/...'




import urllib3
import ffmpy
from hanziconv import HanziConv

http = urllib3.PoolManager()
r = http.request('GET', url)
text = r.data.decode('utf-8')

text_file = open("/Users/tommy/Desktop/test.txt", "w")
text_file.write(text)
text_file.close()

aTagStart = text.find('<source src=')
start_quote = text.find('"', aTagStart)
end_quote = text.find('"', start_quote+1)
m3u8Url = text[start_quote+1:end_quote]

h1TagStart = text.find('<h1 class = ""')
h1start_quote = text.find('>', h1TagStart)
h1end_quote = text.find('<', h1start_quote+1)
h1Title = text[h1start_quote+1:h1end_quote]

timeTagStart = text.find('<span class = "time"')
timestart_quote = text.find('>', timeTagStart)
timeend_quote = text.find('<', timestart_quote+1)
timeStamp = text[timestart_quote+2:timeend_quote]

time1 = timeStamp.replace(' ', '_')
time2 = time1.replace(':', '')

name = h1Title
name1 = HanziConv.toSimplified(name)

ff = ffmpy.FFmpeg(
	inputs={m3u8Url: None},
	outputs={'/Users/tommy/Desktop/untitledfolder/'+time2+'_'+name1+'.mp4': None}
)
ff.run()
