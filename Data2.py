import numpy, csv
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.externals import joblib


def get_dataset2(test_fraction, training_label=''):
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

    y_shape = y.shape
    for i in range(0, y_shape[0]):
        y[i] = 1 if y[i] == training_label else 0

    # X,y = get_tabledata()

    vec = DictVectorizer()
    feature_dict = [dict(enumerate(x)) for x in X.tolist()]
    X = vec.fit_transform(feature_dict).toarray()
    joblib.dump(vec, 'vectorizer.pkl')

    lb = LabelBinarizer()
    y = lb.fit_transform(y)
    joblib.dump(lb, 'binarizer_' + training_label + '.pkl')
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction)
    # return X_train, X_test, y_train, y_test
    return X, y


def remove_duplicates():
    dataset = list()
    dup_count = 0
    add_count = 0
    with open('labels.csv', 'r') as datafile:
        csv_reader = csv.reader(datafile, delimiter=',', quotechar='|')
        for row in csv_reader:
            if row in dataset:
                dup_count += 1
            else:
                dataset.append(row)
                add_count += 1

            if (dup_count + add_count) % 1000 == 0:
                print('%d duplicate found. %d added. total: %d' % (dup_count, add_count, dup_count + add_count))

    with open('labels3.csv', 'w') as output:
        writer = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for r in dataset:
            writer.writerow(r)
    pass


if __name__ == '__main__':
    remove_duplicates()