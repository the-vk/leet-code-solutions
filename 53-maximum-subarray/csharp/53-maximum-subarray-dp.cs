using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int MaxSubArray(int[] nums) {
        var maxSum = nums[0];
        for (var i = 1; i < nums.Length; ++i) {
            if (nums[i-1] > 0) {
                nums[i] += nums[i-1];
            }
            maxSum = Math.Max(maxSum, nums[i]);
        }
        return maxSum;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(19, new[]{10,-1,10});
    }

    private static void Test(int expected, int[] nums)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.MaxSubArray(nums);
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