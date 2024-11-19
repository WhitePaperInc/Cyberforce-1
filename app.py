from flask import Flask, render_template, request

app = Flask(__name__)

# Route for homepage with form handling
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        return f"Hello, {username}! Welcome to Cyberforce-1!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
