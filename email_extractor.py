import re

# Open and read the input file
with open("input.txt", "r") as file:
    content = file.read()

# Find all email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Save emails to another file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")