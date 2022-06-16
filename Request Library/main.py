'''
REQUEST LIBRARY - Helps in post info, download images, send authentication info for basic laws and forms,
follow redirects etc from a website. 
Request webpages, post data, read JSON etc.

To parse the info from a website use beautiful soup.'''

import requests

# to fetch/get any webpage
r = requests.get('url')

print(r)

# to get the all attributes and methods available in the response object r
print(dir(r))
# to learn how to use those methods in detail
print(help(r))

# to get the content of the response in unicode
print(r.text) # --> returns the html code used in the page.

# to download the image
i = requests.get('image url')
print(r.content) # --> returns the bytes from that image. 
# so we take those bytes and save it our machine for that-
with open('nameofimage.png', 'wb') as f: # wb mode means write byte
    f.write(i.content)

# to check whether we are getting a good response from the site or not.
print(r.status_code)
print(i.status_code) 
''' Some HTTP status code are:
200 - A Success code
300 - a redirect
400 are client errors. (either permission error)
In 500 errors are the server errors, when a site just crashes and you can't access a site.
'''

# to check the site is responsive or not
print(r.ok) # if return true, means it's okay for anything less than 400 response.
# for client or server error, it returns false.

# to get all the headers with the response
print(r.headers)