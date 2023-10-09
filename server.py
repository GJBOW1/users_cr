from flask_app.controllers import user_accounts
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
