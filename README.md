# UserRegistrationAndLoginApi

This is a REST API for user registration and login.
This API is created using Django Rest Framework.


The user registration part of this API is implemented by using Django Base User Model.
And The login/token based login part is implemented by using JWT Authentication with Django REST Framework.


The available URLs in The API:

admin/
auth/ register/ [name='register']
api/token/ [name='token_obtain_pair']
api/token/refresh/ [name='token_refresh']
message/ [name='message']



Use:

auth/ register/       --> To register a user
api/token/            --> To obtain a token
api/token/refresh/    --> To refresh a token
message/              --> To get a message from API



To Log in, use MobileNo and Password. e.g.

MobileNo: +911234567890
Password: password@123
