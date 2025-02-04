from flask import *
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/buy')
def temp():
    return render_template('by page.html')
if __name__ == '__main__':
    app.run(debug=True)