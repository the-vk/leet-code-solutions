using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        if (nums.Length == 0) return 0;
        
        var seen = new Dictionary<int, int>();
        var left = 0;
        var right = 0;
        var maxAns = 0;  
        
        seen[nums[0]] = 1;
        
        while (true) {
            var (min, max) = MinMax(seen.Keys);
            
            if (max-min <= limit) {
                maxAns = Math.Max(maxAns, right-left+1);
                right++;
                if (right == nums.Length) break;
                if (seen.ContainsKey(nums[right])) {
                    seen[nums[right]] += 1;
                } else {
                    seen[nums[right]] = 1;
                }
            } else {
                seen[nums[left]] -= 1;
                if (seen[nums[left]] == 0) {
                    seen.Remove(nums[left]);
                }
                left++;
            }
        }
        
        return maxAns;
    }
    
    (int, int) MinMax(IEnumerable<int> seq) {
        int? min = null;
        int? max = null;
        foreach (var x in seq) {
            if (min == null && max == null) {
                min = max = x;
            } else {
                min = Math.Min(min.Value, x);
                max = Math.Max(max.Value, x);
            }
        }
        return (min ?? 0, max ?? 0);
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