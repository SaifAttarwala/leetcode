# Last updated: 8/17/2025, 2:03:53 AM
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    