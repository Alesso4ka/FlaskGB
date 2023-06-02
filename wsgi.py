import os
from blog.app import create_app, db
from commands import init_db, create_admin, create_tags

#app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        debug=True,
    )
