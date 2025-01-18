from pathlib import Path
import pandas as pd
import json

def json_load():
    readDir = Path("readjson")
    # 讀取JSON文件
    dfJSON = pd.read_json(readDir/"film.json")
    print(f"dfJSON:\n{dfJSON}")


    df = pd.DataFrame(dfJSON)

# 將 DataFrame 存成 Excel
    excel_file = "movies_data.xlsx"
    df.to_excel(excel_file, index=False)

    print(f"JSON 資料已成功轉存為 Excel 檔案：{excel_file}")




