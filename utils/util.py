import os
from datetime import datetime, timedelta
import jwt


SECRET_KEY = os.environ.get('SECRET_KEY') or 'key'

def encode_token(customer_id):
    payload = {
        'exp': datetime.now() + timedelta(hours=1),
        'iat': datetime.now(),
        'sub': customer_id
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
