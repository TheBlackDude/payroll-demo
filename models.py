import sqlite3
from datetime import datetime
import pandas as pd


# create db connection
def db_connection():
    conn = sqlite3.connect('reports.db')
    return conn


def save_data(data):
    conn = db_connection()
    data.to_sql('reports', conn, if_exists='replace', index=False)


def read_data():
    conn = db_connection()
    try:
        return pd.read_sql_query("SELECT * FROM reports", conn)
    except Exception as e:
        return "No table with that name found, Error: {}".format(e)


def report_exists(sql_data, csv_data):
    return sql_data.get('hours worked')[len(sql_data)-1] == csv_data.get('hours worked')[len(csv_data)-1]


def get_salary(data):
    employees = []
    for e in data.groupby('employee id').groups:
        employee = data[data['employee id'] == e]
        if employee.get('job group')[employee.first_valid_index()] == 'A':
            employees.append({ 'id': int(e), 'pay_period': '{0} - {1}'.format('1/15/2016', '15/11/2016'), 'amount_paid':  20 * employee.loc[:,['hours worked']].sum()[0] })
        else:
            employees.append({ 'id': int(e), 'pay_period': '{0} - {1}'.format('15/11/2016', '16/11/2016'), 'amount_paid':  30 * employee.loc[:,['hours worked']].sum()[0] })
    return employees


def get_date(groups):
    first_period = []
    second_period = []
    for date in groups:
        if datetime.strptime(date, '%d/%m/%Y') < datetime.strptime('15/11/2016', '%d/%m/%Y'):
            first_period.append(date)
        else:
            second_period.append(date)
    return first_period, second_period
