import functools


# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function

@make_secure
def get_admin_password():
    return "1234"
   
# get_admin_password = make_secure(get_admin_password)
user = {"username": "moses", "access_level": "guest"}

print(get_admin_password())