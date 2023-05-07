import re
from flask import Flask,request,redirect,render_template
app=Flask(__name__,
    static_folder="image",
    static_url_path="/i"

) #__name__代表目前執行的模組

@app.route("/re")
def red():
    return redirect("https://www.google.com.tw")


@app.route("/") #函式的裝飾(Decorator):以函式為基礎，判讀url後的query來提供功能
def index():
    
    return render_template("index.html")

@app.route("/getSum")
def getsum():
    data=request.args.get("data",100)
    result=1
    for i in range(1,int(data)+1):
        result*=i
    return "結果： "+str(result)

@app.route("/page") #函式的裝飾(Decorator):以函式為基礎，判讀url後的query來提供功能
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("Third.html")

if __name__=="__main__": #如果以主程式執行
    app.run(port=3000)   #立刻啟動伺服器,可透過port參數指定埠號
