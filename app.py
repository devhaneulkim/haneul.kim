from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/minus')
def minus():
   return render_template("calculator/minus.html")

@app.route('/plus')
def plus():
   return render_template("calculator/plus.html")

@app.route('/multiple')
def multiple():
   return render_template("calculator/multiple.html")

@app.route('/divide')
def divide():
   return render_template("calculator/divide.html")



@app.route('/approval')
def approval():
   return render_template("esg/report_chatbot/approval.html")

@app.route('/chatbot')
def chatbot():
   return render_template("esg/report_chatbot/chatbot.html")

@app.route('/dashboard')
def dashboard():
   return render_template("esg/report_chatbot/dashboard.html")


@app.route('/energy')
def energy():
   return render_template("esg/data_platform/energy.html")


@app.route('/finserv')
def finserv():
   return render_template("esg/data_platform/finserv.html")


@app.route('/manufacturer')
def manufacturer():
   return render_template("esg/data_platform/manufacturer.html")

@app.route('/bigretail')
def bigretail():
   return render_template("esg/auto_system/bigretail.html")

@app.route('/build')
def build():
   return render_template("esg/auto_system/build.html")

@app.route('/healthcare')
def healthcare():
   return render_template("esg/auto_system/healthcare.html")



if __name__ == '__main__ ' :
   app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True