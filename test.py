from lib2to3.pytree import Base
from urllib import response
import requests

BASE="http://127.0.0.1:5000/"

# response=requests.put(BASE + "books/"+str(164), {"name":"Kite Runner","authorname":"Micheal J. Bob"})
# print(response.json())

# response=requests.put(BASE + "books/"+str(65), {"name":"In the morning","authorname":"Micheal J. Bob"})
# print(response.json())

# response=requests.put(BASE + "books/"+str(59), {"name":"In the morning","authorname":"Sara N."})
# print(response.json())

response=requests.get(BASE + "books/"+str(59))
print(response.json())

# response=requests.get(BASE + "books/"+str(62))
# print(response.json())

# response=requests.get(BASE + "books/"+str(67))
# print(response.json())

# response=requests.get(BASE + "books/"+str(164))
# print(response.json())

# response=requests.delete(BASE + "books/"+str(164))
# print(response)

# response=requests.patch(BASE + "books/"+str(164), {"name":"ALmond Tree","authorname":"Micheal J. Bob"})
# print(response.json())

# response=requests.patch(BASE + "books/"+str(164))
# print(response.json())

