from flask import Flask,render_template,request
import pickle
import numpy as np
model =pickle.load(open('ER.pkl','rb'))
app=Flask(__name__)


@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def home():
    data1=request.form['a']
    data2=request.form['b']
    data3=request.form['c']
    data4=request.form['d']
    data5=request.form['f']
    data6=request.form['h']
    data7=request.form['i']
    data8=request.form['j']
    if data6=='0':
          n1,n2=1,0
    elif data6=='1':
          n1,n2=0,1
    else:
        n1,n2=0,0

    
    arr =np.array([[data1,data2,data3,data7,data8,data5,data4,n1,n2]])
    pred=model.predict(arr)
    return render_template('output.html',data=pred)
    
#" data1 "+str(data1)+" data2 "+str(data2)+" data3 "+str(data3)+" data7 "+str(data7)+" data8 "+str(data8)+" data5 "+str(data5)+" data4 "+str(data4)+" a "+str(a)+" b "+str(b)
if __name__=="__main__":
    app.run(debug=True)