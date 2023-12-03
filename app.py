# importing flask
# importing pandas module
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
# @app.route('/table')
# @app.route('/upload-csv/', methods=['POST'])
def table():
    data = pd.read_csv('./bill.csv')
    print(data)
    data.fillna(0, inplace=True)
    result = data.to_dict(orient='records')
    return render_template('/table.html', tables=result, titles=[''])


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
