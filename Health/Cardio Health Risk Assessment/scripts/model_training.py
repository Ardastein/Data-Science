from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

def train_models(X_train, y_train):
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    
    svc = SVC()
    svc.fit(X_train, y_train)
    
    return lr, rf, svc

def hyperparameter_tuning(X_train, y_train):
    rf = RandomForestClassifier()
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30]
    }
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    best_rf = grid_search.best_estimator_
    
    return best_rf
