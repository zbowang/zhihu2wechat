from flask import Flask, g, jsonify, render_template
from settings import HTML, BASE_HTML
from spiders.spiderquestion import QuestionSpider
from spiders.spidertopic import TopicSpider

__all__ = ['app']

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# http://localhost:1234
@app.route('/')
def index():
    return render_template('index.html')

# http://localhost:1234/topic/19552832/20
@app.route('/topic/<topic_id>/<number>')
def get_tweixin(topic_id, number):
    topic = TopicSpider(topic_id, int(number))
    return topic.get_html()

# http://localhost:1234/question/20799742/30
@app.route('/question/<question_id>/<number>')
def get_qweixin(question_id, number):
    question = QuestionSpider(question_id, int(number))
    return question.get_html()

