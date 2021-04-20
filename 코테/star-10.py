# def fill_star(size,x,y):
#     if size == 1:
#         stars[y][x] = '*'
#     else:
#         next_size = size //3
#         for dy in range(3):
#             for dx in range(3):
#                 if dx == 1 and dy ==1 : continue
#                 fill_star(next_size,x + dx * next_size,y + dy * next_size)
#
# N = int(input())
# stars = [[' ' for _ in range(N)] for _ in range(N)]
# fill_star(N,0,0)
# for i in range(N):
#     print(''.join(stars[i]))
#

def fill_star(size,x,y):
    if size == 1:
        stars[y][x] = '*'
    else:
        next_size = size //3
        fill_star(next_size,x + 0 * next_size , y + 0*next_size)
        fill_star(next_size,x + 1 * next_size , y + 0*next_size)
        fill_star(next_size,x + 2 * next_size , y + 0*next_size)
        fill_star(next_size,x + 0 * next_size , y + 1*next_size)
        fill_star(next_size,x + 0 * next_size , y + 2*next_size)
        fill_star(next_size,x + 2 * next_size , y + 2*next_size)
        fill_star(next_size,x + 1 * next_size , y + 2*next_size)
        fill_star(next_size,x + 2 * next_size , y + 1*next_size)

N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]
fill_star(N,0,0)
for i in range(N):
    print(''.join(stars[i]))