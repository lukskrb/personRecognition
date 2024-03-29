import pickle
import numpy as np
    
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

desired_length = 500
X = []
y = []

for input_mode in ["Finger", "Stylus"]:
    for user_id in range(20):
        if user_id in data and input_mode in data[user_id]:
            user_data = data[user_id]

            for content_id in range(26,312):
                if "tablet" in user_data.get(input_mode, {}) and str(content_id) in user_data[input_mode]["tablet"]:
                    input_data = user_data[input_mode]["tablet"][str(content_id)]
                   
                    clean_data = input_data['data']

                    features = [
                    clean_data['ts'],
                    clean_data['rawposX'],
                    clean_data['rawposY'],
                    clean_data['relposX'],
                    clean_data['relposY'],
                    clean_data['velX'],
                    clean_data['velY'],
                    clean_data['magX'],
                    clean_data['magY'],
                    clean_data['magZ'],
                    clean_data['orientation'],
                    clean_data['pressure'],
                    clean_data['size']
                    ]

                    # Nadopuna podataka do zeljene duzine
                    for feature in features:
                        print(len(feature))
                    padded_features = [np.pad(feature, (0, desired_length - len(feature)), mode='constant') for feature in features]

                    features_concatenated = np.concatenate(padded_features)

                    #print("Length of features_concatenated:", len(features_concatenated))


                    X.append(features_concatenated)
                    y.append(user_id)

X = np.array(X)
y = np.array(y)

#print("Number of samples in the dataset:", len(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


scaler = StandardScaler()
X_train_standardized = scaler.fit_transform(X_train)
X_test_standardized = scaler.transform(X_test)

pca = PCA(n_components=0.95) 
X_train_pca = pca.fit_transform(X_train_standardized)
X_test_pca = pca.transform(X_test_standardized)

# Treniranje klasifikatora
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train_pca, y_train)

# Evaluacija modela
y_pred = classifier.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
