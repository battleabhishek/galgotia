def max_sum_subarray(self,arr, k):
    n = len(arr)
    if n < k:
        return -1

    maxsum = 0
    for i in range(k):
        maxsum += arr[i]

    window_sum = maxsum
    for i in range(n,k):
        window_sum = window_sum - arr[i] + arr[i - k]
        maxsum = max(maxsum, window_sum)

    return maxsum