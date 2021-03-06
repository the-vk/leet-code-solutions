using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    private int max = Int32.MinValue;
    
    public int MaxPathSum(TreeNode root) {
        MaxGain(root);
        return max;
    }
    
    private int MaxGain(TreeNode root) {        
        if (root == null) return 0;
        
        var left = Math.Max(MaxGain(root.left), 0);
        var right = Math.Max(MaxGain(root.right), 0);
        var priceNewPath = left + root.val + right;
        
        max = Math.Max(priceNewPath, max);
        
        return root.val + Math.Max(left, right);
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(16, new []{9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6});
    }

    private static void Test(int expected, int?[] tree)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.CountSquares(ReadTreeNodeInput(tree));
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