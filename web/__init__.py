from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from web.views.student.common import student_common
from web.views.student.v1.student import student_v1
from web.views.student.v2.student import student_v2

app = Flask(__name__)
app.register_blueprint(student_common)
app.register_blueprint(student_v1, url_prefix='/v1')
app.register_blueprint(student_v2, url_prefix='/v2/student')
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
