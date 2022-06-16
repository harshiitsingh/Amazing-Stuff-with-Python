import requests

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params= payload)

print(r.text)
print(r.url) # --> returns the actual url with parameters in it

# TO POST SOME DATA TO THIS ROUTE.
payload1 = {'username': 'harshit', 'password': 'testing'}
r1 = requests.post('https://httpbin.org/post', data= payload1)

print(r1.text) # --> returns args, forms etc. check the html or source code of the url, in that check forms, 
# that which type of data does it required and then set payload according to that.

# as we are geting json response from the httpbin.org website
# so JSON response is very common while working with certain APIs
# so instead of using .text method use .json method.

print(r1.json()) # it created the python dictionary from that json response
r1_dict = r1.json() # so you can access the key-value pair from that dictionary.
print(r1_dict['form'])

# similary you can create the pull request also.