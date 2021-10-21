from functools import wraps
from api import MapXaccessToken, UserSession
from flask import request, jsonify
import jwt
from config.configs import Config


def authenicate_required():
    def _authenicate(f):
        @wraps(f)
        def __authenicate(*args, **kwargs):
            jwtToken = request.headers.get("x-access-token")
            if jwtToken is None:
                return (
                    jsonify({"success": False, "message": "Missing token on request."}),
                    400,
                )
                
            elif jwtToken in MapXaccessToken:
                # SessionId = MapXaccessToken[jwtToken]
                # userSession = UserSession[SessionId]
                # username = userSession['user']['_name']
                pass

            else:
                return jsonify({"success": True, "message": "Incorrect token."}), 400

            return f(*args, **kwargs)

        return __authenicate

    return _authenicate

