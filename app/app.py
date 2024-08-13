from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    content = open('content','r').read()
    return render_template('index.html', content=content)

@app.post("/save")
def save():
    content = request.json.get('content')
    content = open('content','w').write(content)
    return 'saved'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
