from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQL_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.no} - {self.title}"

@app.route("/")
def hello_world():
    todo=Todo(title="First Todo Task", desc="Start diving into blockchain security")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")
    # return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
