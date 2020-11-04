using System;
using System.Collections.Generic;
using System.Diagnostics;

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

public class Solution {
    public int MaxSumBST(TreeNode root) {
        int maxSum = 0;
        Traverse(root, ref maxSum);
        return maxSum;
    }

    private (bool? isBST, int? sum, int? low, int? high) Traverse(TreeNode node, ref int maxSum)
    {
        if (node == null)
        {
            return (null, 0, null, null);
        }
        
        var (leftBST, leftSum, leftLow, leftHigh) = Traverse(node.left, ref maxSum);
        var (rightBST, rightSum, rightLow, rightHigh) = Traverse(node.right, ref maxSum);

        if 
        (
            (!leftBST.HasValue || (leftBST.Value && leftHigh.Value < node.val)) &&
            (!rightBST.HasValue || (rightBST.Value && node.val < rightLow.Value))
        )
        {
            var sum = leftSum.Value + node.val + rightSum.Value;
            maxSum = Math.Max(maxSum, sum);
            return (true, sum, leftLow.HasValue ? leftLow : node.val, rightHigh.HasValue ? rightHigh : node.val);
        }
        
        return (false, null, null, null);
    }
}

public static class Program
{
    public static void Main()
    {
        Test(0, new int?[] {-4,-2,-5});
        Test(14, new int?[] {4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10});
        Test(20, new int?[] { 1,4,3,2,4,2,5,null,null,null,null,null,null,4,6 });
        Test(2, new int?[] { 4,3,null,1,2 });
        Test(6, new int?[] {2,1,3});
        Test(7, new int?[] {5,4,8,3,null,6,3});

    }

    private static void Test(int expected, int?[] input)
    {
        var solution = new Solution();
        var root = ReadTreeNodeInput(input);
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.MaxSumBST(root);
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