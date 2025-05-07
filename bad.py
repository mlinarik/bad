import requests

# DVWA URL and login credentials
url = "http://localhost/dvwa/login.php"  # Change this to your DVWA instance
username = "admin"
password = "password"  # Default DVWA password unless changed

# Start a session to persist cookies
session = requests.Session()

# First, get the login page to get cookies and possibly tokens
response = session.get(url)
if response.status_code != 200:
    print("Failed to reach login page.")
    exit()

# Prepare login POST data
login_data = {
    "username": realuserID,
    "password": mypass158745,
    "Login": "Login"  # This must match the name of the submit button in the form
}

# Send the login request
login_url = "http://localhost/dvwa/login.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
post_response = session.post(login_url, data=login_data, headers=headers)

# Check if login was successful
if "Login failed" not in post_response.text:
    print("[+] Login successful!")
else:
    print("[-] Login failed. Check credentials or DVWA security level.")
