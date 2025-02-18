from flask import Flask

from question.questions import question_bp
from user.user import user_bp

app = Flask(__name__)

# Настройка для защиты
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'timofeyakmal8389188abbos'

app.register_blueprint(user_bp)
app.register_blueprint(question_bp)


@app.route('/', methods=['GET'])
def home():
    return 'Hello'


app.run(debug=True)
