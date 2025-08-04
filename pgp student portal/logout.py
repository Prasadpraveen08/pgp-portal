#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import http.cookies
print("Content-Type: text/html\r\n")


cookie = http.cookies.SimpleCookie()
cookie["user"] = ""
cookie["user"]["path"] = "/"
cookie["user"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"

print(cookie.output())
print("<script>alert('Logged out successfully'); window.location='login.py';</script>")
