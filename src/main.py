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
