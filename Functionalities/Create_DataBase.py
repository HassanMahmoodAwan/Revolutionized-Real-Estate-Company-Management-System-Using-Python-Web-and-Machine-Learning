import pandas as pd


def create_database(features, name):
    database_feature = {}
    for feature in features:
        database_feature[feature] = []

    database = pd.DataFrame(database_feature)
    database.to_csv(f'{name}.csv')



