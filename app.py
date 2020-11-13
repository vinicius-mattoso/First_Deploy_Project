import numpy as np
from flask import Flask, request, jsonify, render_template,render_template_string
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)

    if prediction == 0:
        #resp=Markup("<h1>Paciente sem Diabetes/<h1>")
        resp = 'Paciente sem Diabetes '
        print(resp)
        #return resp #render_template('index.html', prediction_text=resp)
        #render_template_string('{{resp}}')
        #return render_template('index.html')
        #return resp
    else:
        resp='Paciente com Diabetes '
        #resp = Markup("<h1>Paciente com Diabetes/<h1>")

        print(resp)
        #render_template_string('{{resp}}')
        #return render_template('index.html') #render_template('index.html', prediction_text=resp)
        #return  resp
    #output = round(prediction[0], 2)
    #print(output)


    return render_template('Resposta.html', prediction_text='{}'.format(resp))

if __name__ == "__main__":
    app.run(debug=True)