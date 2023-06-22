import requests
import re


def find_xss(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    if response.status_code == 200:
        # Extract all the HTML content from the response
        html_content = response.text

        # Find potential XSS vulnerabilities using regular expressions
        xss_patterns = [
            r"<script[^>]>[^<]</script>",
            r"on\w+=\"[^\"]*\"",
            r"on\w+='[^']*'",
            r"javascript:",
            r"alert\([^)]*\)",
            r"<img[^>]src\s=\s*[\'|\"](?P<src>[^\'|\"])[\'|\"][^>]>",
        ]

        for pattern in xss_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                print(f"Potential XSS found: {matches}")

        print("XSS detection completed.")
    else:
        print(f"Error: {response.status_code}")


# Example usage
url = "https://www.zoom.com"
find_xss(url)