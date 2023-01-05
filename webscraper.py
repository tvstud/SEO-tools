import requests
from bs4 import BeautifulSoup

def check_metadata(url):
    # Make a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the title element
    title_element = soup.find('title')
    if title_element:
        # Get the text of the title element
        title = title_element.text
    else:
        # Set the title to an empty string if it was not found
        title = ''
        
    # Find the meta element with the name attribute 'description'
    description_element = soup.find('meta', attrs={'name': 'description'})
    if description_element:
        # Get the value of the content attribute
        description = description_element['content']
    else:
        # Set the description to an empty string if it was not found
        description = ''
        
    # Print the title and description
    print(f'Title: {title}')
    print(f'Description: {description}')

# Test the function with a sample URL
check_metadata('https://harrisontuja.com')
