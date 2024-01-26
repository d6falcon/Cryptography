import cProfile

def profile(n):
    if n <= 1:
        return n
    else:
        return profile(n-1)*n
    
def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(profile(10))")