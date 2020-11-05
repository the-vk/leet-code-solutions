using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

using System.Drawing;

public class Solution {
    public int[][] UpdateMatrix(int[][] matrix) {
        var N = matrix.Length;
        if (N == 0) {
            return new int[0][];
        }
        var M = matrix[0].Length;
        
        var result = new int[N][];
        for (var x = 0; x < N; x++)
        {
            result[x] = new int[M];
        }
        
        for (var x = 0; x < N; ++x)
        for (var y = 0; y < M; ++y) {
            result[x][y] = FindNearest(matrix, x, y, N-1, M-1);
        }
        
        return result;
    }
    
    private int FindNearest(int[][] matrix, int x, int y, int maxX, int maxY) {
        var processed = new HashSet<Point>();
        var queue = new Queue<Point>();
        queue.Enqueue(new Point() {X = x, Y = y});
            
        while (queue.Count > 0) {
            var p = queue.Dequeue();
            if (processed.Contains(p))
                continue;
            if (matrix[p.X][p.Y] == 0)
                return Math.Abs(x - p.X) + Math.Abs(y - p.Y);
            if (p.X > 0)
                queue.Enqueue(new Point() {X = p.X-1, Y = p.Y});
            if (p.Y > 0)
                queue.Enqueue(new Point() {X = p.X, Y = p.Y-1});
            if (p.X < maxX) 
                queue.Enqueue(new Point() {X = p.X+1, Y = p.Y});
            if (p.Y < maxY)
                queue.Enqueue(new Point() {X = p.X, Y = p.Y+1});
            processed.Add(p);
        }
        return -1;
    }
}

public static class Program
{
    public static void Main()
    {
        int[][] matrix = new int[5][];
        matrix[0] = new [] {0,1,0,1,1};
        matrix[1] = new [] {1,1,0,0,1};
        matrix[2] = new [] {0,0,0,1,0};
        matrix[3] = new [] {1,0,1,1,1};
        matrix[4] = new [] {1,0,0,0,1};
        Test(null, matrix);
    }

    private static void Test(int[][] expected, int[][] matrix)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.UpdateMatrix(matrix);
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