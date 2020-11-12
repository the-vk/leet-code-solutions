using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public string LongestPalindrome(string s) {
        var maxPal = (0,0);
        for (var i = 0; i < s.Length - 1; ++i) {
            maxPal = TupleMax(maxPal, ExpandPalindrome(i, i, s));
            maxPal = TupleMax(maxPal, ExpandPalindrome(i, i+1, s));
        }
        return s.Substring(maxPal.Item1, maxPal.Item2 - maxPal.Item1 + 1);
    }
    
    (int,int) ExpandPalindrome(int s, int e, string str)
    {
        if (str[s] != str[e]) return (0,0);
        while (s > 0 && e < str.Length-1){
            if (str[s-1] == str[e+1]) {
                s--;
                e++;
            } else {
                break;
            }
        }
        return (s,e);
    }
    
    (int, int) TupleMax((int, int) l, (int,int) r) => (l.Item2 - l.Item1) > (r.Item2 - r.Item1) ? l : r;
}

public static class Program
{
    public static void Main()   
    {
        Test("aa", "caac");
    }

    private static void Test(string expected, string s)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.LongestPalindrome(s);
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