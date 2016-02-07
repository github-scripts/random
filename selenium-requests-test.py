#!bin/python

import seleniumrequests

driver = seleniumrequests.PhantomJS()

resp = driver.request('GET', 'http://centos7vm/test.php', data={'name':'mytestuser'})

for i in resp.iter_lines():
    print i 



