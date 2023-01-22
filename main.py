import polars as pl

file = "./passport-index-dataset/passport-index-tidy-iso3.csv"

df_csv = pl.scan_csv(file)

"""
Results would be like, countries where Argentina visa is required but not Venezuelan

Country | Passport
"""

ven_arg_query = df_csv.filter(
    (pl.col("Passport") == "VEN") | (pl.col("Passport") == "ARG")
).with_column(pl.col("Requirement").str.contains(r"visa|covid").alias("needs_visa"))

print(ven_arg_query.collect())
