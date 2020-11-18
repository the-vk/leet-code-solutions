using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    public int CountSubstrings(string s) {
        var ans = 1;
        for (var i = 0; i < s.Length - 1; ++i) {
            ans += Expand(i, i, s);
            if (s[i] == s[i+1]) ans += Expand(i, i+1, s);
        }
        return ans;
    }
    
    private int Expand(int l, int r, string s) {
        var ans = 0;
        while (l >= 0 && r < s.Length) {
            if (s[l] == s[r]) {
                ans++;
            } else {
                break;
            }
            l--; r++;
        }
        return ans;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(6, "aaa");
    }

    private static void Test(int expected, string s)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.CountSubstrings(s);
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