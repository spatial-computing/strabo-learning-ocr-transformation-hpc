from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
import xgboost
import Data2


__author__ = 'rmenon'


def classify(training_label='l'):
    print('Reading data.')
    x, y = Data2.get_dataset2(0.3, training_label)

    print('Begin training.')
    clf = OneVsRestClassifier(xgboost.XGBClassifier(n_estimators=100, silent=False, nthread=4))
    clf.fit(x, y)
    joblib.dump(clf, 'gbc_model_' + training_label + '.pkl')

    print('Finish.')