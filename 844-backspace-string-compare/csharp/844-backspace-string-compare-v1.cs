using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public bool BackspaceCompare(string S, string T) {
        var s = Sanitize(S);
        var t = Sanitize(T);
        return s == t;
    }
    
    private string Sanitize(string s) {
        var sb = new StringBuilder();
        foreach (var c in s) {
            if (c == '#') {
                if (sb.Length > 0) {
                    sb.Remove(sb.Length-1, 1);
                }
            } else {
                sb.Append(c);
            }
        }
        return sb.ToString();
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(true,"ab#c", "ad#c");
    }

    private static void Test(bool expected, string S, string T)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.BackspaceCompare(S, T);
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