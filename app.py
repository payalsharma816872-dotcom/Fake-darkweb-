from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Chat Website</title>
        <style>
            body{
                background:#111;
                color:#00ff00;
                font-family:Arial;
                text-align:center;
                padding-top:100px;
            }
            a{
                color:#00ff00;
                text-decoration:none;
                border:1px solid #00ff00;
                padding:10px 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Chat Website</h1>
        <p>Your Flask app is running successfully.</p>
        <a href="/login">Login</a>
    </body>
    </html>
    """

@app.route("/login")
def login():
    return """
    <h2>Login Page</h2>
    <p>This is a starter page.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
