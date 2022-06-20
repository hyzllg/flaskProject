from flask import Flask,render_template,Response,request,make_response
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/livecity/<string:city>/')
def hello_world(city):
    return f"我最喜欢的城市是：{city}"

@app.route('/login/')
def login():
    r = render_template('login.html')
    return r

@app.route('/index/',methods=['GET','POST'])
def index():
    print(request.method)
    #判断请求方式
    if request.method == 'GET':
        print(request.args)
        print(request.args.get('username'))
    elif request.method == 'POST':
        print(request.form)
        print(request.form.get('username'))
    return "这是首页！"

@app.route('/test/')
def test():
    Response = make_response("大家好！")
    Response.headers['myhesders'] = '111'
    Response.set_cookie('zheshicookie')
    return Response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
