from flask import Flask,request,jsonify
import markdown

app=Flask(__name__)


@app.route("/")
def index():
    return "<h1>HTML2Markdown App</h1>"

@app.route("/getHTML",methods=["GET","POST"])
def getHTML2Markdown():
    if request.method=="POST":
        markdown_data=request.form.get('markdown_data')
        html_data=markdown.markdown(markdown_data)
        return jsonify({"html_data":html_data})
    return "<h2>POST Request On '/getHTML' endpoint with 'markdown' data as body parameter</h2>"