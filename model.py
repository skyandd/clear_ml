from sklearn import svm
from sklearn import datasets
from joblib import dump, load

from clearml import Task


if __name__  == '__main__':
    task = Task.init(
        project_name='My test project',
        task_name='Iris classification'
    )

    clf = svm.SVC()
    X, y= datasets.load_iris(return_X_y=True)
    clf.fit(X, y)
    dump(clf, 'filename.joblib')