# 2022-10-06
# This script is updated because chouseisan changed specifications of CSV.

import pandas as pd
import csv
import random


num_of_people = []
flag = 0


def main():

    chouseisan = []

    # # chouseisan が Shift-JIS から UTF-8 になったぞ！！
    # # わざわざ shift.csv 変換してたが変換しなくていいようになったので修正
    # with open('./shift.csv', 'r') as f:
    with open('./chouseisan.csv', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            # #chouseisan.append(row[:-1])
            chouseisan.append(row)

    # 日付 + 名前のリスト
    names = chouseisan[2]
    # 希望日の2次元配列
    wish_matrix = chouseisan[3:-1]

    # 希望なしの削除
    for i, row in enumerate(wish_matrix):
        for j, val in enumerate(row):
            # 日程はパス
            if j == 0:
                pass
            else:
                # ○ と × を True と False に置き換える
                # # アプデで○の文字コードが変わったっぽいので修正
                if val == '◯':
                    wish_matrix[i][j] = True
                else:
                    wish_matrix[i][j] = False

    # pandas の形式に変換
    df_wish_matrix = pd.DataFrame(wish_matrix, columns=names)

    del_names = []

    for i in range(len(df_wish_matrix.iloc[0, :])):
        # 列で切り出す
        is_possible = df_wish_matrix.iloc[:, i]
        # 勤務日の希望がある場合(列の中にTrueがある)
        if any(is_possible):
            pass
        # 勤務日の希望がない場合(列の中にTrueがない)
        else:
            # 削除用名前リストに追加
            del_names.append(is_possible.name)
            # names から削除
            names.remove(is_possible.name)

    # names[0] = '日程' なので names を日付なしに修正
    names.pop(0)

    # 希望なしの人を予め削除
    df_wish_matrix.drop(del_names, axis=1, inplace=True)
    print(f'希望なし : {del_names}')

    # shifts を numpy 配列に変換したのちに配列に再変換
    shifts = df_wish_matrix.to_numpy().tolist()

    # 日付のみ抽出
    dates = []
    for shift in shifts:
        # 抽出しshiftからは削除する
        dates.append(shift.pop(0))
    
    # ほしい人数の確認(1回のみの実行)
    global flag
    global num_of_people
    if(flag == 0):
        for i, date in enumerate(dates):
            # 希望者を出力し枠をいくつ用意するかを入力
            tmp = int(input(f'{date} (最大 {shifts[i].count(True)}) : '))
            num_of_people.append(tmp)
        flag = 1
        print('\n')

    # シフトの確定
    while True:
        # 優先度を振るためのスコアとシフトの確定
        points = [0] * len(shifts[0])
        # 1人しか希望を出していないところを探して埋める
        decided = []
        for i in range(len(shifts)):
            # 出れる人たちの名前のインデックス
            possible_person_index = []
            for j in range(len(shifts[i])):
                if shifts[i][j] == True:
                    possible_person_index.append(j)
            how_many = len(possible_person_index)
            # 1人しか希望が出ていない日がある場合
            if how_many == 1:
                # 先に決めておく
                # 日付
                decided.append(dates[i])
                # 名前
                decided.append([names[possible_person_index[0]]])
                # pointsの加算
                points[possible_person_index[0]] += 1
            # 2人以上の場合
            else:
                decided_names = []
                # 設定した枠の数だけ勤務者を選出
                for k in range(num_of_people[i]):
                    rand_num = random.randint(0, len(possible_person_index) - 1)
                    emp_index = possible_person_index.pop(rand_num)
                    decided_names.append(names[emp_index])
                    # pointsの加算
                    points[emp_index] += 1
                # シフト確定用配列 decided に append
                # 日付
                decided.append(dates[i])
                # 名前
                decided.append(decided_names)
        # max_pointの再計算
        max_point = max(points)
        # 勤務なし or 枠の 1/3 を超える人がいる場合は再実行
        if not 0 in points and max_point < (sum(num_of_people) / 3):
            break    
    
    # 確認用で出力
    for i in range(0, len(decided), 2):
        print(f'{decided[i]} : {", ".join(decided[i+1])}')
    for i in range(0, len(names)):
        print(f'{names[i]}: {points[i]} / ', end = "")
    print('\n')


if __name__ == '__main__':
    times = int(input("いくつシフト候補を作成しますか？"))
    for i in range(times):
        main()