import pandas as pd


def load_and_clean_data(path):
    # Column names for wine dataset
    columns = [
        "target",
        "alcohol",
        "malic_acid",
        "ash",
        "alcalinity",
        "magnesium",
        "phenols",
        "flavanoids",
        "nonflavanoid_phenols",
        "proanthocyanins",
        "color_intensity",
        "hue",
        "od280_od315",
        "proline",
    ]

    df = pd.read_csv(path, header=None, names=columns)

    # No missing values in this dataset, but just in case
    df.dropna(inplace=True)

    return df
