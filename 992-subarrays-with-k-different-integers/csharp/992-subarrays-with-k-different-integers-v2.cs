using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int SubarraysWithKDistinct(int[] A, int K) {
        int answer, l1, l2;
        answer = l1 = l2 = 0;
        var seen1 = new Dictionary<int, int>();
        var seen2 = new Dictionary<int, int>();
        foreach (var x in A) {
            seen1.Inc(x);
            seen2.Inc(x);
            while (seen1.Count > K) {
                seen1.Dec(A[l1++]);
            }
            while (seen2.Count >= K) {
                seen2.Dec(A[l2++]);
            }
            answer += l2 - l1;
        }
        return answer;
    }
}

public static class Extensions {
    public static void Inc(this Dictionary<int, int> dict, int key) {
        if (dict.ContainsKey(key))
            dict[key] += 1;
        else
            dict[key] = 1;
    }
    
    public static void Dec(this Dictionary<int, int> dict, int key) {
        dict[key] -= 1;
        if (dict[key] == 0) dict.Remove(key);
    }
}

public static class Program
{
    public static void Main()   
    {
        Test(7, new []{1,2,1,2,3}, 2);
    }

    private static void Test(int expected, int[] A, int K)
    {
        var solution = new Solution();
        var stopwatch = Stopwatch.StartNew();
        var actual = solution.SubarraysWithKDistinct(A, K);
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