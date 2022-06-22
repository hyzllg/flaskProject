import json

from flask import Flask,render_template,Response,request,make_response,url_for,redirect
import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []
girls = []
@app.route('/livecity/<string:city>/')
def hello_world(city):
    return f"我最喜欢的城市是：{city}"

@app.route('/login/',endpoint='login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if users:
            for user in users:
                if user.get('username') == username and user.get('password') == password:
                    return "登录成功"
                else:
                    return "账号密码错误"
        else:
            return "未匹配到账号信息"
    return render_template('login.html')

@app.route('/register/',methods=["GET","POST"],endpoint='register')
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        is_password = request.form.get('is_password')
        print(username,password,is_password)
        if username != '' or password != '' or is_password != '':
            if password == is_password:
                user = {'username':username,'password':password}
                users.append(user)
                print(users)
                return redirect(url_for('index'))
            else:
                return "两次输入的密码不一致"
    return render_template('register.html')

@app.route('/index/',endpoint='index')
def index():
    return render_template('index.html')

@app.route('/test/')
def test():
    Response = make_response("大家好！")
    Response.headers['myhesders'] = '111'
    Response.set_cookie('zheshicookie')
    return Response

@app.route('/show/')
def show():
    response = render_template('show.html',girls=girls,users=users)
    return response

if __name__ == '__main__':
    app.run()
