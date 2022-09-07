from fastapi import FastAPI
from fastapi.responses import RedirectResponse


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
