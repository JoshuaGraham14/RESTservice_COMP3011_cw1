import requests
import os

BASE_URL = "http://127.0.0.1:8000/api/"  # Change this to your actual API URL when deployed

TOKEN_FILE = "token.txt"  # Used to store the authentication token

def save_token(token):
    with open(TOKEN_FILE, "w") as file:
        file.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE): #get token from token_file
        with open(TOKEN_FILE, "r") as file:
            return file.read().strip() 
    return None

def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    url = f"{BASE_URL}register/" 
    data = {"username": username, "email": email, "password":password} 

    response = requests.post(url, json=data) # POST request to the server
    if response.status_code == 201:
        print("✅ Registration successful!")
    else:
        print("❌ Registration failed:", response.json())

def login():
    username = input("Enter username: ")
    password = input("Enter password: ") 
   
    url = f"{BASE_URL}login/" 
    data = {"username": username, "password":password} 

    response = requests.post(url, json=data) 

    if response.status_code == 200:
        token = response.json().get("token")   
        print(f"✅ Login successful! Token: {token}") 
        save_token(token)
    else:
        print("❌ Login failed:", response.json()) 

def logout(): 
    token = load_token()
    if not token: 
        print("❌ No active session found. Please log in first.")
        return

    url = f"{BASE_URL}logout/"
    headers= {"Authorization": f"Token {token}"}
    
    response= requests.post(url,headers=headers) 

    if response.status_code == 200: 
        print("✅ Logged out successfully.")
        os.remove(TOKEN_FILE)  #Delete token file on logout
    else:
        print("❌ Logout failed:", response.json()) 

    
#----------------------------------

def main():
    print("--- Professor Rating Client Application ---")
    while True:
        print("\nOptions:")
        print("1= Register")
        print("2= Login")
        print("3= Logout")
        print("Any key= Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        else:
            print("Bye!")
            break

if __name__ == "__main__":
    main()
