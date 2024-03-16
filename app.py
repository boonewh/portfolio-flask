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

if __name__ == '__main__':
    app.run(debug=True)