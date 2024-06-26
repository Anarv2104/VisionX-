from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
# Add the correct import statement for your_application
from app import db  # Import the correct module or package that contains the "db" object

app = Flask(__name__)
migrate = Migrate(app, db)
manager = Manager(app)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()