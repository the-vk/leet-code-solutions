using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int NumEquivDominoPairs(int[][] dominoes) {
        var seen = new Dictionary<(int,int), int>();
        var pairs = 0;
        for (var i = 0; i < dominoes.Length; ++i) {
            var d = dominoes[i];
            var tuple = (Math.Min(d[0], d[1]), Math.Max(d[0], d[1]));
            if (seen.ContainsKey(tuple)) {
                pairs += seen[tuple];
                seen[tuple] += 1;
            } else {
                seen[tuple] = 1;
            }
        }
        return pairs;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(1, new[]{new[]{1,2}, new[]{1,2}});
    }

    private static void Test(int expected, int[][] dominoes)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.NumEquivDominoPairs(dominoes);
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