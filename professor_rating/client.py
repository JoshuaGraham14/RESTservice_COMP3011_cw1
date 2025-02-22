import requests
import os
import sys
from tabulate import tabulate

BASE_URL = "http://127.0.0.1:8000/api"

TOKEN_FILE = "token.txt"

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

    url = f"{BASE_URL}/register/" 
    data = {"username": username, "email": email, "password":password} 

    response = requests.post(url, json=data) # POST request to the server
    if response.status_code == 201:
        print("✅ Registration successful!")
    else:
        print("❌ Registration failed:", response.json())

def login():
    username = input("Enter username: ")
    password = input("Enter password: ") 
   
    url = f"{BASE_URL}/login/" 
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

    url = f"{BASE_URL}/logout/"
    headers= {"Authorization": f"Token {token}"}
    
    response= requests.post(url,headers=headers) 

    if response.status_code == 200: 
        print("✅ Logged out successfully.")
        os.remove(TOKEN_FILE)  #Delete token file on logout
    else:
        print("❌ Logout failed:", response.json()) 

def list_modules():
    url = f"{BASE_URL}/modules/" 
    response = requests.get(url) 

    if response.status_code == 200:
        modules = response.json() 
        if not modules: 
            print("No module instances found.")
        else:
            table_data = []
            for module in modules:
                module_code = module["module"]["id"] 
                module_name =module["module"]["name"] 
                year=module["year"] 
                semester=module["semester"]
                professors= ", ".join(module["professors"])
                table_data.append([module_code,module_name,year, semester,professors])
 
            headers = ["Code", "Name","Year","Semester","Taught by"] 

            print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("❌ Failed to retrieve module instances.") 
          
     
#----------------------------------

def main():
    if len(sys.argv) < 2:
        print("❌ No command provided. Available commands: register, login <url>, logout, list, view, average, rate")
        return

    command = sys.argv[1].lower()    

    if command == "register":
        register() 
    elif command == "login":
        login() 
    elif command == "logout":
        logout()
    elif command == "list": 
        list_modules()
    else: 
        print("❌ Unknown command. Available commands: register, login <url>, logout, list, view, average, rate")
   
if __name__ == "__main__":
    main()

