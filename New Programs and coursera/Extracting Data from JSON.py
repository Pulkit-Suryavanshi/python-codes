import urllib.parse,urllib.error
import urllib.request as ur
import json

json_url = input("Enter location: ")
if(len(json_url)<1):
    json_url='http://py4e-data.dr-chuck.net/comments_595055.json'
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)