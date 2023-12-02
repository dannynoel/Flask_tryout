from flask import Flask, render_template

app=Flask(__name__)
app.run(port=5000, debug=True)

@app.route('/')
def ap():
    return"<p>Hello World!</p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

