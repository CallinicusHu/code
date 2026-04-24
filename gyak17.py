import pandas as pd
from pathlib import Path


file_path = r"C:\Users\User\Documents\RPG dolgok\hh télitábor 26\szentborb 26.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="játékbeosztáscsütörtök"
)

# directory where the python file is
out_path = Path(__file__).parent / "gamescsut26tt.csv"

df.to_csv(out_path, index=False, encoding="utf-8-sig")

p = Path("C:/Users/User/code/script.py")
print(p.parent)