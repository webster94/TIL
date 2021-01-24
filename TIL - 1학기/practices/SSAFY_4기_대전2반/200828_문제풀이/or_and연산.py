def true():
    print("참을 리턴")
    return True

def false():
    print("거짓을 리턴")
    return False

# if true() and true():
#     print("실행")
#
# if true() and false():
#     print("실행")
#
# if false() and true():
#     print("실행")
#
# if false() and false():
#     print("실행")


# if true() or true():
#     print("실행")
#
# if true() or false():
#     print("실행")
#
# if false() or true():
#     print("실행")

# if false() or false():
#     print("실행")

visited = [[1,1,1],
           [1,1,1],
           [1,1,1]]

r = 1
c = 2

#사방 탐색을 하려고 하는데 이때 오른쪽을 확인하려고 함.
nr = r + 0
nc = c + 1
# if 0<= nr < 2 and 0 <= nc <2 and visited[nr][nc] == 0:
#     print("실행")

if visited[nr][nc] == 0and 0<= nr < 2 and 0 <= nc <2:
    print("실행")

