class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        mini = float('inf')  # Initialize the minimum length as infinite
        current_sum = 0  # To store the sum of the current window
        start = 0  # Left boundary of the window

        for end in range(n):
            current_sum += arr[end]

            # When the current sum becomes greater than x, we try to shrink the window
            while current_sum > x:
                mini = min(mini, end - start + 1)  # Update the minimum length
                current_sum -= arr[start]  # Shrink the window from the left
                start += 1

        # If no subarray was found, return 0; otherwise, return the minimum length
        return mini if mini != float('inf') else 0
