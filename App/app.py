from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    from sklearn.datasets import load_iris
    import pandas as pd
    import perceptron as pc
    import numpy as np
    
    iris = load_iris()

    df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])

    X = df.iloc[:100,[0,2]].values
    y = df.iloc[0:100,4].values
    y = np.where(y == 0, -1, 1)

    global ppn
    ppn = pc.Perceptron(n_iter=20)
    ppn.fit(X,y)


    return '<h1>test</h1>'

@app.route('/Abc', methods=['GET'])
def get_prediction():

    from flask import request
    from flask import jsonify
        
    length_s = float(request.args.get('length_s'))
    length_p = float(request.args.get('length_p'))

    data = [length_s, length_p]

    try:
    
        predicted_class = int(ppn.predict(data))

        return jsonify(data=data, predicted_class=predicted_class)
    
    except:
        return jsonify(data=data, predicted_class='Invalid predition')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
