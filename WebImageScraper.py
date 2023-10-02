import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

x = 'https://www.ithinkilikeyou.net/wp-content/uploads/2023/10/'
url = x
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

base_url = x

file_urls = []

for link in soup.find_all('a'):
    file_url = base_url + link.get('href')
    file_urls.append(file_url)
    print(file_url)

parsed_url = urlparse(url)
directories = parsed_url.path.split('/')[-3:]
directory_name = '_'.join(directories)

file_path = os.path.join(os.getcwd(), f"{directory_name}_ripped_links.txt")

if os.path.exists(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    file_path = f"{file_name}_1{file_extension}"

with open(file_path, 'w') as file:
    file.write('\n'.join(file_urls))
    print(f"File '{directory_name}_ripped_links.txt' saved successfully at {file_path}")
