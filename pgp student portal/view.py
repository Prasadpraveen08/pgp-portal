#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import cgi, cgitb, pymysql, http.cookies, os
cgitb.enable()

print("Content-type: text/html\r\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
user_cookie = cookie.get("user")

if not user_cookie:
    print("<script>alert('Please login first'); window.location='login.py';</script>")
    exit()

user_email = user_cookie.value  

conn = pymysql.connect(host="localhost", user="root", password="", database="test")
cur = conn.cursor()


cur.execute("SELECT id, name, phone, email, profile FROM users WHERE email=%s", (user_email,))
row = cur.fetchone()
conn.close()

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="icon" type="image/png" href="static/images/pgp.png">
    <style>
        .sidebar {{
            min-height: 100vh;
            background-color: #343a40;
        }}
        .sidebar a {{
            color: white;
            display: block;
            padding: 10px 15px;
            text-decoration: none;
        }}
        .sidebar a:hover {{
            background-color: #495057;
        }}
    </style>
</head>
<body class="m-0 p-0">
<div class="container-fluid m-0 p-0">
  <div class="row g-0">

    <!-- Sidebar -->
     <div class="col-md-3 col-lg-2 sidebar d-flex flex-column justify-content-between p-3">
  <div>
    <a class="navbar-brand d-flex align-items-center mb-3" href="home.py">
      <img src="static/images/pgp.png" alt="PGP Logo" height="30" class="me-2">
      <h4 class="text-white mb-0">PGP Portal</h4>
    </a>
    <a href="view.py">My Profile</a>
      <a href="logout.py" class="text-danger">Logout</a>
  </div>

  
 <div class="text-white small">
    <hr class="border-light">
    <p class="mb-1">&#9993; pgp@example.com</p>
    <p class="mb-0">&#9742; +91 98765 43210</p>
    <p class="mt-2 mb-0">&copy 2025 PGP</p>
  </div>
</div>
    <!-- Main Content -->
    <div class="col-md-9 col-lg-10 p-4">
      <h3 class="mb-4">Welcome, {row[1]}</h3>
""")

if row:
    profile_img = f"<img src='uploads/{row[4]}' width='80' class='rounded'>" if row[4] else "No Image"
    print(f"""
      <table class='table table-bordered w-50'>
          
          <tr><th>Name</th><td>{row[1]}</td></tr>
          <tr><th>Phone</th><td>{row[2]}</td></tr>
          <tr><th>Email</th><td>{row[3]}</td></tr>
          <tr><th>Profile</th><td>{profile_img}</td></tr>
      </table>
     <a href='edit_profile.py' class='btn btn-warning mt-3'>Edit My Profile</a>

    """)
else:
    print("<p class='text-danger'>User data not found.</p>")

# Close HTML
print("""
    </div>
  </div>
</div>
</body>
</html>
""")
