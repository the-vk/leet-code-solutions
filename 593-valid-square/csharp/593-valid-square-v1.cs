using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

using System.Drawing;

public class Solution {
    public bool ValidSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        const float epsilon = 0.000000001f;
        var vectors = new PointF[6];
        vectors[0] = new PointF() { X = p1[0] - p2[0], Y = p1[1] - p2[1] };
        vectors[1] = new PointF() { X = p1[0] - p3[0], Y = p1[1] - p3[1] };
        vectors[2] = new PointF() { X = p1[0] - p4[0], Y = p1[1] - p4[1] };
        vectors[3] = new PointF() { X = p2[0] - p3[0], Y = p2[1] - p3[1] };
        vectors[4] = new PointF() { X = p2[0] - p4[0], Y = p2[1] - p4[1] };
        vectors[5] = new PointF() { X = p3[0] - p4[0], Y = p3[1] - p4[1] };
        var lens = vectors.Select(x => x.X*x.X + x.Y*x.Y).OrderBy(x => x).ToArray();
        
        if (lens.Any(x => Math.Abs(x - 0.0f) < epsilon)) {
            return false;
        }
        
        for (var i = 1; i < 4; ++i) {
            if (Math.Abs(lens[0] - lens[i]) > epsilon) {
                return false;
            }
        }        
        
        return Math.Abs(lens[4] - lens[5]) < epsilon;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(true, new [] {0,0}, new [] {1,1}, new [] {1,0}, new [] {0,1});
    }

    private static void Test(bool expected, int[] p1, int[] p2, int[] p3, int[] p4)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.ValidSquare(p1, p2, p3, p4);
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