def sort(arr, m):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if m == 1:
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif m == 2:
                if arr[j] < arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    
def main():
    iflr = raw_input()
    iflr = int(iflr)
    x = raw_input()
    x = str(x)
    req = x.split(" ")
    bflrs = []
    tflrs = []
    for i in req:
        if int(i) > iflr:
            tflrs.append(int(i))
        else:
            bflrs.append(int(i))
    sort(bflrs, 2)
    sort(tflrs, 1)
    schedule = [iflr] + tflrs + bflrs
    d = 0
    prev = iflr
    for i in range(len(schedule)):
        print schedule[i],
        d += abs(schedule[i] - prev)
        prev = schedule[i]
    print''
    print d
    sort(bflrs, 2)
    sort(tflrs, 2)
    schedule = [iflr] + bflrs + tflrs
    d = 0
    prev = iflr
    for i in range(len(schedule)):
        print schedule[i],
        d += abs(schedule[i] - prev)
        prev = schedule[i]
    print ''
    print d
    
if __name__ == '__main__':
    main()
