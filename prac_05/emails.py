"""
Emails
Estimate: 30 minutes
Actual:  28 minutes
"""

def extract_name_from_email(email):
    # Get the part before '@' in the email
    username = email.split('@')[0]