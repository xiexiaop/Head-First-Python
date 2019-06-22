from flask import Flask, render_template, request, redirect, escape
from vsearch import search4Letters
import mysql.connector
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'xiezac',
        'password': '1121',
        'database': 'vsearchlogDB'
    }
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'

# Logging the request and response data
def log_request(req: 'flask_request', res: str) -> None:
    # DBLog with version
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                            (phrase,letters,ip,browser_string,results) values
                            (%s,%s,%s,%s,%s) """
            cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                                    req.remote_addr, req.user_agent.browser, res))
    except Exception as err:
        print('****** Some errors happens in database connection:',str(err))

# ********************************************************
# Flask-Redirect
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4Letters(phrase, letters))
    try:
        log_request(req=request, res=results)
    except Exception as err:
        print('******* Logging failed with this error:', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """ select phrase, letters, ip, browser_string, results from log"""
        contents = []
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ['Form Data', 'Remote Address', 'User Agent', 'Result']
    # 删除第一条数据
    contents.pop(0)
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
