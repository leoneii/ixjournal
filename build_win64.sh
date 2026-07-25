#!/bin/bash
# Builds ixjournal (PySide6) for Windows and assembles a self-contained
# dist/jour_main/ folder.
#
# Prerequisites (one-time setup, not done by this script):
#   - A genuine Windows Python installed under Wine (see winpy/README.md),
#     with PySide6, requests, Pillow, pyinstaller pip-installed into it.
#   - win-firebird/extracted/fbclient.dll (fbclient.dll for the Firebird
#     Qt SQL driver - shared with ix_susn, see ixsusndev/win-firebird)
#
# PyInstaller cannot cross-compile: it has to run on (or under Wine
# emulating) the target platform so PySide6's compiled .pyd extensions get
# bundled correctly. Hence running PyInstaller itself through Wine here,
# exactly like the Wine-hosted Qt/MinGW toolchain used for ix_susn.
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

WINPY="/home/leone/.wine/drive_c/users/leone/Local Settings/Application Data/Programs/Python/Python311/python.exe"
FBCLIENT="$PROJECT_DIR/../ixsusndev/win-firebird/extracted/fbclient.dll"
DIST_DIR="$PROJECT_DIR/dist/jour_main"

if [ ! -f "$WINPY" ]; then
    echo "Не найден Wine-Python: $WINPY" >&2
    echo "См. winpy/README.md - нужно один раз поставить python-3.11.9-amd64.exe под wine" >&2
    exit 1
fi

echo "==> Сборка (PyInstaller под Wine)"
rm -rf "$PROJECT_DIR/build/jour_main" "$DIST_DIR"
WINEDEBUG=-all wine "$WINPY" -m PyInstaller --noconfirm --onedir --windowed \
    --name jour_main \
    --add-data "image;image" \
    jour_main.py

echo "==> Докладываю ресурсы, которые PyInstaller не резолвит сам"
# image/ резолвится в коде относительно рабочей директории, а не
# sys._MEIPASS - в onedir-режиме PyInstaller 6.x кладёт данные в
# _internal/, поэтому копируем ещё и рядом с exe.
cp -r "$PROJECT_DIR/image" "$DIST_DIR/image"

# fbclient.dll нужен Qt-плагину qsqlibase.dll (QSqlDatabase.addDatabase
# ('QIBASE')) - сам PyInstaller его не находит, т.к. в Wine-окружении
# Firebird-клиент не установлен.
if [ -f "$FBCLIENT" ]; then
    cp "$FBCLIENT" "$DIST_DIR/"
else
    echo "Предупреждение: не найден $FBCLIENT - fbclient.dll не добавлен" >&2
fi

echo "==> Done: $DIST_DIR ($(du -sh "$DIST_DIR" | cut -f1))"
