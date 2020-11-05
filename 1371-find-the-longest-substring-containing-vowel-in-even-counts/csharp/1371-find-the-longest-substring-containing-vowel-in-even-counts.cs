using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    public int FindTheLongestSubstring(string s) {
        var bitm = new Dictionary<char, byte> {
            ['a'] = 1,
            ['e'] = 2,
            ['i'] = 4,
            ['o'] = 8,
            ['u'] = 16
        };
        var pos = new Dictionary<byte, int>() { [0] = -1 };
        byte mask = 0;
        int result = 0;
        for (var i = 0; i < s.Length; ++i) 
        {
            var c = s[i];
            if (bitm.ContainsKey(c))
            {
                mask ^= bitm[c];
            }
            if (!pos.ContainsKey(mask))
            {
                pos.Add(mask, i);
            }
            else
            {
                result = Math.Max(result, i - pos[mask]);
            }
        }
        return result;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(13, "eleetminicoworoep");
        Test(5, "leetcodeisgreat");
    }

    private static void Test(int expected, string s)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.FindTheLongestSubstring(s);
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