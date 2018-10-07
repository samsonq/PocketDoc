from Preprocessing import *

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import make_scorer, accuracy_score

from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split

X_train = data.drop(labels=["No-show"], axis=1)
y_train = data["No-show"]

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=0)

print("The test set is 20% of the dataset")


def classification_models(model, parameters):
    clf = model
    parameters = parameters
    grid_clf = GridSearchCV(clf, parameters, scoring=make_scorer(accuracy_score))
    grid_clf.fit(X_train, y_train)

    clf = grid_clf.best_estimator_
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return accuracy


acc_mnnb = classification_models(MultinomialNB(), {})
acc_rf = classification_models(RandomForestClassifier(), {})
acc_lr = classification_models(LogisticRegression(), {})
acc_gnb = classification_models(GaussianNB(), {})
acc_dt = classification_models(DecisionTreeClassifier(), {})

accuracies = {"Multinomial NB": acc_mnnb, "Random Forest": acc_rf, "Logistic Regression": acc_lr, "Gaussian NB": acc_gnb,
              "Decision Tree": acc_dt}

best_model = max(accuracies, key=accuracies.get)

print("The best model is: " + str(best_model))
print("The accuracy of " + str(best_model) + " is: " + str(max(accuracies.values())))