#!/bin/bash
# Builds ixjournal (PySide6) for Linux and assembles a self-contained
# dist-lin64/jour_main/ folder.
#
# Prerequisites: system python3 + PySide6 + requests + Pillow + pyinstaller
# (on this machine PySide6 is the Arch package, linked against the system
# Qt6 - that's why PyInstaller's PySide6 hook picks up libqsqlibase.so and
# its libfbclient.so.2 dependency automatically here, unlike build_win64.sh
# where fbclient.dll has to be added by hand).
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

DIST_DIR="$PROJECT_DIR/dist-lin64/jour_main"

echo "==> Сборка (PyInstaller)"
rm -rf "$PROJECT_DIR/build-lin64" "$PROJECT_DIR/dist-lin64"
pyinstaller --noconfirm --onedir --console \
    --name jour_main \
    --distpath "$PROJECT_DIR/dist-lin64" \
    --workpath "$PROJECT_DIR/build-lin64" \
    --add-data "image:image" \
    jour_main.py

echo "==> Докладываю ресурсы, которые PyInstaller не резолвит сам"
# image/ резолвится в коде относительно рабочей директории, а не
# sys._MEIPASS - в onedir-режиме PyInstaller 6.x кладёт данные в
# _internal/, поэтому копируем ещё и рядом с исполняемым файлом.
cp -r "$PROJECT_DIR/image" "$DIST_DIR/image"

if [ ! -f "$DIST_DIR/_internal/PySide6/Qt/plugins/sqldrivers/libqsqlibase.so" ]; then
    echo "Предупреждение: не найден драйвер Firebird (libqsqlibase.so) в сборке -" >&2
    echo "подключение к БД (QSqlDatabase::addDatabase('QIBASE')) работать не будет." >&2
fi

echo "==> Done: $DIST_DIR ($(du -sh "$DIST_DIR" | cut -f1))"
