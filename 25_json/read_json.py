# Read a json file
# JSON = JavaScript Object Notation

import urllib.request as req
import json

request = req.Request(
    url='http://globalmentoring.com.mx/api/personas.json',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with req.urlopen(request) as response:
    response_body = response.read()  # reads bytes
    decoded_body = response_body.decode('utf-8')
    json_response = json.loads(decoded_body)
    print(json_response)

    # In python JSON is converted to lists and dictionaries

    # Print only person names and age
    for person in json_response['personas']:
        print(f'Name: {person['nombre']}, Age: {person['edad']}')
