using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution {
    public int LongestOnes(int[] A, int K) {
        int l = 0;
        int r = 0;
        int max = 0;
        var flipped = new Queue<int>();
        while (r < A.Length)
        {
            if (A[r] != 1)
            {
                if (K > 0)
                {
                    if (flipped.Count >= K)
                    {
                        var f = flipped.Dequeue();
                        l = f + 1;
                    }
                    flipped.Enqueue(r);
                }
                else
                {
                    l = r+1;
                }
            }
            r++;
            max = Math.Max(max, r - l);
        }
        return max;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(4, new int[] {1,1,1,0,0,0,1,1,1,1,0}, 0);
        Test(6, new int[] {1,1,1,0,0,0,1,1,1,1,0}, 2);
        Test(10, new int[] {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1}, 3);
        Test(1, new int[] {1}, 0);
        Test(3, new int[] {0,0,1,1,1,0,0}, 0);
    }

    private static void Test(int expected, int[] A, int K)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.LongestOnes(A, K);
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