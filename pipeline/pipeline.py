import pandas as pd
import sys

df = pd.DataFrame({f"day": [1, 2], "num_passengers": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")