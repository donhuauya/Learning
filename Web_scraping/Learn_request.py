"""
In this tutorial, I'will learn how to:

    - Make requests :: using the most common HTTP methods
    - Customize ::  your requests' headers and using the query string and message body 
    - Inspect :: data from your request and responses
    - Make authenticated request
    - Configure :: your requests to help prevent your application from backing up or slowing down

    Msg Note:
    
        - Informational responses   (100 - 199)
        - Successful responses      (200 - 299)
            - 204 No Content
            - 304 No Modified
        - Redirection messages      (300 - 399)
        - Client error responses    (400 - 499)
        - Server error responses    (500 - 599)
"""
#----------------------------------------------------------------------------------------------------#

import requests

urls = ["https://api.github.com/", "https://api.github.com/invalid","thisurlnotfound", "https://www.dia.es/"]


#------------------------------Check if the route works----------------------------------------------#
"""
        - Description: Your can see the status code.
            - Option 1: 
                - If retourned 200, which means that your request was successful. 
                - If retoruned 404, which means that your request was not found.
            - Option 2: 
                - If response is true, it means that is between the values: 200 - 399
                - If it's not, then you raise an exception that includes the non.success status code in an f-string
            - Option 3:
                - Using the Requests Built-in capacities to raise an exception: from requests.exceptions import HTTPError
                    - 1. Try if the status code is success.
                    - 2. If error ocurred a error HTTP, the exception used is: HTTPError
                    - 3. If another type error ocurred, the exception used is: Exception

"""
#--------------#
#-- Option 1 --#
#--------------#
# response = requests.get(urls[0])
# print(response.status_code)
# if response.status_code == 200:
#     print("Success!")
# if response.status_code == 404:
#     print("Not found")

#--------------#
#-- Option 2 --#
#--------------#
# response = requests.get(urls[0])
# if response:
#     print("Success!")
# else:
#     raise Exception(f"Non-success status code: {response.status_code}")

#--------------#
#-- Option 3 --#
#--------------#
# from requests.exceptions import HTTPError
# for url in urls:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f"HTTP error ocurred: {http_err}")
#     except Exception as err:
#         print(f"Other error ocurred: {err}")
#     else:
#         print("Success!")

#----------------------------------------------------------------------------------------------------#

#--------------------------------------------Content-------------------------------------------------#
"""
    - .content :: gives you access to the raw bytes of the response payload
    - .text :: to convert them into a struing using character encoding such as UTF-8.response (Doesn't specify an encoding scheme)
        - .encoding = "UTF-8" :: so the request doesn't try to guess the encoding based on the response header
    - .json :: to convert a json content serialized.

    To convert of bit to string : response.text
    To convert of string to json : response.json.loades() //->// Search more about this, but it's not essential.
"""
# response = requests.get(urls[0])
# print("----------------bit------------------")
# print(response.content)
# print(type(response.content))# class bit
# print("----------------text------------------")
# print(response.text)
# print(type(response.text)) # class str (no encoding scheme)
# print("----------------encoding------------------")
# response.encoding = "utf-8"
# print(response.text)
# print(type(response.text)) # class str (width encoding scheme)
# print("----------------JSON------------------")
# print(response.json())
# print(type(response.json())) # class dict
# response_dict = response.json()
# print(response_dict["emojis_url"]) # Acces of json() dictionary by key.

#----------------------------------------------------------------------------------------------------#

#--------------------------------------------Headers-------------------------------------------------#
"""
    - They key value is a case-insensitive :: Content-Type -> content-type
"""

# response = requests.get(urls[3])
# print(response.headers)
# print(f"Using key value: {response.headers["Content-Type"]}")

#----------------------------------------------------------------------------------------------------#

#--------------------------------------------Query String Parameters-------------------------------------------------#
"""
    To pass values thought query string parameters in the URL
"""
#--------------------------------------------------------------#
#-- Search Github's repositories for popular Python projects --#
#--------------------------------------------------------------#
# In the form of a dictionary
# response = requests.get(
#     "https://api.github.com/search/repositories",
#     params={"q": "language:python", "sort": "stars", "order": "desc"},
# )

# In the form a list of tuples
# response = requests.get(
#     "https://api.github.com/search/repositories",
#     [("q", "language:python"),("sort", "stars"),("order", "desc")],
# )

# Pass values as bytes
# response = requests.get(
#     "https://api.github.com/search/repositories",
#     params=b"q=language:python&sort=stars&order=desc",
# )

# Inspect some attributes of the first three repositories
# json_response = response.json()
# popular_repositories = json_response["items"]
# for repo in popular_repositories:
#     print(f"Name: {repo['name']}")
#     print(f"Description: {repo['description']}")
#     print(f"Stars: {repo['stargazers_count']}")
#     print()


#continue
# https://realpython.com/python-requests/#query-string-parameters

