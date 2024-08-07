def find_peak_element(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return None


arr = [1,2,3]
print("Peak element:", find_peak_element(arr))

