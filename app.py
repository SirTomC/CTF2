from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Try accessing /divide?num=0 or /divide?num=abc'

@app.route('/divide')
def divide():
    num = int(request.args.get('num', '1'))
    result = 100 // num
    return f"Result: {result}"

@app.errorhandler(500)
def error(e):
    return f"<h3>Oops, something went wrong!</h3><pre>{e}</pre><hr><code>Tommy{{pLz_Us3_As_1nT3nd3d}}</code>", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # required for Render
    app.run(host='0.0.0.0', port=port)
