#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import cgi, cgitb, pymysql, http.cookies, os
cgitb.enable()

print("Content-type: text/html\r\n\r\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
user_cookie = cookie.get("user")

if not user_cookie:
    print("<script>alert('Please login first'); window.location='login.py';</script>")
    exit()

user_email = user_cookie.value

conn = pymysql.connect(host="localhost", user="root", password="", database="test")
cur = conn.cursor()

form = cgi.FieldStorage()
if form.getvalue("submit"):
    name = form.getvalue("name")
    phone = form.getvalue("phone")
    password = form.getvalue("password")

    cur.execute("UPDATE users SET name=%s, phone=%s, password=%s WHERE email=%s",
                (name, phone, password, user_email))
    conn.commit()
    conn.close()
    print("<script>alert('Profile updated successfully'); window.location='view.py';</script>")
    exit()

cur.execute("SELECT name, phone, email, password FROM users WHERE email=%s", (user_email,))
data = cur.fetchone()
conn.close()

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Edit Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="static/images/pgp.png">
</head>
<body class="bg-light">
<div class="container mt-5 p-4 shadow bg-white rounded" style="max-width:600px;">
  <h3 class="mb-4">Edit My Profile</h3>
  <form method="post" action="edit_profile.py">
    <div class="mb-3">
        <label class="form-label">Name:</label>
        <input type="text" name="name" value="{data[0]}" class="form-control" required>
    </div>
    <div class="mb-3">
        <label class="form-label">Phone:</label>
        <input type="text" name="phone" value="{data[1]}" class="form-control" required>
    </div>
    <div class="mb-3">
        <label class="form-label">Email (readonly):</label>
        <input type="email" value="{data[2]}" class="form-control" readonly>
    </div>
    <div class="mb-3">
        <label class="form-label">Password:</label>
        <input type="password" name="password" value="{data[3]}" class="form-control" required>
    </div>
    <input type="submit" name="submit" value="Update Profile" class="btn btn-success">
    <a href="view.py" class="btn btn-secondary">Cancel</a>
  </form>
</div>
</body>
</html>
""")
