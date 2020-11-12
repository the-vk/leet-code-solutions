using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int LongestValidParentheses(string s) {
        var subs = new int[s.Length];
        for (var i = 0; i < s.Length - 1; ++i) {
            if (s[i] == '(' && s[i+1] == ')') {
                subs[i] = i+1;
            }
        }
        var max = 0;
        var changed = false;
        do {
            changed = false;
            // merge
            for (var i = 0; i < s.Length - 1; ++i) {
                if (subs[i] == 0) continue;
                if (subs[i] + 1 < subs.Length && subs[subs[i] + 1] != 0) {
                    var e = subs[i] + 1;
                    subs[i] = subs[e];
                    subs[e] = 0;
                    changed = true;
                }
                if (i > 0 && subs[i] < s.Length - 1 && s[i-1] == '(' && s[subs[i] + 1] == ')') {
                    subs[i-1] = subs[i] + 1;
                    subs[i] = 0;
                    changed = true;
                }
            }
            // percolate
        } while (changed);
        
        for (var i = 0; i < subs.Length; ++i){
            if (subs[i] != 0) max = Math.Max(max, subs[i]-i+1);
        }
        return max;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(4, ")()())");
    }

    private static void Test(int expected, string s)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.LongestValidParentheses(s);
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