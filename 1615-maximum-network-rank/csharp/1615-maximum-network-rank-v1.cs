using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        if (n == 0) return 0;
        
        var cityRank = new int[n];
        var ajm = new bool[n][];
        
        for (var i = 0; i < n; ++i) {
            ajm[i] = new bool[n];
        }
        
        foreach (var r in roads)
        {
            var f = r[0];
            var t = r[1];
            ajm[f][t] = true;
            ajm[t][f] = true;
            cityRank[f] += 1;
            cityRank[t] += 1;
        }

        var networkRank = 0;
        for (var i = 0; i < n; ++i) {
            for (var j = i+1; j < n; ++j) {
                var pairRank = cityRank[i] + cityRank[j];
                if (ajm[i][j]) pairRank -= 1;
                networkRank = Math.Max(networkRank, pairRank);
            }
        }
        
        return networkRank;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(4, 4, new int[][] {new[]{0,1}, new[]{0,3}, new []{1,2}, new[]{1,3}});
    }

    private static void Test(int expected, int n, int[][] roads)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.MaximalNetworkRank(n, roads);
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