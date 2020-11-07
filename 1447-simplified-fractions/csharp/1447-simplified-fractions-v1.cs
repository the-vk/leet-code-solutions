using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution {
    public IList<string> SimplifiedFractions(int n) {
        var result = new List<string>();
        for (var den = 2; den <= n; den++) {
            for (var num = 1; num < den; num++) {
                var skip = false;
                for (var f = 2; f <= num; f++) {
                    if (num % f == 0 && den % f == 0) {
                        skip = true;
                        break;
                    }
                }
                if (!skip) {
                    result.Add($"{num}/{den}");
                }
            }
        }
        return result;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(null, 4);
    }

    private static void Test(IList<string> expected, int n)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.SimplifiedFractions(n);
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