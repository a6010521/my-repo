import pandas as pd
import csv
import os


df = pd.read_csv('C:\\Users\\Tibame\\Desktop\\my-repo\\read\\票房資料匯出年票房 2025-01.csv')
print(df)

excel_file = '2025_1_年票房.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')
print('儲存成功')

if os.path.exists(excel_file):
        print(f"Excel 檔案已成功儲存至：{excel_file}")
else:
    print("Excel 儲存失敗，請檢查路徑或權限。")
