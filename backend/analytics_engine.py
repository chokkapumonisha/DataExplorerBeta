import pandas as pd

class AnalyticsEngine:

    @staticmethod
    def dataset_summary(df: pd.DataFrame):

        summary = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "column_names": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict(),
        }

        return summary

    @staticmethod
    def statistics(df: pd.DataFrame):

        stats = df.describe(include="all").fillna("").to_dict()

        return stats

    @staticmethod
    def correlation_matrix(df: pd.DataFrame):

        numeric_df = df.select_dtypes(include="number")

        corr = numeric_df.corr()

        return corr.to_dict()