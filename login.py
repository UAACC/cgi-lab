#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import templates
import secret
import cgi
import cgitb
import os
from http import cookies
cgitb.enable()


# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
username = form.getfirst('username')
password  = form.getfirst('password')

form_ok = username == secret.username and password == secret.password




cook = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if cook.get("username"):
    c_username = cook.get("username").value
if cook.get("password"):
    c_password = cook.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password

print("Conten-Type: text/html")



if form_ok:            #id/index = value e.g cook[username] = 123
    print(f"Set-Cookie: username = {username}")
    print(f"Set-Cookie: password = {password}")

print()

if not username and not password:
    print(templates.login_page())
    #print(cook["username"])
elif username == secret.username and password == secret.password:
    
    print(templates.secret_page(username, password))
else:
    
    
    print(templates.after_login_incorrect())  


