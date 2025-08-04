#!C:/Users/prasad praveen/AppData/Local/Programs/Python/Python311/python.exe

import cgitb
cgitb.enable()

print("Content-type: text/html\r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PGP Student Portal - Home</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="icon" type="image/png" href="static/images/pgp.png">
  <style>
    .carousel-item img {
      height: 400px;
      object-fit: cover;
    }
    .sidebar {
      min-height: 100vh;
      background-color: #343a40;
    }
    .sidebar a {
      color: white;
      padding: 15px;
      display: block;
      text-decoration: none;
    }
    .sidebar a:hover {
      background-color: #495057;
    }
    @media (max-width: 768px) {
      .sidebar {
        flex-direction: row;
        flex-wrap: wrap;
        min-height: auto;
      }
      .sidebar a {
        flex: 1 1 100%;
        text-align: center;
      }
    }
  </style>
</head>
<body class="bg-light">

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
      <!-- Welcome Section -->
      <div class="container mt-4 p-4 bg-white shadow rounded text-center">
        <h1 class="mb-4">Welcome to PGP Student Management System</h1>
        <p class="lead">Register, Login & Manage Your Student Profile Easily</p>
        <a href="register.py" class="btn btn-success m-2">Get Started</a>
        <a href="login.py" class="btn btn-primary m-2">Login Now</a>
      </div>

      <!-- Carousel -->
      <div class="container mt-4 mb-5">
        <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner rounded">
            <div class="carousel-item active">
              <img src="static/images/c6.jpg" class="d-block w-100" alt="Slide 1">
            </div>
            <div class="carousel-item">
              <img src="static/images/pgp-build2.jpg" class="d-block w-100" alt="Slide 2">
            </div>
            <div class="carousel-item">
              <img src="static/images/confr5.jpg" class="d-block w-100" alt="Slide 3">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
          </button>
        </div>
      </div>
     


     
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
