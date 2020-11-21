using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class Solution {
    public int Reverse(int x) {
        if (x == 0) return 0;
        if (x == Int32.MaxValue || x == Int32.MinValue) return 0;
        var sign = (long)x/Math.Abs((long)x);
        x = Math.Abs(x);
        var stack = new Stack<int>();
        while (x > 0) {
            stack.Push(x % 10);
            x /= 10;
        }
        long ans = 0;
        var radix = 1;
        while (stack.Count > 0) {
            ans += ((long)stack.Pop() * radix);
            radix *= 10;
        }
        if (ans > Int32.MaxValue || ans < Int32.MinValue) return 0;
        ans *= sign;
        return (int)ans;
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