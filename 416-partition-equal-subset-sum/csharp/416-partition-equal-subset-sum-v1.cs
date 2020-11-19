using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    Dictionary<int, bool> memo = new Dictionary<int, bool>();
    public bool CanPartition(int[] nums) {
        var sum = nums.Sum();
        if (sum % 2 != 0) return false;
        sum /= 2;
        
        return CanSum(nums, sum, new HashSet<int>());
    }
    
    public bool CanSum(int[] list, int target, HashSet<int> skip) {
        if (memo.ContainsKey(target)) return memo[target];
        for (var i = 0; i < list.Length; ++i) {
            if (skip.Contains(i)) continue;
            var x = list[i];
            if (x == target) {
                memo[target] = true;
                return true;  
            } 
            if (x > target) {
                memo[target] = false;
                return false;
            }
            
            skip.Add(i);
            if (CanSum(list, target - x, skip)) {
                memo[target] = true;
                return true;
            }
            skip.Remove(i);
        }
        memo[target] = false;
        return false;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(true, new []{1,5,11,5});
    }

    private static void Test(bool expected, int[] nums)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.CanPartition(nums);
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