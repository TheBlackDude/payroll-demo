#!flask/bin/python
from flask import Flask, jsonify, request, render_template, redirect, flash, abort, Response
import pandas as pd
from models import save_data, read_data, report_exists, get_salary
import pprint

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/34HT%'

@app.route('/')
def index():
    if type(read_data()) != str:
        sql_data = read_data()
        # data = get_salary(sql_data)
        return render_template('home.html', data=get_salary(sql_data))
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    report_file = request.files['payroll']
    pd_data = pd.read_csv(report_file)

    if type(read_data()) != str:
        if report_exists(read_data(), pd_data):
            flash('Sorry this report already exist')
            abort(409)
    # str = pprint.pformat(data, depth=5)
    # return Response(str, mimetype="text/text")
    save_data(pd_data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
