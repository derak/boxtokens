#!/usr/bin/python

"""Basic module for interacting with the Box.com API.
This module is mainly used to get a access token and from a 
refresh token. It assumes that you already have a valid set
of tokens to start with.

An expired access_token can be automatically refreshed by
calling get_new_token().

Copyright (c) 2014 Derak Berreyesa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = "Derak Berreyesa (github.com/derak)"
__version__ = "1.0"

import urllib
import urllib2
import json
import sys

from urllib2 import Request, urlopen, URLError
from collections import defaultdict

base_url = 'https://www.box.com/api/2.0'
token_url = 'https://www.box.com/api/oauth2/token'
token_file = 'tokens.json'

def read_tokens():
    """Read JSON input from file"""
    with open(token_file) as json_file:
        json_obj = json.load(json_file)
    return json_obj

def write_tokens(json_obj):
    """Write JSON output to file"""
    with open(token_file, 'w') as json_file:
        json.dump(json_obj, json_file)

def tree(): 
    return defaultdict(tree)

def get_post_values():
    """Get values for POST"""

    tokens = read_tokens()

    values = tree()
    values['grant_type'] = 'refresh_token'
    values['refresh_token'] = tokens['refresh_token']
    values['client_id'] = 'YOUR_CLIENT_ID'
    values['client_secret'] = 'YOUR_CLIENT_SECRET'
    #data = json.dumps(values)

    # convert str to bytes (ensure encoding is OK)
    #post_data = data.encode('utf-8')
    data = urllib.urlencode(values)

    #print 'post values'
    #print json.dumps(values, sort_keys=True, indent=2, separators=(',', ': '))
    return data

def get_new_token():
    """Make API call to refresh access_token using refresh_token"""

    token_obj = call_api(token_url,'post')
    write_tokens(token_obj)
    #print json.dumps(token_obj, sort_keys=True, indent=2, separators=(',', ': '))
    return token_obj

def call_api(url, method='get'):
    """Make call to API"""

    if method == 'get':
        tokens = read_tokens()
        headers = {'Authorization' : 'Bearer ' + tokens['access_token'],
                   'Accept' : 'application/json',
                   'Content-Type' : 'application/json' }

        req = urllib2.Request(url=url, headers=headers)  #GET
    else:
        data = get_post_values()
        #req = urllib2.Request(url, data, headers)       #headers is not needed
        req = urllib2.Request(url, data)                 #POST

    #print 'Method: '+req.get_method()

    try:
        response = urllib2.urlopen(req)
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'Failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        json_obj = json.load(response)   
        return json_obj

    #print json.dumps(json_obj)
    #print json.dumps(json_obj, sort_keys=True, indent=2, separators=(',', ': '))
    #return json_obj

if __name__ == '__main__':
 
    #refresh access_token if needed
    #tokens = get_new_token()

    # print the authenticated users folder information
    url = base_url + '/folders/0'
    #url = base_url + '/events'

    folders = call_api(url)

    # check if token needs to be refreshed
    if folders is None:
        print "token is being refreshed"
        tokens = get_new_token()
        folders = call_api(url)


    #print json.dumps(folders)
    print json.dumps(folders, sort_keys=True, indent=2, separators=(',', ': '))

