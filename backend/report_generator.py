import pandas as pd

class ReportGenerator:

    @staticmethod
    def generate_csv_report(df: pd.DataFrame, path: str):

        df.describe(include="all").to_csv(path)

        return path