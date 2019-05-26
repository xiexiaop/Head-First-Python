from flask import Flask, render_template, request, redirect
from vsearch import search4Letters

app = Flask(__name__)
@app.route('/')
# def hello() -> str:
#     return 'Hello world from Flask'

# Flask-Redirect
def hello() -> '302':
    return redirect('/entry')


@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4Letters(phrase, letters))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
