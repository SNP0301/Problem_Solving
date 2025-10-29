#!/usr/bin/env bash
set -euo pipefail

# 고정 파일명 사용 (요구사항)
MAIN=main.cpp
IN=sample_input.txt
SOL=solution.cpp
OUT="${OUT:-main}"   # 실행파일 이름(원하면 OUT=app ./run.sh 식으로 바꿀 수 있음)

# 빌드
g++ -std=c++17 -O2 -Wall -Wextra -o "$OUT" "$MAIN" "$SOL"

# 실행 (input.txt 있으면 리디렉션)
if [[ -f "$IN" ]]; then
  "./$OUT" < "$IN"
else
  "./$OUT"
fi
