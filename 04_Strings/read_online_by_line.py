import urllib.request as req
import os

_file_path = os.path.abspath(__file__)
_dir_path = os.path.dirname(_file_path)

request = req.Request(
    url='http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

words = []

with req.urlopen(request) as msg:
    for line in msg:
        words_per_line = line.decode('utf-8').split()
        for word in words_per_line:
            words.append(word)

print(words)
