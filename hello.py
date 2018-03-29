#!/usr/bin/python
from github3 import login

gh = login('savagecm', password='savage221')

sigmavirus24 = gh.me()
# <User [sigmavirus24:Ian Stapleton Cordasco]>

print(sigmavirus24.name)
# Ian Stapleton Cordasco
print(sigmavirus24.login)
# sigmavirus24
print(sigmavirus24.followers_count)
# 4

for f in gh.followers():
    print(str(f))

kennethreitz = gh.user('savagecm')
# <User [kennethreitz:Kenneth Reitz]>

print(kennethreitz.name)
print(kennethreitz.login)
print(kennethreitz.followers_count)
