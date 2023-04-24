import os
import sys
import re
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '' # Not uploading this online :/
testList = []

@app.route("/", methods=("GET", "POST"))
def index():    
    if request.method == "POST":
        idea = request.form["idea"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(idea),
            temperature=0.6,
            max_tokens=250
        )
        text = response.choices[0].text.split('\n\n')
        global testList
        testList = text
    return render_template("index.html", result=testList    )


def generate_prompt(idea):
    return f"""
    Give me a 3 act structure for a movie based on {idea}, with each act summaraized to a single sentence
    """

app.run(debug=True)