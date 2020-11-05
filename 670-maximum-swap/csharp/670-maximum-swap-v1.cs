using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

using System.Drawing;

public class Solution {
    public int MaximumSwap(int num) {
        var digits = new List<int>();
        while (num > 0) {
            digits.Add(num % 10);
            num /= 10;
        }
        var digitsSorted = digits.OrderBy(x => x).ToList();
        for (var i = digits.Count - 1; i >= 0; --i) {
            if (digits[i] != digitsSorted[i]) {
                for (var j = 0; j < i; j++) {
                    if (digits[j] == digitsSorted[i]) {
                        var t = digits[i];
                        digits[i] = digits[j];
                        digits[j] = t;
                        break;
                    }
                }
                break;
            }
        }
        num = 0;
        digits.Reverse();
        foreach (var d in digits) {
            num *= 10;
            num += d;
        }
        return num;
    }
}

public static class Program
{
    public static void Main()
    {
        Test(7326, 2376);
    }

    private static void Test(int expected, int num)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.MaximumSwap(num);
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