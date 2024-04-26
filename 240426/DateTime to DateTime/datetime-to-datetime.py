# 입력
a, b, c = map(int, input().split())

# 시작 시간과 종료 시간 간의 분 차이 계산
start_time = 11 * 24 * 60 + 11 * 60 + 11  # 시작 시간을 분으로 변환
end_time = a * 24 * 60 + b * 60 + c  # 종료 시간을 분으로 변환
diff = end_time - start_time

# 결과 출력
if diff < 0:
    print(-1)
else:
    print(diff)