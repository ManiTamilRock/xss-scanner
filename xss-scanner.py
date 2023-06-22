import re

def detect_xss(input_string):
    # Define the patterns to check for potential XSS attacks
    patterns = [
        r'<script.*?>.*?</script.*?>',
        r'<.*?on\w+.*?>.*?</.*?>'
        r"on\w+=\"[^\"]*\"",
            r"on\w+='[^']*'",
            r"javascript:",
            r"alert\([^)]*\)",
            r"<img[^>]*src\s*=\s*[\'|\"](?P<src>[^\'|\"]*)[\'|\"][^>]*>",
    ]

    # Check if any of the patterns match the input string
    for pattern in patterns:
        match = re.search(pattern, input_string, re.IGNORECASE)
        if match:
            return True
    
    return False

# Example usage:
input_string = input("Enter a string to check for XSS attacks: ")
if detect_xss(input_string):
    print("Potential XSS attack detected!")
else:
    print("No XSS attack detected.")
