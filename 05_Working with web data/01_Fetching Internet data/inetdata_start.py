'''we're going to just retrieve data from a server and print the results. 
So in order to make a request to a web server, I need to import the url lib request module. 
So I'll so that first. So this module provides the classes and code I need to make http requests.'''

import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()