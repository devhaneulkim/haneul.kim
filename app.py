from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template("auth/login.html")


@app.route('/index')
def index():
   return render_template("index.html")


@app.route('/login', methods=["post"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print("username:", username)
    print("password:", password)
    if username == "kim" and password == '1234': 
     print ("😊로그인 성공")
     return redirect(url_for('index')) 
    
    else :
     print("😂로그인 실패")
     return render_template("auth/loginfail.html")
    
    

   
@app.route('/minus')
def minus():
   return render_template("calculator/minus.html")

@app.route('/minusanswer', methods = ["POST"])
def minusanswer():
   print("➖뺄셈 알고리즘")
   num1 = request.form.get('num1')
   num2 = request.form.get('num2')
   print("num1:", num1)
   print("num2:", num2)
   result = int(num1) - int(num2)
   print("결과:", result)
   print("😊뺄셈 성공")
   return render_template("answer/minus.html", num1 = num1, num2 = num2, result = result)

@app.route('/plus')
def plus():
   return render_template("calculator/plus.html")


@app.route('/plusanswer',methods=["POST"])
def plusanswer():
    print("➕덧셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) + int(num2)
    print("결과:", result)
    print("😊덧셈 성공")
    return render_template("answer/plus.html", num1  = num1, num2 = num2, result = result)


@app.route('/multiple')
def multiple():
   return render_template("calculator/multiple.html")

@app.route('/multipleanswer',methods=["POST"])
def multipleanswer():
    print("✖️곱셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) * int(num2)
    print("결과:", result)
    print("😊곱셈 성공")
    return render_template("answer/multiple.html", num1  = num1, num2 = num2, result = result)


@app.route('/divide')
def divide():
   return render_template("calculator/divide.html")

@app.route('/divideanswer',methods=["POST"])
def divideanswer():
    print("➗나눗셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) / int(num2)
    print("결과:", result)
    print("😊나눗셈 성공")
    return render_template("answer/divide.html", num1  = num1, num2 = num2, result = result)


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