boxtokens
=================

Basic module for interacting with the Box.com API that includes some helpful functions for dealing with refreshing an access_token. This module is mainly used to get an access token from a refresh token. It assumes that you already have a valid set of tokens to start. Instructions of getting a set of tokens can be found in the link below. You will need to put the entire JSON response in tokens.json in the same directory as boxtokens.py.

An expired access_token can be automatically refreshed by calling get_new_token().



Documentation on the Box.com API can be found here:
https://developers.box.com/docs

Documentation on how to setup your app and get an authorization code can be found here:
https://developers.box.com/oauth
