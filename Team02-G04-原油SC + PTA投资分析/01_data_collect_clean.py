# -*- coding: utf-8 -*-
import akshare as ak
import pandas as pd
import numpy as np
import os
import time
import warnings
warnings.filterwarnings('ignore')

# ====================== 配置 ======================
START_DATE = "20100101"
END_DATE   = "20251231"

# 相对路径，全部在当前文件夹 Team02-G04-原油SC + PTA投资分析/ 内
BASE_DIR   = "./"
DIR_RAW    = os.path.join(BASE_DIR, "data_raw")
DIR_CLEAN  = os.path.join(BASE_DIR, "data_clean")

os.makedirs(DIR_RAW, exist_ok=True)
os.makedirs(DIR_CLEAN, exist_ok=True)

# ====================== 获取数据 ======================
def fetch(symbol, path):
    if os.path.exists(path):
        print(f"Load from cache: {path}")
        return pd.read_csv(path)

    df = None
    for attempt in range(3):
        try:
            df = ak.futures_main_sina(symbol=symbol, start_date=START_DATE, end_date=END_DATE)
            break
        except:
            time.sleep(2)
    if df is None:
        raise Exception(f"Failed to fetch {symbol}")

    df.to_csv(path, index=False, encoding="utf-8")
    print(f"Saved: {path}")
    return df

sc_raw  = fetch("SC0", os.path.join(DIR_RAW, "sc_raw.csv"))
pta_raw = fetch("TA0", os.path.join(DIR_RAW, "pta_raw.csv"))

# ====================== 清洗数据 ======================
def process(df, prefix):
    df.columns = ["date","open","high","low","close","volume","amount","oi"]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna().drop_duplicates("date")
    df = df[df["close"] > 0].sort_values("date").reset_index(drop=True)

    df["ret"]    = np.log(df["close"] / df["close"].shift(1))
    df["vol20"]  = df["ret"].rolling(20).std()

    new_cols = []
    for c in df.columns:
        if c != "date":
            new_cols.append(f"{prefix}_{c}")
        else:
            new_cols.append("date")
    df.columns = new_cols
    return df

sc_clean  = process(sc_raw,  "SC")
pta_clean = process(pta_raw, "PTA")

# ====================== 合并输出 ======================
final = pd.merge(sc_clean, pta_clean, on="date", how="inner").dropna()
final_path = os.path.join(DIR_CLEAN, "sc_pta_final.csv")
final.to_csv(final_path, index=False, encoding="utf-8")

print("\n===== DONE =====")
print(f"Total rows: {len(final)}")
print(f"Missing values: {final.isnull().sum().sum()}")
print(f"Output: {final_path}")