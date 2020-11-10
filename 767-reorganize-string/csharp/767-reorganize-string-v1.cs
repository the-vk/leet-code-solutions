using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public string ReorganizeString(string S) {
        var letters = new Dictionary<char, int>();
        foreach (var c in S) {
            if (letters.ContainsKey(c)) {
                letters[c] += 1;
            } else {
                letters[c] = 1;
            }
        }
        
        var sb = new StringBuilder();
        while (letters.Count > 0) {
            var sorted = letters.OrderByDescending(x => x.Value).ToList();
            char next;
            if (sb.Length > 0) {
                var last = sb[sb.Length - 1];
                if (sorted[0].Key == last) {
                    if (sorted.Count == 1) {
                        return "";
                    } else {
                        next = sorted[1].Key;
                    }
                } else {
                    next = sorted[0].Key;
                }
            } else {
                next = sorted[0].Key;
            }
            letters[next] -= 1;
            if (letters[next] == 0) {
                letters.Remove(next);
            }
            sb.Append(next);
        }
        return sb.ToString();
    }
}

public static class Program
{
    public static void Main()   
    {
        Test("abab", "aabb");
    }

    private static void Test(int expected, string S)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.ReorganizeString(S);
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