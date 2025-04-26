import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(filepath='../data/creditcard.csv'):
    # Load dataset
    df = pd.read_csv(filepath)

    # Feature scaling
    scaler = StandardScaler()
    df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))

    # Drop original Amount and Time
    df.drop(['Time', 'Amount'], axis=1, inplace=True)

    # Rearranging columns
    scaled_amount = df.pop('scaled_amount')
    scaled_time = df.pop('scaled_time')
    df.insert(0, 'scaled_amount', scaled_amount)
    df.insert(1, 'scaled_time', scaled_time)

    # Features and label
    X = df.drop('Class', axis=1)
    y = df['Class']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        stratify=y, 
                                                        random_state=42)

    return X_train, X_test, y_train, y_test
