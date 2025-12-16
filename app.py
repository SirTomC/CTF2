from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '<h3>Go to <a href="/dashboard">/dashboard</a></h3>'

@app.route('/dashboard')
def dashboard():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>User Dashboard</title>
      <style>
        body {
          font-family: Arial;
          background: #f4f4f4;
          color: #333;
        }
        #flag {
          display: none;
          background: #1e1e1e;
          color: lime;
          padding: 1em;
          border-radius: 5px;
          margin-top: 1em;
        }
      </style>
    </head>
    <body>
      <h2>Welcome to your dashboard</h2>
      <p>Status: <span id="status">Logged in as guest</span></p>
      <button onclick="checkAdmin()">Check Access</button>

      <div id="flag">FLAG{no_auth_logic}</div>

      <script>
        // Insecure client-side only check
        let user = "guest";

        function checkAdmin() {
          if (user === "admin") {
            document.getElementById("status").textContent = "Logged in as admin";
            document.getElementById("flag").style.display = "block";
          } else {
            alert("Access denied. You are not an admin!");
          }
        }
      </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
