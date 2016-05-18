__author__ = 'rmenon'

import database
import numpy, csv
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.externals import joblib


def get_tabledata():
    """
    Gets data from the database and splits into features and labels
    :return: X, y
    """
    rows = database.connect()
    data = numpy.asarray(rows)
    X = data[:, 0:data.shape[1]-1]
    y = data[:, data.shape[1]-1]
    return X,y


def get_tabledata2():
    """
    Gets data from the database and splits into features and labels
    :return: X, y
    """
    rows = database.connect()
    return rows

def get_dataset(test_fraction):
    """
   @:param: test_fraction used to split train and test
   Vectorizes the features and labels into categorical values and randomly splits into train and test set
   :return: X_train, X_test, y_train, y_test
   """
    X,y = get_tabledata()

    vec = DictVectorizer()
    feature_dict = [dict(enumerate(x)) for x in X.tolist()]
    X = vec.fit_transform(feature_dict).toarray()
    joblib.dump(vec, 'vectorizer.pkl')

    lb = LabelBinarizer()
    y = lb.fit_transform(y)
    joblib.dump(lb, 'binarizer.pkl')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction)
    return X_train, X_test, y_train, y_test


def get_dataset2(test_fraction):
    """
   @:param: test_fraction used to split train and test
   Vectorizes the features and labels into categorical values and randomly splits into train and test set
   :return: X_train, X_test, y_train, y_test
   """
    data = []
    with open('labels.csv', 'r') as datafile:
        csv_reader = csv.reader(datafile, delimiter=',', quotechar='|')
        for row in csv_reader:
            data.append(row)

    data = numpy.asarray(data)
    X = data[:, 0:data.shape[1]-1]
    y = data[:, data.shape[1]-1]

    # X,y = get_tabledata()

    vec = DictVectorizer()
    feature_dict = [dict(enumerate(x)) for x in X.tolist()]
    X = vec.fit_transform(feature_dict).toarray()
    joblib.dump(vec, 'vectorizer.pkl')

    lb = LabelBinarizer()
    y = lb.fit_transform(y)
    joblib.dump(lb, 'binarizer.pkl')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction)
    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    d = get_tabledata2()
    with open('labels.csv', 'w') as output:
        writer = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for r in d:
            writer.writerow(r)