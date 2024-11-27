from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        visitor_name = request.form['visitor_name']
        session['visitor_name'] = visitor_name  # Store visitor's name in session
        return redirect('/welcome')  # Redirect to the welcome page
    return render_template('index.html')

# Route for the welcome page
@app.route('/welcome')
def welcome():
    visitor_name = session.get('visitor_name', 'Guest')  # Retrieve name from session
    return render_template('welcome.html', visitor_name=visitor_name)

# Route for the everyday security page
@app.route('/everyday-security')
def everyday_security():
    visitor_name = session.get('visitor_name', 'Guest')
    return render_template('everyday-security.html', visitor_name=visitor_name)

# Route for the quiz page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    visitor_name = session.get('visitor_name', 'Guest')
    if request.method == 'POST':
        # Get the answers from the form and calculate the score
        score = 0
        answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5'),
            'q6': request.form.get('q6'),
            'q7': request.form.get('q7'),
            'q8': request.form.get('q8'),
            'q9': request.form.get('q9'),
            'q10': request.form.get('q10')
        }

        # Define the correct answers for the quiz
        correct_answers = {
            'q1': '1', 'q2': '2', 'q3': '1', 'q4': '2', 'q5': '2',
            'q6': '2', 'q7': '2', 'q8': '1', 'q9': '1', 'q10': '2'
        }

        # Calculate score
        for question, answer in answers.items():
            if answer == correct_answers.get(question):
                score += 1

        session['score'] = score  # Store the score in the session
        return redirect('/results')  # Redirect to results page
    return render_template('quiz.html', visitor_name=visitor_name)

# Route for the results page
@app.route('/results', methods=['GET'])
def results():
    visitor_name = session.get('visitor_name', 'Guest')
    score = session.get('score', 0)  # Retrieve the score from session
    return render_template('results.html', visitor_name=visitor_name, score=score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Set host to 0.0.0.0 and port to 5000
