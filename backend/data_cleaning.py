import pandas as pd

class DataCleaning:

    @staticmethod
    def clean_dataframe(df: pd.DataFrame):

        df = df.copy()

        # remove duplicates
        df = df.drop_duplicates()

        # drop empty rows
        df = df.dropna(how="all")

        # fill numeric missing
        numeric_cols = df.select_dtypes(include="number").columns

        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

        # fill categorical
        cat_cols = df.select_dtypes(include="object").columns

        df[cat_cols] = df[cat_cols].fillna("Unknown")

        return df