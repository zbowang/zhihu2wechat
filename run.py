from api import app
from settings import API_HOST, API_PORT
import threading, webbrowser

if __name__ == '__main__':
	url = 'http://localhost:1234'
	threading.Timer(1.5, lambda: webbrowser.open(url) ).start()
	app.run(API_HOST, API_PORT)