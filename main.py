def boxPacking(boxes):
    # Step 1: Sort each box's dimensions in ascending order
    boxes = [tuple(sorted(box)) for box in boxes]
    
    # Step 2: Sort the list of boxes based on the first dimension, then second, then third
    boxes.sort()

    # Step 3: Apply Longest Increasing Subsequence (LIS) on the sorted boxes
    n = len(boxes)
    dp = [1] * n  # Initialize dp array where dp[i] will store the length of the longest sequence ending at box i
    
    for i in range(1, n):
        for j in range(i):
            if (boxes[i][0] > boxes[j][0] and
                boxes[i][1] > boxes[j][1] and
                boxes[i][2] > boxes[j][2]):
                dp[i] = max(dp[i], dp[j] + 1)

    # The result is the maximum value in dp
    return max(dp)
