


import re

# Define a list of keywords that indicate a failed password attempt
failed_keywords = [r"failed", r"invalid", r"incorrect"]

failed_password = 0  # Counter for failed password attempts
failed_attempts = []  # List to store the actual lines of failed attempts

# Open the file and read its content
with open(r"C:\Users\john_\Desktop\Project LogHawk\auth.log", "r") as file:
    content = file.read()
    
    # Split content into lines
    lines = content.splitlines()
    
    # Iterate through each line and look for failed login attempts
    for line in lines:
        # Check if any of the failed password keywords are in the line
        if any(re.search(keyword, line, re.IGNORECASE) for keyword in failed_keywords):
            failed_password += 1
            failed_attempts.append(line)  # Store the line with the failed attempt

# Output the total number of failed password attempts
print(f"Total number of failed password attempts: {failed_password}")

# Print the actual failed password attempts
print("\nList of Failed Password Attempts:")
for attempt in failed_attempts:
    print(attempt)
    print("🚫 ALERT: FAILED PASSWORD ATTEMPT ")  # Alert after each failed attempt
print()

print("LIST OF HTTP ALERTS")
# Regex pattern to find status codes in the 400's (i.e., 400-499)
status_400s_pattern = re.compile(r'\s(4\d{2})\s')  # Looks for 3-digit numbers starting with 4

# Open the file and read its content
with open(r"C:\Users\john_\Desktop\Project LogHawk\access.log", "r") as file:
    content = file.read()
    
    # Split content into lines
    lines = content.splitlines()
    
    # Iterate through each line and check for status codes in the 400's
    for line in lines:
        if status_400s_pattern.search(line):  # Check if the line contains a 400-series status code
            print(line)  # Print the line containing the status code in the 400's 

# Alert if status code is in 400's
        if status_400s_pattern.search(line):
            print("🚫 ALERT: HTTP ALERT")
print()



print("LIST OF WARNINGS")
# Define a list of keywords that indicate these keywords
failed_keywords = [r"error", r"warning", r"critical"]

# List to store failed lines
failed_attempts = []

# Open the file and read its content
with open(r"C:\Users\john_\Desktop\Project LogHawk\app.log", "r") as file:
    content = file.read()
    
    # Split content into lines
    lines = content.splitlines()
    
    # Iterate through each line and look for these keywords
    for line in lines:
        if any(re.search(keyword, line, re.IGNORECASE) for keyword in failed_keywords):
            failed_attempts.append(line)
            print(line)
            print("🚫 ALERT: KEYWORDS ALERT")  # Alert after each keyword
print()


print("LIST OF IOC's")
# Define a list of keywords that indicate these keywords
failed_keywords = [r"block", r"suspicious behavior", r"memory", r"High cpu", r"DDos"]

# List to store failed lines
failed_attempts = []

# Open the file and read its content
with open(r"C:\Users\john_\Desktop\Project LogHawk\system.log", "r") as file:
    content = file.read()
    
    # Split content into lines
    lines = content.splitlines()
    
    # Iterate through each line and look for these keywords
    for line in lines:
        if any(re.search(keyword, line, re.IGNORECASE) for keyword in failed_keywords):
            failed_attempts.append(line)
            print(line)
            print("🚫 ALERT: SUSPICIOUS ACTIVITY ALERT")  # Alert after each keyword










