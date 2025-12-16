from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def calc():
    op = request.args.get('op')
    a = float(request.args.get('x'))
    b = float(request.args.get('y'))

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b 
    elif op == 'pow':
        result = a ** b
    else:
        raise ValueError("Unsupported operation")
    
    return f"""
        <h3>Calculator</h3>
        <p><b>Result:</b> {result}</p>
    """

@app.errorhandler(500)
def error(e):
    return f"""
        <h3>Calculator</h3>
        <p>Oops, something went wrong!</p>
        <pre>{e}</pre>
        <hr>
        <code>Tommy{{pLz_Us3_As_1nT3nd3d}}</code>
    """, 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
