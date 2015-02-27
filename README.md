expandurl.py
=============
Expand a shortened URL to the full URL.

This function expands a shortened URL (like in Twitter tweets) to the full URL.

It is inspired on code from urlclean.

A lot of the same functionality can be achieved by using urllib2.url but this fetches the full page with the Python browser identification. Unfortunately some sites block your access if you use Python as the browser identification. This is why I wrote my own function.

This function reads the HTTP redirect codes and follows them. It should work for both http and https.

The given user agent is the one used by the Google bot.

Some redirects do not contain the "http://mysite.com" in the Location header. This has been dealt with.

The function reads the URLs from a file (one URL per line) and fetches the redirects.

No full page request is done, only the HEAD is requested.

If an error occurs then the original URL is returned.

Usage
------------
```expandurl.py urllist```

Output
------------
```
http://t.co/t2XiWoXL9m
 
 \__http://m.motherjones.com/politics/2015/01/republicans-free-city-wifi-municipal-broadband-socialism?utm_content=bufferc0538&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer
http://t.co/WQpQwmPFGd
 
 \__http://deredactie.be/cm/vrtnieuws/politiek/1.2253446
https://t.co/w1Sd1dmUL3
 
 \__https://nomadphp.com/2014/12/19/nomadphp-2015-03-eu/
http://t.co/BGZ52avOB5
 
 \__http://blog.dynamoo.com/2015/02/an-analysis-of-reported-equation-group.html?spref=tw
https://t.co/K04nbfyWST
 
 \__https://bitbucket.org/mihaila/bindead/wiki/Home
```

urlclean
------------
module that resolves and cleans up urls 
 https://github.com/stef/urlclean


