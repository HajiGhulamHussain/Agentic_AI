import requests
from agents import function_tool

@function_tool
def fetch_user_data()->list:
    """
    fetch function for user data and return list
    """
    url="https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    return(res.json())


# single user get by id
@function_tool
def fetch_user_data_by_id(id:int)->list:
    """
    fetch function for user data and return list
    """
    url=f"https://jsonplaceholder.typicode.com/users/{id}"
    res = requests.get(url)
    return(res.json())

# print(fetch_user_data_by_id(3))

# @function_tool
# def fetch_user_data_by_id(id: int) -> dict:
#     """
#     Returns simplified user data to be compatible with the agent framework.
#     """
#     url = f"https://jsonplaceholder.typicode.com/users/{id}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         return {"error": "User not found"}

#     user = response.json()

    # return {
    #     "id": user.get("id"),
    #     "name": user.get("name"),
    #     "username": user.get("username"),
    #     "email": user.get("email"),
    #     "city": user.get("address", {}).get("city"),
    #     "company": user.get("company", {}).get("name"),
    #     "phone": user.get("phone"),
    #     "website": user.get("website")
    # }