from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def calc():
    try:
        # Get values with fallback defaults
        op = request.args.get('op')
        x = request.args.get('x')
        y = request.args.get('y')

        # If no parameters provided, just show page with no result
        if not op or not x or not y:
            return '''
                <h3>Calculator</h3>
                <p>Provide parameters like <code>?op=add&x=1&y=2</code></p>
            '''

        a = float(x)
        b = float(y)

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
            <p><b>Operation:</b> {op}({a}, {b})</p>
            <p><b>Result:</b> {result}</p>
        """

    except Exception as e:
        return f"""
            <h3>Calculator</h3>
            <p>Oops, something went wrong!</p>
            <pre>{e}</pre>
            <hr><code>Tommy{{pLz_Us3_As_1nT3nd3d}}</code>
        """, 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
