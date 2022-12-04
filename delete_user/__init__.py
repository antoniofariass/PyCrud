import logging

import azure.functions as func
from users.user import User


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    id = req.route_params.get('id')

    user = User(id)
    user.delete_user(id)

    return func.HttpResponse(f"Deletion of {id} successfully.")