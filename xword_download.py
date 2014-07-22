"""
import datetime
daterange = lambda d1, d2: (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))
for d in daterange(date1, date2):
    getday(d)
    ... do some stuff

date1 = datetime.date(2004, 9, 25)
date2 = datetime.date(2004, 9, 26)
print(getday(date1)['grid'])
"""
import requests

def getday(d):
    payload = {'date': d.strftime('%m/%d/%Y')}
    myAuth = ('username', 'password')
    r = requests.get('http://www.xwordinfo.com/JSON/Data.aspx', auth=myAuth, params=payload)
    return r.json()


