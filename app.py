from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        df = pd.read_csv('Coding_Problems_Week_1.csv')
        for i in df.index:
            df.at[i, 'Status'] = 'Completed' if data.get(str(i)) == 'on' else ''
        df.to_csv('Coding_Problems_Week_1.csv', index=False)
    else:
        df = pd.read_csv('Coding_Problems_Week_1.csv')
    return render_template('index.html', problems=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
