from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQL_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.no} - {self.title}"

    # converting to dict so that it can be easily written in JSON
    def to_dict(self):
        return {
            'no': self.no,
            'title': self.title,
            'desc': self.desc,
            'date_created': self.date_created.isoformat()
        }


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request == 'POST':
        print("Post")
    todo = Todo(title="First Todo",
                desc="Start blockchain security")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
    # return "Hello, World!"


@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return jsonify(allTodo.to_dict())


if __name__ == "__main__":
    app.run(debug=True, port=8000)
