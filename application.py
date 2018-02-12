from flask import Flask
#from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy #for postgres
 

#db = MongoEngine()
################
#### config ####
################

def create_app(**config_overrides):
	#app = Flask(__name__)
	app = Flask(__name__)
	db = SQLAlchemy()
	

	#Load config

	app.config.from_pyfile('settings.py')


	#apply overrides for tests

	app.config.update(config_overrides)

	# setup db
	db.init_app(app)

	####################
	#### blueprints ####
	####################
	from home.views import home_blueprint
	from recipes.views import recipes_blueprint
	from users.views import users_blueprint

	#register blueprints
	app.register_blueprint(home_blueprint)
	app.register_blueprint(recipes_blueprint)
	app.register_blueprint(users_blueprint)

	
	
	return app
	
