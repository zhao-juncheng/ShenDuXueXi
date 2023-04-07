# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.read_excel("1.xlsx")
df2 = pd.read_excel("2.xlsx")

result_file = "r2.xlsx"
writer = pd.ExcelWriter(result_file, engine='openpyxl')

print("合并开始")
df_outer = pd.merge(df1, df2, how='outer', on=['Stkcd','ShortName', 'Accper',])
df_outer.to_excel(writer, sheet_name="outer方式merge", index=False)
print("合并结束")

writer.save()