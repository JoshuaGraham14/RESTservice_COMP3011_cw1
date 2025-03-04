import requests
from tabulate import tabulate

BASE_URL = "http://127.0.0.1:8000/api"

session = requests.Session()

def register():
    username = input("Enter username: ")
    email =input("Enter email: ")
    password=input("Enter password: ")

    #Call REST endpoint
    url=f"{BASE_URL}/register/" 
    data ={"username": username, "email": email, "password":password} 

    response = requests.post(url, json=data) # POST request to the server
    if response.status_code==201:
        print("✅ Registration successful!")
    else:
        print("❌ Registration failed:",response.json())

def login():
    username=input("Enter username: ")
    password =input("Enter password: ") 
   
    #Call REST endpoint
    url=f"{BASE_URL}/login/" 
    data = {"username": username, "password":password} 

    response = session.post(url, json=data) 
    
    if response.status_code==200: 
        token = response.json().get("token")   
        print(f"✅ Login successful!") 
        session.headers.update({'Authorization': f"Token {token}"})
    else:
        print("❌ Login failed:", response.json())  
   
def logout(): 
    #Call REST endpoint
    url=f"{BASE_URL}/logout/"
    response = session.post(url)

    if response.status_code==200:
        print("✅ Logged out successflly")
        session.headers.pop("Authorization", None)
    else:
        print("❌ Logout failed:", response.json())

def list_modules():
    #Call REST endpoint
    url=f"{BASE_URL}/modules/" 
    #Even though authentication not required, still use sessions as more efficient...
    response = session.get(url) 

    if response.status_code==200:
        modules =response.json() 
        if not modules: 
            print("No module instances found.")
        else:
            table_data = []
            for module in modules:
                module_code = module["module"]["module_code"] 
                module_name =module["module"]["name"] 
                year=module["year"] 
                semester=module["semester"]
                professors= ", ".join(module["professors"])
                table_data.append([module_code,module_name,year, semester,professors])
 
            headers = ["Module Code", "Name","Year","Semester","Taught by (Name & ID)"] 

            print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("❌ Failed to retrieve module instances.") 
          
def view_professor_ratings():
    #Call REST endpoint
    url=f"{BASE_URL}/professors/ratings/"
    response =session.get(url)
    
    if response.status_code==200: 
        professors = response.json() 
        if not professors:
            print("No professor ratings available") 
        else:
            table_data = []
            for professor in professors:
                professor_id = professor["professor_id"]
                name =professor["name"]  
                rating=professor["average_rating"]   

                table_data.append([f"{name} ({professor_id})", rating])

            headers= ["Professor", "Average rating"] 
            print(tabulate(table_data, headers=headers,tablefmt="grid")) 
    else: 
        print("❌ Failed to retrieve professor ratings")

def average_professor_rating():
    professor_id =input("Enter professor ID: ")
    module_code =input("Enter module code: ")

    if not professor_id or not module_code:
        print("❌ Both Professor ID and Module Code are required.")
        return
    
    #Call REST endpoint
    url=f"{BASE_URL}/professors/{professor_id}/module/{module_code}/rating/"
    response = session.get(url)

    if response.status_code==200:
        data=response.json() 
        print(f"\n📌 The rating of {data['professor']} in {data['module']} is: {data['average_rating']} ⭐\n")
    elif response.status_code == 404:
        print(f"❌ {response.json()['error']}")
    else:
        print("❌ Failed to retrieve professor rating")


def rate_professor(): 
    if "Authorization" not in session.headers:
        print("❌ You must be logged in to rate a professor. Please log in first.")
        return  

    professor_id = input("Enter professor ID: ").strip()
    module_code = input("Enter module code: ").strip()
    year = input("Enter year: ").strip()
    semester = input("Enter semester: ").strip()
    rating =input("Enter rating (1-5): ").strip() 

    #Quick validate of user inputs
    if (not professor_id) or (not module_code) or (not year) or (not semester):
        print("❌ All fields are required")
        return
    if not rating.isdigit() or not (1<=int(rating)<=5):
        print("❌ Rating must be a number between 1 and 5") 
        return   

    #Call REST endpoint
    url=f"{BASE_URL}/professors/{professor_id}/module/{module_code}/{year}/{semester}/rate/"
    data ={"rating": int(rating)}

    response =session.post(url, json=data)

    if response.status_code==200 or response.status_code==201:
        print(f"✅ Successfully rated Professor {professor_id} in {module_code} ({year} Semester {semester}) with {rating} ⭐")
    elif response.status_code== 400 or response.status_code==404:
        print(f"❌ {response.json()['error']}")
    else:
        print("❌ Failed to submit rating")
         
#----------------------------------

def main(): 
    print("--- Welcome to the Professor Rating App ---")
    print("Type 'exit' to quit")
 
    while True:
        command = input("> ").strip().lower()
 
        if command == "register":
            register() 
        elif command == "login":
            login()
        elif command == "logout":
            logout()
        elif command == "list":
            list_modules() 
        elif command == "view":
            view_professor_ratings()
        elif command == "average": 
            average_professor_rating()
        elif command == "rate":
            rate_professor() 
        elif command == "exit":
            print("Exiting the application... Bye!")
            break 
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main() 
