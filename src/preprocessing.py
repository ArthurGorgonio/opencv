import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("base.csv")

samples = data.iloc[:, 0:4095].values
target = data.iloc[:, 4096].values

# Spliting train ans test data
X_train, X_test, y_train, y_test = train_test_split(
    samples, target, test_size=0.25, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Perform LDA
lda = LDA(n_components=2081)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)

# Classify
model = rf(max_depth=4, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Scoring
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("Acc" + str(accuracy_score(y_test, y_pred)))
