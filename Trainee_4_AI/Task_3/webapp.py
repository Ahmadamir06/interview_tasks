from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from task3 import llm_call

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

chathistory = []


@app.route("/", methods=["GET", "POST"])
def index():
    message = llm_call("hello")
    print(message)
    chathistory.append(message)
    return jsonify(chathistory)
    

