
from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = b'\xa4\x04@}W;tW2\xba:QPxt\xa4'
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route("/test_session")
def test_session():
    session["name"] = "Mark"
    session.permanent = True
    return "<h1 style='color: red'>Session OK</h1>"




if __name__ == "__main__":
    app.run(debug=True)