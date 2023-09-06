def find_outlier(integers):
    odd = []
    even = []
    
    for i in integers:
        odd.append(i) if i % 2 != 0 else even.append(i)
    
    return odd[0] if len(odd) == 1 else even[0]