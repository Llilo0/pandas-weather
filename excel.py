import pandas as pd
import openpyxl
from pandas import value_counts
import os

# products = [
#     {
#         "nazwa":"Pomidory",
#         "cena":20,
#         "kraj": "PL"
#     },
#     {
#         "nazwa":"Jabłka",
#         "cena": 10,
#         "kraj":"FR"
#     },
#     {
#         "nazwa":"Wiśnie",
#         "cena": 10,
#         "kraj":"PL"
#     }
# ]
# def create_excel(data):
#     df = pd.DataFrame(data)
#     # df["czas"]  = "01-01-1970 12:12:12"
#     # filtered = df[df["cena"]<15]
#     # only_nazwa = df["nazwa"]
#     # sorted = df.sort_values(by="cena",ascending=True)
#     # countries = df["kraj"].unique()
#     # group_by_country = df["kraj"].value_counts().reset_index()
#     # group_by_country.columns = ["kraj","liczba"]
#     #
#     #
#     # # df.to_excel("testowy.xlsx",index=False)
#     # # df.to_csv("plik1.csv")
#     # # df.to_json("zakupy.json")
#     # # df.to_html("sklep.html")
#
#
# # create_excel(products)
#
#
# def read_excel():
#     data_one = pd.read_excel("testowy.xlsx")
#     data_two = pd.read_json("zakupy.json")
#     df = pd.concat([data_one,data_two])
#     print(df)
#
# # read_excel()

def append_to_excel(new_data):

    df_new = pd.DataFrame([new_data])

    if os.path.exists("dane_pogodowe.xlsx"):
        df_existing = pd.read_excel("dane_pogodowe.xlsx")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    else:
        df_combined = df_new

    df_combined.to_excel("dane_pogodowe.xlsx", index=False)



