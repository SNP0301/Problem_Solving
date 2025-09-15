#!/usr/bin/env bash
set -e

SRC=${1:-main.cpp}    # 1번 인자: 소스파일 (기본 main.cpp)
IN=${2:-input.in}     # 2번 인자: 입력파일 (기본 input.in)
OUT="${SRC%.*}"       # 실행파일 이름: 확장자 제거

g++ -std=c++17 -O2 -Wall -Wextra -o "$OUT" "$SRC"
"./$OUT" < "$IN"