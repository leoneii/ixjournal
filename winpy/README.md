# winpy/

Разовая настройка Windows-Python под Wine (используется `../build_win64.sh`).
Ставится один раз, в `~/.wine`, а не в этот каталог - здесь только заметка.

```bash
# скачать python-3.11.9-amd64.exe с python.org, затем:
WINEDEBUG=-all wine python-3.11.9-amd64.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 SimpleInstall=1

WINPY="/home/leone/.wine/drive_c/users/leone/Local Settings/Application Data/Programs/Python/Python311/python.exe"
wine "$WINPY" -m pip install --upgrade pip
wine "$WINPY" -m pip install PySide6 requests Pillow pyinstaller
```

Проверка: `wine "$WINPY" -c "import PySide6; print(PySide6.__version__)"`.
