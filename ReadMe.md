# このソフトウェアについて

Pythonで国際化した（ソースコードと国際化用ファイルのディレクトリを分けた）。

`Hello World!!`を`こんにちは世界！`へ置き換える等。

# 参考

* http://d.hatena.ne.jp/fgshun/20100319/1269004530
* https://docs.python.jp/3/library/gettext.html
* https://ja.wikipedia.org/wiki/ISO_639-1%E3%82%B3%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7

# 実行

```sh
$ python main.py 
こんにちは世界！
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: de
Willkommen bei i18n!
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: en  
Welcome to i18n !
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: ja
ようこそ i18n へ！
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: 
```

# ファイル構成

* src/
    * main.py
* res/
    * i18n/
        * languages/
            * de/
                * LC_MESSAGES/
                    * hello.mo
            * en/
                * LC_MESSAGES/
                    * hello.mo
            * ja/
                * LC_MESSAGES/
                    * hello.mo
        * hello_de.po
        * hello_en.po
        * hello_ja.po
        * messages.pot
        * msgfmt.py
        * pygettext.py

# 手順

1. コードを書く
1. 以下のファイルを入手する
    * [pygettext.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/pygettext.py)
    * [msgfmt.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/msgfmt.py)
1. `$ python pygettext.py main.py`で`messages.pot`ファイルが出力される
1. `messages.pot`ファイルをコピーして`hello_ja.po`にリネームする
1. `hello_ja.po`の項目を任意に埋める（`msgstr ""`を`msgstr "こんにちは世界！"`とする等）
1. `$ python msgfmt.py hello_ja.po`で`hello_ja.mo`ファイルが出力される
1. `./ja/LC_MESSAGES/hello.mo`に配置する（ファイル名から`_ja`をとる（`gettext.install()の第一引数と同一名にする`））
1. `$ python main.py`を実行して`Hello World !!`でなく`こんにちは世界！`と表示されたら成功

## main.py

main.py
```python
#!python3.6
import gettext
import pathlib
langPath = str(pathlib.Path('../res/i18n/languages').resolve())
gettext.install('hello', langPath)
print(_('Hello World !!'))

langs = ['ja', 'en', 'de']
lang = 'ja'
while lang:
    print(f'言語コードを入力してください(未入力+Enterで終了) {langs}: ', end='')
    lang = input()
    if lang not in langs: continue
    l = gettext.translation('hello', langPath, languages=[lang])
    l.install()
    print(_('Welcome i18n !!'))
```
```sh
$ python main.py 
こんにちは世界！
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: de
Willkommen bei i18n!
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: en  
Welcome to i18n !
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: ja
ようこそ i18n へ！
言語コードを入力してください(未入力+Enterで終了) ['ja', 'en', 'de']: 
```

* domain: `hello.mo`ファイルと同じ名前にする(拡張子をとる)
* localedir: `(ここで指定したディレクトリ)/ja/LC_MESSAGES/hello.mo`
* fallback: moファイルが見つからない場合そのまま実行する
* `_(...)`で囲った文字列が翻訳対象となる

poファイルのヘッダ部分は[こちら](http://www.gnu.org/software/gettext/manual/gettext.html#Header-Entry)を参照。

## hello_ja.po

`msgstr ""`の部分をそれぞれ翻訳して埋める。以下、日本語用ファイルの場合。

```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) 2017 ytyaru
# FIRST AUTHOR <EMAIL@ADDRESS>, 2017.
#
msgid ""
msgstr ""
"Project-Id-Version: 1.0\n"
"POT-Creation-Date: 2017-09-15 08:30+0900\n"
"PO-Revision-Date: 2017-09-15 08:31+0900\n"
"Last-Translator: ytyaru <EMAIL@ADDRESS>\n"
"Language-Team: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: pygettext.py 1.5\n"

#: main.py:5
msgid "Hello World !!"
msgstr "こんにちは世界！"

#: main.py:15
msgid "Welcome i18n !!"
msgstr "ようこそ i18n へ！"
```

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
* [pygettext.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/pygettext.py)
* [msgfmt.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/msgfmt.py)

# ライセンス

* https://sites.google.com/site/michinobumaeda/programming/pythonconst

Library|License|Copyright
-------|-------|---------
http://code.activestate.com/recipes/65207/|[PSF](https://ja.osdn.net/projects/opensource/wiki/licenses%2FPython_Software_Foundation_License)|Copyright (c) 2001 Python Software Foundation; All Rights Reserved
