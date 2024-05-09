from flask import Flask,request,jsonify
import markdown
from pdf_module import getText
app=Flask(__name__)


@app.route("/")
def index():
    return "<h1>HTML2Markdown App</h1>"

@app.route("/getPdfText",methods=["GET","POST"])
def getPDFText():
    if request.method=="POST":
        f = request.files['file'] 
        print(f.filename)
        f.save(f.filename)   
        text=getText(f.filename)
        return jsonify({"text":text})
    return "Send file"

@app.route("/getHTML",methods=["GET","POST"])
def getHTML2Markdown():
    if request.method=="POST":
        markdown_data=request.form.get('markdown_data')
        html_data=markdown.markdown(markdown_data)
        return jsonify({"html_data":html_data})
    return "<h2>POST Request On '/getHTML' endpoint with 'markdown' data as body parameter</h2>"