using System;

public class Solution
{
    // Function to find minimum number of attempts needed in 
    // order to find the critical floor.
    public int EggDrop(int n, int k)
    {
        // Create a 2D array to store the results
        int[,] w = new int[n + 1, k + 1];

        // Initialize the base cases
        for (int i = 1; i <= k; i++)
        {
            w[1, i] = i;
        }
        
        for (int i = 1; i <= n; i++)
        {
            w[i, 0] = 0;
            w[i, 1] = 1;
        }

        // Fill the table
        for (int i = 2; i <= n; i++)
        {
            for (int j = 2; j <= k; j++)
            {
                w[i, j] = int.MaxValue;
                for (int x = 1; x <= j; x++)
                {
                    int res = 1 + Math.Max(w[i - 1, x - 1], w[i, j - x]);
                    if (res < w[i, j])
                    {
                        w[i, j] = res;
                    }
                }
            }
        }

        return w[n, k];
    }
}

// Example usage
public class Program
{
    public static void Main()
    {
        Solution sol = new Solution();
        int n = 2; // Number of eggs
        int k = 10; // Number of floors
        Console.WriteLine("Minimum number of attempts needed: " + sol.EggDrop(n, k));
    }
}
