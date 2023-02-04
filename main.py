import polars as pl

file = "./passport-index-dataset/passport-index-tidy-iso3.csv"

pl.Config.set_tbl_rows(100)

"""
Results would be like, countries where Argentina visa is required but not Venezuelan

Country | Passport
"""


def get_visa_countries(country1: str, country2: str):
    df_csv = pl.scan_csv(file)
    needs_visa = df_csv.filter(
        (pl.col("Passport") == country1) | (pl.col("Passport") == country2)
    ).with_column(
        pl.col("Requirement")
        .str.contains(r"required|covid|e\-visa|arrival")
        .alias("needs_visa")
    )

    country_1_visas = needs_visa.filter(pl.col("Passport") == country1)
    country_2_visas = needs_visa.filter(pl.col("Passport") == country2)

    total = country_1_visas.join(country_2_visas, on="Destination")
    f = total.filter(
        (pl.col("needs_visa") == True) & (pl.col("needs_visa_right") == False)
    )

    return f.collect()


print(get_visa_countries("VEN", "ARG"))
