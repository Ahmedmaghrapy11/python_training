def birthdayCakeCandles(arr):
    
    tallestCandle = max(arr)
    tallestCandles = 0
    
    for candle in arr:
        if candle == tallestCandle:
            tallestCandles += 1
    
    return tallestCandles

print(birthdayCakeCandles([4,4,4,4]))