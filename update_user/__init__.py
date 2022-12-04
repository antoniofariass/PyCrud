import logging

import azure.functions as func
from users.user import User


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    req_body = req.get_json()

    id = req.route_params.get('id') 
    
    name = req_body.get('name')
    age = req_body.get('age')
    city = req_body.get('city')

    user = User(id)
    user.update_user(id,name,age,city)

    return func.HttpResponse(f"Hello, the id:{id} was updated.")
