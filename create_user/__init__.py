import logging

import azure.functions as func
from users.user import User
from data.dataBase import data

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()

    id = req_body.get('id')
    name = req_body.get('name')
    email = req_body.get('email')
    age = req_body.get('age')
    city = req_body.get('city')

    user = User(id)
    user.add_user(name,email,age,city)
    user.create_user()


    return func.HttpResponse(f"The user with id: {id} was created.")
    

    



