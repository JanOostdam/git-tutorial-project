from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpele "database" - gewoon een lijst in memory
gebruikers = []

@app.route('/')
def home():
    return render_template('index.html', gebruikers=gebruikers)

@app.route('/add', methods=['POST'])
def add_user():
    naam = request.form.get('naam')
    if naam:
        gebruikers.append(naam)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)