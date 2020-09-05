from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


class MlModels:

    @staticmethod
    def get_all_objects(dataset, features):
        result = []
        for count in range(len(dataset[0])):
            for pair in range(count+1, len(dataset[0])):
                variant = []
                for element in dataset:
                    variant.append({'x': element[count], 'y': element[pair]})
                result.append({'{}:{}'.format(features[count], features[pair]): variant.copy()})
        return result

    @staticmethod
    def iris():
        iris_dataset = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                            iris_dataset['target'],
                                                            random_state=0)

        return iris_dataset

    @staticmethod
    def titanic():
        pass

    @staticmethod
    def movies():
        pass
