from tabnanny import check
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests
import json

hotel_url = "https://hotels4.p.rapidapi.com"
hotel_headers = {
    'X-RapidAPI-Key': 'bb81d64da8msh55686902a97b128p14da0fjsne27d6f91ee56',
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
  }

# Swagger UI Configuration
swagger_ui_params = {
    "docExpansion": "none",
    "layout": "BaseLayout",
    "filter": False
   }

# Swagger API Information
swagger_ui_info = {
  "title": "Weather API for Learning",
  "description": "Teaching Ben to build and API that connect to another API.",
  "termsOfService": "http://swagger.io/terms/",
  "contact": {
        "name": "",
        "email": ""
        },
  "license": {
    "name": "Apache 2.0",
    "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
  },
  "version": "0.0.1 Beta"
}


# API Object
wapi = FastAPI(
    title=swagger_ui_info['title'],
    description=swagger_ui_info['description'],
    termsOfService=swagger_ui_info['termsOfService'],
    # contact=swagger_ui_info['contact'],
    license=swagger_ui_info['license'],
    version=swagger_ui_info['version'],
    swagger_ui_parameters=swagger_ui_params,
)


# Redirect from away root url
@wapi.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')





@wapi.get("/username", tags=["Ben"])
async def get_username():
  return {"user":"Ben Hart"}

@wapi.get("/timestwo", tags=["Ben"])
async def times_two(num: int):
  return {"result": num*2}

@wapi.get("/addtwonumbers", tags=["Ben"])
async def add_two(num1: int, num2: int) -> object:
  return {"result": num1 + num2}

@wapi.get("/findpassword", tags=["Ben"])
async def find_password(name: str):
  users = {"Ben": "bens password", "nicole": "bitchface"}
  try:
    return users[name]
  except:
    return {"Error": "User Not Found"}


@wapi.get("/get_location", tags=["Hotels"])
async def get_location(city:str) -> object:
  
  endpoint = "/locations/v2/search"
  
  querystring = {"query": city, "locale": "en_GB", "currency": "GBP"}
  
  response = requests.request("GET", f'{hotel_url}{endpoint}', headers=hotel_headers, params=querystring)
  
  return response.json()


@wapi.get("/get_meta_data", tags=["Hotels"])
async def get_meta_data(start_date:str, end_date:str) -> object:

  endpoint = "/get-meta-data"

  response = requests.request("GET", f'{hotel_url}{endpoint}', headers=hotel_headers)

  uf_list = response.json()

  f_list = {}
  idx = 0

  for i in uf_list:
    f_list[idx] = i['name']
    idx += 1

  return f_list

@wapi.get("/get_properties", tags=["Hotels"])
async def get_properties(locationid: int, checkin: str, checkout:str) -> object:
  
  endpoint = "/properties/list"
  
  querystring = {"destinationId":locationid,"pageNumber":"1","pageSize":"25","checkIn":checkin,"checkOut":checkout,"adults1":"1","sortOrder":"PRICE","locale":"en_GB","currency":"GBP"}
  
  response = requests.request("GET", f'{hotel_url}{endpoint}', headers=hotel_headers, params=querystring)
  
  return response.json()

@wapi.get("/get_details", tags=["Hotels"])
async def get_details(ID: int) -> object:
  
  endpoint = "/properties/get-details"
  
  querystring = {"id": ID, "locale":"en_GB", "currency": "GBP"}
  
  response = requests.request("GET", f'{hotel_url}{endpoint}', headers=hotel_headers, params=querystring)
  
  return response.json()

@wapi.get("/get_photo", tags=["Hotels"])
async def get_photo(ID: int) -> object:
  
  endpoint = "/properties/get-hotel-photos"
  
  querystring = {"id": ID, "locale":"en_GB", "currency": "GBP"}
  
  response = requests.request("GET", f'{hotel_url}{endpoint}', headers=hotel_headers, params=querystring)
  
  return response.json()