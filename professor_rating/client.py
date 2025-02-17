import requests

def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    url = "http://127.0.0.1:8000/api/register/" 
    data = {"username": username, "email": email, "password":password} 

    response = requests.post(url, json=data) # POST request to the server
    if response.status_code == 201:
        print("✅ Registration successful!")
    else:
        print("❌ Registration failed:", response.json())

if __name__ == "__main__":
    register()
