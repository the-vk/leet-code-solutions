using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class Solution {
    public int SubarraysWithKDistinct(int[] A, int K) {
        var answer = 0;
        Dictionary<int, int> seen;
        for (var factor = K; factor <= A.Length; ++factor) {
            seen = new Dictionary<int, int>();
            for (var i = 0; i < factor; ++i) {
                if (seen.ContainsKey(A[i])) {
                    seen[A[i]] += 1;
                } else {
                    seen[A[i]] = 1;
                }
            }
            if (seen.Count == K) {
                answer++;
            }
            for (var i = factor; i < A.Length; ++i) {
                seen[A[i-factor]] -= 1;
                if (seen[A[i-factor]] == 0) {
                    seen.Remove(A[i-factor]);
                }
                if (seen.ContainsKey(A[i])) {
                    seen[A[i]] += 1;
                } else {
                    seen[A[i]] = 1;
                }
                if (seen.Count == K) {
                    answer++;
                }
            }
        }
        return answer;
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