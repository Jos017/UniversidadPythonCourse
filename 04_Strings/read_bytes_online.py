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

with req.urlopen(request) as msg:
    content_bytes = msg.read()
    content_string = content_bytes.decode('utf-8')
    print(content_string)

with open(os.path.join(_dir_path, 'new_file.txt'), 'w', encoding='utf-8') as file:
    file.write(content_string)
