import re
import requests
from bs4 import BeautifulSoup
def extract_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            urls.append(href)
    return urls
def is_vulnerable(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all('script')
    for script in scripts:
        if re.search(r'<script.*?>', str(script)):
            return True
    return False
def main(url):
    urls = extract_urls(url)
    for url in urls:
        if is_vulnerable(url):
            print(f"Vulnerable URL: {url}")
        else:
            print(f"Secure URL: {url}")
if __name__ == '__main__':
    target_url = input("Enter the target URL: ")
    main(target_url)
