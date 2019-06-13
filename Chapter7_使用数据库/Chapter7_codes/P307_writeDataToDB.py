from flask import Flask, render_template, request, redirect, escape
from vsearch import search4Letters
import mysql.connector

app = Flask(__name__)
@app.route('/')
# def hello() -> str:
#     return 'Hello world from Flask'
# Logging the request and response data
def log_request(req: 'flask_request', res: str) -> None:
    #     with open('log_request.log', 'a') as log:
    #         # print(str(dir(req)), res, file=log)

    #         # print(req.form, file=log, end='|')
    #         # print(req.remote_addr, file=log, end='|')
    #         # print(req.user_agent, file=log, end='|')
    #         # print(res, file=log)

    #         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

        # ********************************************************
        # DBLog
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'xiezac',
        'password': '1121',
        'database': 'vsearchlogDB'
    }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
                    (phrase,letters,ip,browser_string,results) values
                    (%s,%s,%s,%s,%s) """
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                          req.remote_addr, req.user_agent.browser, res))
    conn.commit()
    cursor.close()
    conn.close()
    # ********************************************************

#     # ********************************************************
#     # DBLog with version
#     dbconfig = {
#         'host': '127.0.0.1',
#         'user': 'xiezac',
#         'password': '1121',
#         'database': 'vsearchlogDB'
#     }
#     with UseDatabase(dbconfig) as cursor:
#         _SQL = """insert into log
#                         (phrase,letters,ip,browser_string,results) values
#                         (%s,%s,%s,%s,%s) """
#         cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
#                                 req.remote_addr, req.user_agent.browser, res))
# # ********************************************************
# Flask-Redirect


def hello() -> '302':
    return redirect('/entry')


@app.route('/search', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4Letters(phrase, letters))

    log_request(req=request, res=results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    # with open('log_request.log') as logviewer:
    #     contents = logviewer.read()
    # return escape(contents)

    contents = []
    with open('log_request.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    # return str(contents)

    titles = ['Form Data', 'Remote Address', 'User Agent', 'Result']
    # 删除第一条数据
    contents.pop(0)
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)


app.run(debug=True)
