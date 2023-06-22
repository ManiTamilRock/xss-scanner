import requests

def scan_for_xss(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the HTML content
        html_content = response.text

        # Search for potential XSS vulnerabilities
        if "<script>" in html_content:
            print("Potential XSS vulnerability found!")
        else:
            print("No XSS vulnerability found.")
    else:
        print("Error: Failed to fetch the URL.")

# Usage example
scan_for_xss("https://example.com")
