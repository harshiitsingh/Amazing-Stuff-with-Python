'''
pip install bs4

pip install lxml

lxml -> to parse html files from websites to python objects,
there are different ways to parse the html code but lxml parser is best'''

from bs4 import BeautifulSoup

with open('home.html', 'r') as f:
    content = f.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    tags = soup.find('h5')
    print(tags)
    
    tags = soup.find('p')
    print(tags)
    
    all_tags = soup.find_all('p')
    print(all_tags) # since it is a list, therefore we can iterate over all the tags
    
    for tags in all_tags:
        print(tags.text) # Note: Local variables have more priority than global variables.