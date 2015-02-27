#!/usr/bin/env python

#
# Expand shortened URLs
#
# Expand shortened URLs based on the return HTTP redirect headers
# Inspired by 'urlclean' by Stefan Marsiske
#   https://github.com/stef/urlclean
# 
#  Koen Van Impe on 2015-02-27
#   koen dot vanimpe at cudeso dot be
#   license New BSD : http://www.vanimpe.eu/license
#

import sys
import urllib, httplib

url_ua = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
url_timeout = 15


def unshortenURL(url):
    currenturl = url.strip()
    previousurl = None
    while currenturl != previousurl:

        try:
            httprequest = httplib.urlsplit(currenturl)
            scheme = httprequest.scheme.lower()
            netloc = httprequest.netloc.lower()
            previousurl = currenturl
            if scheme == 'http':
                conn = httplib.HTTPConnection(netloc, timeout=url_timeout)
                req = currenturl[7+len(netloc):]
                location = "%s://%s" % (scheme, netloc)
            elif scheme=='https':
                conn = httplib.HTTPSConnection(netloc, timeout=url_timeout)
                req = currenturl[8+len(netloc):]
                location = "%s://%s" % (scheme, netloc)           

            conn.request("HEAD", req, None, {'User-Agent': url_ua,'Accept': '*/*',})
            res = conn.getresponse()

            if res.status in [301, 304]:
                currenturl = res.getheader('Location')
                httprequest_redirect = httplib.urlsplit(currenturl)

                if httprequest_redirect.scheme.lower() != 'http' and httprequest_redirect.scheme.lower() != 'https':
                    # currenturl does not contain http(s) 
                    currenturl = "%s://%s%s" % (scheme, netloc,currenturl)
        except:
            currenturl = url

    return currenturl
    
def main():
    if len(sys.argv) == 2:
        f = open (sys.argv[1])
        for url in f:
            unshorten = unshortenURL(url)
            print "%s \n \__%s" % (url.encode('utf-8'), unshorten)

    else:
        print "Please provide a file containing the URLs (one per line)"

if __name__ == '__main__':
    main()
