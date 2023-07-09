from bs4 import BeautifulSoup

with open('website.html', encoding='utf8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

title = soup.title.string

code = soup.prettify() 

first_p = soup.p

all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    text_of_tag = tag.getText()   #to get text of each tag
    href_of_tag = tag.get('href')   #to get specefic attribute

# searching by name and id
heading = soup.find(name='h1', id='name')

# searching using class
section_heading = soup.find(name='h3', class_='heading')
text_of_heading = section_heading.getText()
name_of_heading = section_heading.name
attribute_of_heading = section_heading.get('class')

#holding specefic anchor tag using css selector method
company_url = soup.select_one(selector='p a')

#for id
name = soup.select_one(selector='#name')

#for class selector 
class_heading = soup.select('.heading')
print(class_heading)