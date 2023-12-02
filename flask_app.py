from flask import Flask, render_template

app=Flask(__name__)
app.run(port=5000, debug=True)

@app.route('/')
def default():
    return"<p>Hello World!</p>"


    app.run(port=5000, debug=True)

