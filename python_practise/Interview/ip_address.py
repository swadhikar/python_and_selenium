# Python script to convert all ip addresses into a new one
import re

old_ips = '192.0.0.1 This is the IP Addresses: 192.128.172.1 and 192.118.171.2'
new_ip = '127.0.0.1'

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

mo = re.match(pattern, old_ips)
if mo:
    print "mo.match() --> {}".format(mo.group())
else:
    print 'no mo object!'

so = re.search(pattern, old_ips)
print "so.group() --> {}".format(so.group())

new_ips = re.sub(pattern, new_ip, old_ips)
print new_ips

all_ips = re.findall(pattern, old_ips)
for ip in all_ips:
    print 'ip: {}'.format(ip)
