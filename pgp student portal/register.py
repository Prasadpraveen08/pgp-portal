#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import cgi, cgitb, pymysql, os
cgitb.enable()

print("Content-type: text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
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

<div class="container-fluid">
  <div class="row">
   
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

    
    <div class="col-md-9 col-lg-10">
      <div class="container mt-5 p-4 shadow bg-white rounded mb-5" style="max-width:600px;">
          <h3 class="mb-4">User Registration Form</h3>
          <form method="post" enctype="multipart/form-data">
              <div class="mb-3">
                  <label class="form-label">Name:</label>
                  <input type="text" name="name" class="form-control" required>
              </div>
              <div class="mb-3">
                  <label class="form-label">Phone:</label>
                  <input type="text" name="phone" class="form-control" required>
              </div>
              <div class="mb-3">
                  <label class="form-label">Email:</label>
                  <input type="email" name="email" class="form-control" required>
              </div>
              <div class="mb-3">
                  <label class="form-label">Password:</label>
                  <input type="password" name="password" class="form-control" required>
              </div>
              <div class="mb-3">
                  <label class="form-label">Upload Profile Photo:</label>
                  <input type="file" name="profile" class="form-control" required>
              </div>
              <input type="submit" name="submit" value="Register" class="btn btn-primary">
              <input type="reset" value="Reset" class="btn btn-secondary">
          </form>
      </div>

    </div>
  </div>
</div>
</body>
</html>
""")

conn = pymysql.connect(host="localhost", user="root", password="", database="test")
cur = conn.cursor()
x = cgi.FieldStorage()
sub = x.getvalue("submit")

if sub != None:
    name = x.getvalue("name")
    phone = x.getvalue("phone")
    email = x.getvalue("email")
    password = x.getvalue("password")

    profile_file = x["profile"]
    profile_name = ""

    if profile_file.filename:
        profile_name = os.path.basename(profile_file.filename)
        upload_path = os.path.join("uploads", profile_name)
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        with open(upload_path, "wb") as f:
            f.write(profile_file.file.read())

    query = """INSERT INTO users(name, phone, email, password, profile) 
               VALUES (%s, %s, %s, %s, %s)"""
    cur.execute(query, (name, phone, email, password, profile_name))
    conn.commit()
    print("""<script>alert("Registration Successful!");</script>""")

conn.close()
