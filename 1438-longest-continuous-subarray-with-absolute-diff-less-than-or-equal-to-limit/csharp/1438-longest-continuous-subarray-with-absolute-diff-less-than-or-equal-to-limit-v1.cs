using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        if (nums.Length == 0) return 0;
        var minQueue = new LinkedList<int>();
        var maxQueue = new LinkedList<int>();
        
        var left = 0;
        var right = 0;
        
        var ans = 0;
        
        while (right < nums.Length) {
            var n = nums[right];
            
            while (maxQueue.Last?.Value > n) {
                maxQueue.RemoveLast();
            }
            while (minQueue.Last?.Value < n) {
                minQueue.RemoveLast();
            }
            
            minQueue.AddLast(n);
            maxQueue.AddLast(n);
            
            if (Math.Abs(minQueue.First.Value - maxQueue.First.Value) > limit) {
                if (maxQueue.First.Value == nums[left]) maxQueue.RemoveFirst();
                if (minQueue.First.Value == nums[left]) minQueue.RemoveFirst();
                left++;
            }
            right++;
            ans = Math.Max(ans, right-left);
        }
        
        
        return ans;
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(4, new[] {10,1,2,4,7,2}, 5);
    }

    private static void Test(int expected, int[] nums, int limit)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.LongestSubarray(nums, limit);
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