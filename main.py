from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This automatically finds your templates/index.html file
    return render_template('index.html')

if __name__ == '__main__':
    print("\n" + "="*50)
    print("WEBSITE RUNNING! Open this address in Google Chrome:")
    print("http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True)