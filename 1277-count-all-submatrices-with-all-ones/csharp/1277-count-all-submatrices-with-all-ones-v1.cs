using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    public int CountSquares(int[][] matrix) {
        var ans = 0;
        
        for (var i = 0; i < matrix.Length; ++i)
        for (var j = 0; j < matrix[0].Length; ++j) {
            if (matrix[i][j] == 0) continue;
            ans += 1;
            var s = 1;
            while (true) {
                if (j+s == matrix[0].Length || i+s == matrix.Length) break;
                
                for (var x = j; x <= j+s; ++x) {
                    if (matrix[i+s][x] == 0) goto next;
                }
                for (var x = i; x <= i+s; ++x) {
                    if (matrix[x][j+s] == 0) goto next;
                }
                ans++;
                s++;
            }
            next:
            continue;
        }
        
        return ans;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(15, new []{
            new[]{0,1,1,1},
            new[]{1,1,1,1},
            new[]{0,1,1,1}
        });
    }

    private static void Test(int expected, int[][] matrix)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.CountSquares(matrix);
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