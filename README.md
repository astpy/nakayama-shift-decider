# nakayama-shift-decider

## REQUIREMENTS

- Python 3
- pip

## HOW TO INSTALL

### Debian / Ubuntu

下のコマンドを実行することで、インストールができる。

```sh
sudo apt install python3 python3-pip 
pip3 install pandas numpy
```

### Windows

1. [ここ](https://www.python.org/downloads/windows/) にある `Latest Python 3 Release` をクリック
2. ページの下の方にある `Files` から`Windows installer (64-bit)` をクリックし、ダウンロード。
3. `python ~ .exe` ファイルがダウンロードされるので、実行し `Python 3` と `pip` をインストール。
4. `powershell` を開いて `python3` と入力し、Python が無事にインストールできているかを確認。
5. `pip install pandas numpy` もしくは `pip3 install pandas numpy` を実行。インストールされればOK。

### Mac

`Homwbrew` をインストールした後、`python 3` をインストール。

## HOW TO USE

- [調整さん](https://chouseisan.com)でシフトの希望を募る
- シフト希望が揃ったら、調整さんのページから CSV ファイルをダウンロードする。
- python ファイルと CSV ファイルを同じディレクトリ (フォルダ) 内に保存する。
- `decider.py` を実行
  - 実行は `python3 decider.py`
- いくつシフトを作成するか、その日は何人バイトを入れるかを決める。
- シフトが生成される。
  - おそらく狙った通りのシフトは出ないので、近いやつを採用して手直しするのが実用的。