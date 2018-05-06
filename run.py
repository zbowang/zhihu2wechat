from api import app
from settings import API_HOST, API_PORT

if __name__ == '__main__':
	app.run(API_HOST, API_PORT)