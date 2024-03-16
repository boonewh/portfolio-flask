from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/roshambo', methods=['GET', 'POST'])
def roshambo():
    result = ""
    if request.method == 'POST':
        one = request.form.get('player1').lower()
        two = request.form.get('player2').lower()

        if one == "r":
            if two == "r":
                result = "It's a tie, throw again."
            elif two == "p":
                result = "Paper covers Rock, Player 2 wins!"
            elif two == "s":
                result = "Rock smashes Scissors, Player 1 wins!"
            else: 
                result = "Invalid move from Player 2."
        elif one == "p":
            if two == "r":
                result = "Paper covers Rock, Player 1 wins!"
            elif two == "p":
                result = "It's a tie, throw again."
            elif two == "s":
                result = "Scissors cut Paper, Player 2 wins!"
            else: 
                result = "Invalid move from Player 2."
        elif one == "s":
            if two == "r":
                result = "Rock smashes Scissors, Player 2 wins!"
            elif two == "p":
                result = "Scissors cut Paper, player 1 wins!"
            elif two == "s":
                result = "It's a tie, please throw again."
            else: 
                result = "Invalid move from Player 2."
        else:
            result = "Invalid move from Player 1."

    return render_template('roshambo.html', result=result)

@app.route('/technical')
def technical():
    return render_template('technical.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')


@app.route('/validate', methods=['POST'])
def validate():
    # Extract form data
    form_data = {
        'summary': request.form.get('summary', ''),
        'accID': request.form.get('accID', ''),
        'lname': request.form.get('lname', ''),
        'fname': request.form.get('fname', ''),
        'init': request.form.get('init', ''),
        'deptID': request.form.get('deptID', ''),
        'ssn': request.form.get('ssn', ''),
        'projID': request.form.get('projID', ''),
    }

    # Initialize an empty dictionary to keep track of errors
    errors = {}

    # Check for empty fields and add errors as needed
    for field, value in form_data.items():
        if not value:
            errors[field] = f'{field} is required.'

    # Additional pattern checks
    if form_data['accID'] and not form_data['accID'].startswith('ACC'):
        errors['accID'] = 'Account ID must start with ACC and follow the pattern ACCnnnn.'
    
    if form_data['deptID'] and not form_data['deptID'].startswith('DEPT'):
        errors['deptID'] = 'Department ID must start with DEPT and follow the pattern DEPTnnnn.'

    if form_data['ssn'] and not request.form['ssn'].replace('-', '').isdigit():
        errors['ssn'] = 'Social Security Number must be numeric and follow the pattern nnn-nn-nnnn.'

    if form_data['projID'] and not form_data['projID'].startswith('PROJ-'):
        errors['projID'] = 'Project ID must start with PROJ- and follow the pattern PROJ-nnnn.'

    # Check if there are any errors
    if errors:
        # If there are errors, render the validation template with error messages
        return render_template('validate.html', errors=errors, form_data=form_data)
    else:
        # If there are no errors, process the form data as needed (e.g., save to a database)
        # Then render the validation template with a success message
        return render_template('validate.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)