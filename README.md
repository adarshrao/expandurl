expandurl.py
=============
Expand a shortened URL to the full URL.

This function expands a shortened URL (like in Twitter tweets) to the full URL.

A derivative of the original by Cudeso - https://github.com/cudeso/expandurl . I used the 2to3.py to convert the code into Python3.

This function reads the HTTP redirect codes and follows them. It should work for both http and https.

The given user agent is the one used by the Google bot.

The function reads the URLs from a file (one URL per line) and fetches the redirects.

No full page request is done, only the HEAD is requested.

If an error occurs then the original URL is returned.

Usage
------------
```expandurl.py urlfile.txt```

Output
------------
```
b'https://t.co/kNgW6nQor6\n'
 \__https://haptic.al/

b'https://t.co/e9UeNQPxk6'
 \__https://mixpanel.com
