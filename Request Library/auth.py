import requests

# creating a basic authentication route which we can use in the browser
r = requests.get('https://httpbin.org/basic-auth/harshit/testing', auth=('harshit', 'testing')) 
# in auth passing tuple as a parameter which contains the username and password.

print(r.text)
# try to give wrong username and password then check the response
print(r)

# timeout

# r1 = requests.get('https://httpbin.org/delay/1', timeout=3)
r1 = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r1)