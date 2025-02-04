from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template("auth/login.html")


@app.route('/index')
def index():
   return render_template("index.html")


@app.route('/login', methods=["POST"])
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
    


@app.route('/calc',methods=["POST", "GET"])
def calc():
    print("❤️계산기❤️")
    print("😝전송된 데이터 방식:😝", request.method)

    if request.method == "POST":
      print("😊post방식으로 전송된 데이터😊")
      num1 = request.form.get('num1')
      num2 = request.form.get('num2')
      opcode = request.form.get("opcode")

      
      print("num1:", num1)
      print("opcode:", opcode)
      print("num2:", num2)

      if opcode == "+": 
         result = int(num1) + int(num2)
      elif opcode == "-":
         result = int(num1) - int(num2)
      elif opcode == "*":
         result = int(num1) * int(num2)
      elif opcode == "/":
         result = int(num1) / int(num2)
      else:
         result = "⚠️연산자 오류 발생⚠️"


      print(f"{num1}{opcode}{num2}={result}")
      return render_template("calculator/calc.html", 
                           num1  = num1, opcode = opcode, num2 = num2, result = result)

    else:
       print("😊get방식으로 전송된 데이터😊")
       return render_template("calculator/calc.html")
    
@app.route('/minus')
def minus():
   return render_template("calculator/minus.html")


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