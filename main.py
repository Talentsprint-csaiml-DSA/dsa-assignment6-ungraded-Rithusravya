def can_pack(box1, box2):
    # Check if box1 can fit inside box2 in all dimensions
    return all(x <= y for x, y in zip(box1, box2))

def box_packing(n, boxes):
    # Sort the boxes by dimensions (sort each box's dimensions first)
    sorted_boxes = [tuple(sorted(box)) for box in boxes]
    sorted_boxes.sort()

    # DP array to store the max number of boxes that can be packed up to the i-th box
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # If the i-th box can be packed inside the j-th box
            if can_pack(sorted_boxes[j], sorted_boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    # The result will be the maximum value in the dp array
    return max(dp)
