using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution {
    public string LongestPrefix(string s) {
        if (s.Length == 0 || s.Length == 1) {
            return String.Empty;
        }
        int suffix = s.Length - 1;
        int prefix = s.Length - 2;
        int prefixLength = suffix;
        while (prefix >= 0) {
            if (s[prefix] == s[suffix]) {
                var pi = prefix;
                while (pi >= 0) {
                    if (s[pi] != s[suffix]) {
                        suffix = s.Length - 1;
                        break;
                    }
                    pi--;
                    suffix--;
                    if (pi < 0) {
                        return s.Substring(0, prefix+1);
                    }
                }
            }
            prefix--;
        }
        return "";
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