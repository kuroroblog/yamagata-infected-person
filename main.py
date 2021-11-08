# csv参考文献 : https://www3.nhk.or.jp/news/special/coronavirus/data/
import csv
import datetime

# 集計する都道府県を格納する。
target_pref = '山形県'
# 集計する期間情報を格納する。
target_from_month = '2021/4/1'
target_to_month = '2021/9/30'
from_month = 4
to_month = 9

# 感染者数を月ごとに格納する変数。
data = []
for i in range(to_month - from_month + 1):
    data.append([])

# 文字列の日付をdatetime型へ変換する。
# 参考　: https://gist.github.com/himoatm/e6a189d9c3e3c4398daea7b943a9a55d
# 参考 : https://techacademy.jp/magazine/33867
# 参考 : https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-format-codes
def string_to_datetime(string):
    return datetime.datetime.strptime(string, "%Y/%m/%d")

# 参考 : https://note.nkmk.me/python-csv-reader-writer/
with open('data.csv') as f:
    reader = csv.reader(f)
    # ヘッダー情報は無視する。
    # 参考 : https://techacademy.jp/magazine/32653
    next(reader)
    for row in reader:
        date_from_csv = row[0]
        pref_name_from_csv = row[2]
        infected_person_from_csv = int(row[3])

        # 山形県以外の情報は無視する。
        if pref_name_from_csv != target_pref:
            continue

        # 2021/4/1~2021/9/30までのデータのみを取得する。
        if string_to_datetime(target_from_month) <= string_to_datetime(date_from_csv) and string_to_datetime(target_to_month) >= string_to_datetime(date_from_csv):
            # month : 2021/n/mmのnを表す。
            month = int(date_from_csv[5])
            data[month - from_month].append(infected_person_from_csv)

total = []
avg = []
for d in data:
    # 参考 : https://docs.python.org/ja/3/library/functions.html?highlight=sum#sum
    tmp = sum(d)
    # 参考 : https://www.javadrive.jp/python/function/index4.html
    tmp_len = len(d)
    total.append(tmp)
    avg.append(tmp / tmp_len)

print(total)
print(avg)
