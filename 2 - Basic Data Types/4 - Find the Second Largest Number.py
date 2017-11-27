if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    l =list(arr)
    mx = max(l)
    while max(l)== mx:
        l.remove(mx)
    print max(l)
    
    
