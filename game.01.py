from flask import Flask, request

app = Flask(__name__)

STYLE = """
<style>
body {
    background: url("/static/bg.jpg") no-repeat center center fixed;
    background-size: cover;
    font-family: monospace;
    color: white;
    text-align: center;
    padding-top: 60px;
}

button {
    font-family: monospace;
    padding: 10px 15px;
    margin: 10px;
    background: black;
    color: white;
    border: 2px solid white;
    cursor: pointer;
}

button:hover {
    background: white;
    color: black;
}
</style>
"""

@app.route("/")
def home():
    return STYLE + """
    <h1>Welcome human</h1>

    <p>This is the planet Sparta in ruins after Kratos destroyed it.</p>

    <p>Robots await your command...</p>

    <form action="/choice" method="POST">
        <button name="option" value="1">Destruction</button>
        <button name="option" value="2">Challenge The Robots</button>
        <button name="option" value="3">Betrayal</button>
    </form>
    """

@app.route("/choice", methods=["POST"])
def choice():
    option = request.form.get("option")

    if option == "1":
        return STYLE + """
        <h2 style='color:red;'>You chose destruction...</h2>
        <h3>GAME OVER</h3>

        <form action="/" method="GET">
            <button>Restart</button>
        </form>
        """

    elif option == "2":
        return STYLE + """
        <h2 style='color:orange;'>You challenged the robots!</h2>
        <h3>CHARGE!!!</h3>

        <form action="/" method="GET">
            <button>Restart</button>
        </form>
        """

    elif option == "3":
        return STYLE + """
        <h2 style='color:purple;'>Betrayal detected...</h2>
        <h3>You were thrown off the ship</h3>

        <form action="/" method="GET">
            <button>Restart</button>
        </form>
        """

    else:
        return STYLE + """
        <h2>Error 404</h2>

        <form action="/" method="GET">
            <button>Restart</button>
        </form>
        """

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
