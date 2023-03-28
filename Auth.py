from jose import jwt
from jose import ExpiredSignatureError
from jwt import InvalidTokenError
from datetime import timedelta
from datetime import datetime
from fastapi import HTTPException
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from passlib.context import CryptContext


import settings


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = settings.Secret

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_email):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1, minutes=50),
            'iat': datetime.utcnow(),
            'sub': user_email
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail='Not enough segments')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)