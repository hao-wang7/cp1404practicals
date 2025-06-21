"""
Emails
Estimate: 30 minutes
Actual:  28 minutes
"""

def extract_name_from_email(email):
    # Get the part before '@' in the email
    username = email.split('@')[0]
    # Split the username by '.' to separate name parts
    parts = username.split('.')
    # Capitalize the first letter of each part and join them with spaces
    name = ' '.join(part.title() for part in parts)
    return name

def main():
    email_to_name = {}  # Dictionary to store emails as keys and names as values
# Prompt the user for the first email
    email = input("Email: ").strip()