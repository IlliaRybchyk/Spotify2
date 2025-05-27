from app import app
from routers.auth import auth

if __name__ == '__main__':
    app.run(debug=True)
