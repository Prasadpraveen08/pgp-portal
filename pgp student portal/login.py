#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import cgi, cgitb, pymysql, http.cookies, os
cgitb.enable()

form = cgi.FieldStorage()
email = form.getvalue("email")
password = form.getvalue("password")
submit = form.getvalue("submit")

if submit:
    conn = pymysql.connect(host="localhost", user="root", password="", database="test")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    result = cur.fetchone()
    conn.close()

    if result:
        cookie = http.cookies.SimpleCookie()
        cookie["user"] = email
        cookie["user"]["path"] = "/"

        print("Content-type: text/html")
        print(cookie.output())
        print()
        print("<script>window.location='view.py';</script>")
        exit()
    else:
        print("Content-type: text/html\r\n\r\n")
        print("<script>alert('Invalid email or password'); window.location='login.py';</script>")
        exit()

print("Content-type: text/html\r\n\r\n")

print("""
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="static/images/pgp.png">
    <style>
        .sidebar {
            min-height: 100vh;
            background-color: #343a40;
        }
        .sidebar a {
            color: white;
            display: block;
            padding: 10px 15px;
            text-decoration: none;
        }
        .sidebar a:hover {
            background-color: #495057;
        }
    </style>
</head>
<body class="bg-light m-0 p-0">
  <div class="container-fluid m-0 p-0">
    <div class="row g-0">
      
     
       <div class="col-md-3 col-lg-2 sidebar d-flex flex-column justify-content-between p-3">
  <div>
    <a class="navbar-brand d-flex align-items-center mb-3" href="home.py">
      <img src="static/images/pgp.png" alt="PGP Logo" height="30" class="me-2">
      <h4 class="text-white mb-0">PGP Portal</h4>
    </a>
    <a href="home.py">Home</a>
    <a href="register.py">Register</a>
    <a href="login.py">Login</a>
  </div>

  
 <div class="text-white small">
    <hr class="border-light">
    <p class="mb-1">&#9993; pgp@example.com</p>
    <p class="mb-0">&#9742; +91 98765 43210</p>
    <p class="mt-2 mb-0">&copy 2025 PGP</p>
  </div>
</div>

      <!-- Main Content -->
      <div class="col-md-9 col-lg-10 d-flex flex-column justify-content-between p-0">
        <div class="p-4">
          <div class="container shadow bg-white rounded p-4 mt-5" style="max-width:500px;">
              <h3 class="mb-4">User Login</h3>
              <form method="post" action="login.py">
                  <div class="mb-3">
                      <label>Email:</label>
                      <input type="email" name="email" class="form-control" required>
                  </div>
                  <div class="mb-3">
                      <label>Password:</label>
                      <input type="password" name="password" class="form-control" required>
                  </div>
                  <input type="submit" name="submit" value="Login" class="btn btn-primary">
              </form>
          </div>
        </div>

        
      </div>

    </div>
  </div>
</body>
</html>
""")
