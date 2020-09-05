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
    result = MlModels.get_all_objects(dataset=dataset['data'].tolist(), features=dataset['feature_names'])
    return jsonify({'dataset': result})
