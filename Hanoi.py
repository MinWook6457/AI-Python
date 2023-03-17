# 하노이 탑
# 입력 : 옮기려는 원반의 개수 n
# 옮길 원반이 현재 있는 출발점 기둥 from_pos
# 원판을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조 기둥 aux_pos
# 출력 : 원반을 옮기는 순서

# 원반이 n개 일때

# 1. A 기둥에 있는 n-1 개의 원반을 B 기둥으로 옮깁니다.
# 2. A 기둥에 남아 있는 원반중 가장 큰 원반을 C 기둥으로 옯깁니다.
# 3. B 기둥에 있는 n-1개 원반을 C 기둥으로 옮깁니다.

def hanoi(n,from_pos,to_pos,aux_pos) :
    if n == 1 : # 원반 한 개를 옮기는 문제면 그냥 옮김
        print(from_pos, "=>",to_pos)
        return
    
    # 원반 n-1 개를 aux_pos로 이동(to_pos를 보조 기둥으로 사용)
    hanoi(n-1,from_pos,aux_pos,to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos,"=>",to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)
print("n=3")
hanoi(3,1,3,2)



