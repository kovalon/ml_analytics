from flask import jsonify, render_template

from app import app
from app.models import MlModels


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iris')
def iris():
    return render_template('iris.html')


@app.route('/irisdata')
def iris_data():
    dataset = MlModels.iris()
    return jsonify({'dataset': dataset['data'].tolist(),
                    'target': dataset['target'].tolist()})
