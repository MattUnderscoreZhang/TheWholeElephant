from enum import Enum, auto
import glob
from pathlib import Path
from flask import Flask, request, jsonify
import logging
from elephant_news.core.color_scheme import Colors, prompt_style, print_color
from elephant_news.core.llm import llm_api
from elephant_news.core.log import Log, Message, read_article


app = Flask(__name__,  static_url_path="/", static_folder='../fe2')

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def static_file(path):
    path1 = app.instance_path
    return app.send_static_file(path)


@app.route("/ask", methods=["POST"])
def ask():
    ensure_openai_token()
    approach = request.json["approach"]
    try:
        #impl = ask_approaches.get(approach)
        #if not impl:
        #    return jsonify({"error": "unknown approach"}), 400
        r = "hello" #impl.run(request.json["question"], request.json.get("overrides") or {})
        results = "test"
        q = "test"
        return {"data_points": results, "answer": "hello", "thoughts": f"Searched for:<br>{q}<br><br>Prompt:<br>" + "hello".replace('\n', '<br>')}
    except Exception as e:
        logging.exception("Exception in /ask")
        return jsonify({"error": str(e)}), 500


@app.route("/chat", methods=["POST"])
def chat():
    ensure_openai_token()
    approach = request.json["approach"]
    try:
        #impl = chat_approaches.get(approach)
        #if not impl:
        #    return jsonify({"error": "unknown approach"}), 400
        r = "whoops!"  #impl.run(request.json["history"], request.json.get("overrides") or {})
        results = "another test"
        q = "another test"
        return {"data_points": results, "answer": "hello", "thoughts": f"Searched for:<br>{q}<br><br>Prompt:<br>" + "hello".replace('\n', '<br>')}
    except Exception as e:
        logging.exception("Exception in /chat")
        return jsonify({"error": str(e)}), 500

def ensure_openai_token():
    return
    global openai_token
    if openai_token.expires_on < int(time.time()) - 60:
        openai_token = azure_credential.get_token("https://cognitiveservices.azure.com/.default")
        openai.api_key = openai_token.token
    
