#!/usr/bin/env python

#
# Expand shortened URLs based on the return HTTP redirect headers
#
# This is the Python3 version of the original Python2 Script by Cudeso at
# https://github.com/cudeso/expandurl
#
#   Adarsh Rao on 2018-05-30
#   adarshnet at gmail dot com
#   license : FreeBSD 2 Clause (Same as prev.)
#
#   Original License#
#   Koen Van Impe on 2015-02-27
#   koen dot vanimpe at cudeso dot be
#   license New BSD : http://www.vanimpe.eu/license
#

import sys
import urllib.request, urllib.parse, urllib.error, http.client

url_ua = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
url_timeout = 15

def unshortenURL(url):
    currenturl = url.strip()
    previousurl = None
    while currenturl != previousurl:

        try:
            httprequest = http.client.urlsplit(currenturl)
            scheme = httprequest.scheme.lower()
            netloc = httprequest.netloc.lower()
            previousurl = currenturl
            if scheme == 'http':
                conn = http.client.HTTPConnection(netloc, timeout=url_timeout)
                req = currenturl[7+len(netloc):]
                location = "%s://%s" % (scheme, netloc)
            elif scheme=='https':
                conn = http.client.HTTPSConnection(netloc, timeout=url_timeout)
                req = currenturl[8+len(netloc):]
                location = "%s://%s" % (scheme, netloc)

            conn.request("HEAD", req, None, {'User-Agent': url_ua,'Accept': '*/*',})
            res = conn.getresponse()

            if res.status in [301, 304]:
                currenturl = res.getheader('Location')
                httprequest_redirect = http.client.urlsplit(currenturl)

                if httprequest_redirect.scheme.lower() != 'http' and httprequest_redirect.scheme.lower() != 'https':
                    # currenturl does not contain http(s)
                    currenturl = "%s://%s%s" % (scheme, netloc,currenturl)
        except:
            currenturl = url

    return currenturl

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            for url in f:
                unshorten = unshortenURL(url)
                print("%s \n \__%s" % (url.encode('utf-8'), unshorten))

    else:
        print("Please provide a file containing the URLs (one per line)")

if __name__ == '__main__':
    main()
