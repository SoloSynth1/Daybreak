# Daybreak
A simple dictionary attacker for HTTP Basic Authentication / Digest Authentication.

This is written as an self-taught tutorial on using (or rather, abusing) Requests' HTTPBasicAuth.

The main.py reads URLs from address.csv and try to send a request to the listed hosts.
If the response is 401 - Unauthorized, it will proceed to do a dictionary attack using wordlist.csv's 'user,password' combinaton.

The URLs contained in address.csv are extracted from Shodan search (https://www.shodan.io/) and are meant to act as placeholder/example.
