using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution {
    public int CherryPickup(int[][] grid) {
        var memo = new Dictionary<(int,int,int), int>();
        Func<int, int, int, int> dp = null;
        dp = (row, col1, col2) => {
            var key = (row, col1, col2);
            if (memo.ContainsKey(key)) return memo[key];
            var cherries = grid[row][col1];
            if (col1 != col2) cherries += grid[row][col2];
            if (row == grid.Length - 1) {
                memo[key] = cherries;
                return cherries;
            }
            var max = 0;
            for (var i = Math.Max(0, col1-1); i < Math.Min(grid[0].Length, col1+2); i++) {
                for (var j = Math.Max(0, col2-1); j < Math.Min(grid[0].Length, col2+2); j++) {
                    max = Math.Max(max, dp(row+1, i, j));
                }
            }
            cherries += max;
            memo[key] = cherries;
            return cherries;
        };
        return dp(0, 0, grid[0].Length - 1);
    }
}

public static class Program
{
    public static void Main()   
    {
        Test("aacaaca", "aacaacaaca");
        Test("leet", "leetcodeleet");
    }

    private static void Test(string expected, string s)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.LongestPrefix(s);
        if (actual != expected)
        {
            Console.WriteLine($"actual value '{actual}' is not equal to expected value '{expected}'");
        }
        stopwatch.Stop();
        var elapsed = stopwatch.Elapsed.TotalSeconds;
        Console.WriteLine($"elapsed: {elapsed} secs");
    }

    private static TreeNode ReadTreeNodeInput(int?[] input)
    {
        TreeNode root = null;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        var i = 0;
        while (i < input.Length)        
        {
            if (root == null)
            {
                root = new TreeNode(input[i].Value);
                queue.Enqueue(root);
                i++;
            }
            else
            {
                var node = queue.Dequeue();
                var left = input[i];
                var right = input[i+1];
                i += 2;
                if (left.HasValue)
                {
                    node.left = new TreeNode(left.Value);
                    queue.Enqueue(node.left);
                }
                if (right.HasValue)
                {
                    node.right = new TreeNode(right.Value);
                    queue.Enqueue(node.right);
                }
            }
        }
        return root;
    }
}

public class TreeNode 
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) 
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}