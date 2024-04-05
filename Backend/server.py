from flask import Flask,render_template, request
from database import get_logs, insert_log
from pathlib import Path

app = Flask(__name__, template_folder=Path(__file__).parent.parent / "Frontend")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dash')
def dash():
    return render_template('dashboard.html')

@app.route('/ping', methods=['Get'])
def ping_pong():
    insert_log("/ping")
    return "Pong"

@app.route('/echo', methods=['Post'])
def echo():
    insert_log("/echo")
    data = request.form["text"]
    return data

@app.route('/info', methods=['Get'])
def info():
    hmtl_logs = "<ul>"
    for log in get_logs():
        hmtl_logs += f"<li>{log['route_log']} - {log['date']} - {log['time']}</li>"
    hmtl_logs += "</ul>"

    return hmtl_logs

if __name__ == '__main__':
    app.run(debug=True)