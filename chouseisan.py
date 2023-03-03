import datetime
import jpholiday

day = {0:'月', 1:'火', 2:'水', 3:'木', 4:'金', 5:'土', 6:'日'}

def main():

    """
    変数
        ---------------------------------------------------------------------------------------------------------
        name                 : description                                                           : type
        ---------------------------------------------------------------------------------------------------------
        input_date           : ユーザが入力した日付 (ex: 20210801)                                   : string
        slashed_date         : ユーザが入力した日付をスラッシュ区切りに変換したもの (ex: 2021/08/01) : string
        dt_slashed_date      : ユーザが入力した日付を datetime 型に変換したもの                      : datetime
        dt_monday            : ユーザが入力した日付の直前の月曜日 (2021/08/01 の場合は 2021/07/26)   : datetime
        monday               : ユーザが入力した日付の直前の月曜日を string 型に変換したもの          : string
        dt_date              : 日付が datetime 型で格納されている                                    : datetime
        consecutive_holidays : 連休の週かどうか (連休の週なら True)                                  : bool
        date                 : 日付が string 型で格納されている配列 (moday = ['2021', '08', '01'])   : array
        day                  : 添字と曜日が格納されている辞書 (上にいる)                             : dictionary
        ---------------------------------------------------------------------------------------------------------
    """

    # 開始日時の入力
    input_date = input('スタート日時 (例 20210801): ')

    # 日付をスラッシュ区切りに変換
    slashed_date = f'{input_date[:4]}/{input_date[4:6]}/{input_date[6:]}'

    # スラッシュ区切りの日付を datetime 型に変換
    dt_slashed_date = datetime.datetime.strptime(slashed_date, '%Y/%m/%d')

    # 入力した日付の直前にある月曜日を探す
    # dt_slashed_date から、月曜日からずれている日数分を引くことで、月曜日を探せる (月曜日のときは dt_monday.weekday() = 0)。
    dt_monday = dt_slashed_date - datetime.timedelta(days = dt_slashed_date.weekday())

    # datetime 型から string 型へ変換
    monday = dt_monday.strftime('%Y-%m-%d').split('-')

    # 火水休みの週は True
    consecutive_holidays = ((int(monday[2]) - 1) // 7 + 1) % 2 == 0

    # 月曜日が祝日なら
    if jpholiday.is_holiday(dt_monday):

        # 祝日なので営業日であることを表示
        print("-----\n月曜日が祝日なので営業日です。\n-----")

        # 連休の週であることを表示
        if consecutive_holidays == True:
            print("-----\n火曜日と水曜日がお休みです。\n-----")

        # datetime 型から string 型へ変換
        monday = dt_monday.strftime('%Y-%m-%d').split('-')

        # chouseisan 用に表示
        print(f'{int(monday[1])}/{int(monday[2])}(月) 昼')
        print(f'{int(monday[1])}/{int(monday[2])}(月) 夜')

        # 1 日足す
        dt_monday += datetime.timedelta(days = 1)

        # datetime 型の日付として代入
        dt_date = dt_monday

        # 2 ~ 7 (水曜日 ~ 日曜日) までループ
        for i in range(2, 7):

            # 水曜日かつ連休の週のときは何も表示しない
            if i == 2 and consecutive_holidays == True:
                dt_date += datetime.timedelta(days = 1)

            # 連休の週ではないとき
            else:

                # 1 日足す
                dt_date += datetime.timedelta(days = 1)

                # datetime 型から string 型へ変換
                date = dt_date.strftime('%Y-%m-%d').split('-')

                # chouseisan 用に表示
                print(f'{int(date[1])}/{int(date[2])}({day[i]}) 昼')
                print(f'{int(date[1])}/{int(date[2])}({day[i]}) 夜')

    # 祝日でなければ
    else:

        # datetime 型の日付として代入
        dt_date = dt_monday

        # 1 ~ 7 (火曜日 ~ 日曜日) までループ
        for i in range(1, 7):

            # 火曜日かつ連休の週のときは何もしない
            if i == 1 and consecutive_holidays == True:
                print("-----\n月曜日と火曜日がお休みです。\n-----")
                dt_date += datetime.timedelta(days = 1)

            # 連休の週ではないとき
            else:

                # 1 日足す
                dt_date += datetime.timedelta(days = 1)

                # datetime 型から string 型に変換
                date = dt_date.strftime('%Y-%m-%d').split('-')

                # chouseisan 用に表示
                print(f'{int(date[1])}/{int(date[2])}({day[i]}) 昼')
                print(f'{int(date[1])}/{int(date[2])}({day[i]}) 夜')

if __name__ == "__main__":
    main()