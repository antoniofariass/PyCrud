import logging

import azure.functions as func
from users.user import User



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    type = req.route_params.get('type')
    id = req.route_params.get('id')
    
    if type == 'unique':
        user = User(id)
        return func.HttpResponse(f"Here the client in the database with this id:{user.read_unique_user(id)}")
    elif type == 'all':
        user = User(id)
        return func.HttpResponse(f"Here all the clients in the database:{user.read_all_users()}")
