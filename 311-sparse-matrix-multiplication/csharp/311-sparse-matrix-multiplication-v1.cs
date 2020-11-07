using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int[][] Multiply(int[][] A, int[][] B) {
        var result = new int[A.Length][];
        for (var i = 0; i < A.Length; ++i) {
            result[i] = new int[B[0].Length];
        }
        
        for (var i = 0; i < A.Length; ++i)
        for (var j = 0; j < B[0].Length; ++j) {
            for (var x = 0; x < A[0].Length; ++x) {
                result[i][j] += A[i][x] * B[x][j];
            }
        }
        
        return result;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(new[]{new[]{17}}, new[]{new[]{1,5}}, new[]{new[]{12}, new[]{-1}});
    }

    private static void Test(int[][] expected, int[][] A, int[][]B)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.Multiply(A, B);
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