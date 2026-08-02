import jwt
from fastapi import Request, HTTPException,Depends

SECRET_KEY = "abcdefghijklmnopqrstuvwxyz"
ALGORITHM = "HS256"


def get_current_user(request: Request):
  token = request.cookies.get("access_token")

  if not token:
    raise HTTPException(status_code=401, detail="Token missing")

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")
  except jwt.InvalidTokenError:
    raise HTTPException(status_code=401, detail="Invalid token")


def verify_admin(current_user: dict = Depends(get_current_user)):
    print(current_user)   # temporary debug
    if current_user.get("is_admin") is not True:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

def verify_admin(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        if not payload.get("is_admin"):
            raise HTTPException(
                status_code=403,
                detail="Admin access required"
            )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )