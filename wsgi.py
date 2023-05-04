import os
from blog.app import app, db
from commands import init_db, create_admin

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )
