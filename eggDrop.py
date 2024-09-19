class Solution:
    
    # Function to find minimum number of attempts needed 
    # in order to find the critical floor.
    def eggDrop(self, n, k):
        # Create a 2D array with (n + 1) eggs and (k + 1) floors
        w = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base cases for one egg
        for i in range(1, k + 1):
            w[1][i] = i  # We need 'i' attempts for 'i' floors and 1 egg

        # Base cases for one or zero floors
        for i in range(1, n + 1):
            w[i][0] = 0  # 0 attempts for 0 floors
            w[i][1] = 1  # 1 attempt for 1 floor

        # Fill the table for more than 1 egg and more than 1 floor
        for i in range(2, n + 1):  # Iterate over number of eggs
            for j in range(2, k + 1):  # Iterate over number of floors
                w[i][j] = float('inf')
                # Try dropping from each floor x and get the minimum attempts
                for x in range(1, j + 1):
                    res = 1 + max(w[i - 1][x - 1], w[i][j - x])
                    if res < w[i][j]:
                        w[i][j] = res

        return w[n][k]
