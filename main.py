import requests


result = requests.get(url='http://dev3.aliway.ru/export-system-settings/marketplace/1/get-info-categories/',
                      headers={
  'Cookie': 'csrftoken=qRtYtRWzIrPvUtWOJV9zx6X2p854GW4F7HJkdSSPuit5XWdP9wqIj1ZrR0pcGeuW; sessionid=6ci2kg843pfarkaamnn3y4tafskx8c9u'
}).json()
print(result)