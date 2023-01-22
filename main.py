import polars as pl

file = "./passport-index-dataset/passport-index-tidy-iso3.csv"

df_csv = pl.scan_csv(file)

"""
Results would be like, countries where Argentina visa is required but not Venezuelan

Country | Passport
"""

needs_visa = df_csv.filter(
    (pl.col("Passport") == "VEN") | (pl.col("Passport") == "ARG")
).with_column(
    pl.col("Requirement")
    .str.contains(r"required|covid|e\-visa|arrival")
    .alias("needs_visa")
)

venezuelan_visas = needs_visa.filter(pl.col("Passport") == "VEN")
arg_visas = needs_visa.filter(pl.col("Passport") == "ARG")

total = venezuelan_visas.join(arg_visas, on="Destination")
f = total.filter((pl.col("needs_visa") == True) & (pl.col("needs_visa_right") == False))

pl.Config.set_tbl_rows(100)

print(f.collect())
