using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public int Guess(string word);
 * }
 */

class Master {
    public int guess(string word) => 0;
}

class Solution {
    public void FindSecretWord(string[] wordlist, Master master) {
        var words = new HashSet<string>(wordlist);
        
        var candidate = Rnd(words);
        var match = master.guess(candidate);
        while (match != 6) {
            Console.WriteLine($"{words.Count} words | candidate: {candidate} | match: {match}");
            if (match == 0) {
                words = words.Where(x => Match(candidate, x) == 0).ToHashSet();
            } else {
                words = words.Where(x => candidate != x && Match(candidate, x) >= match).ToHashSet();
            }
            candidate = Rnd(words);
            match = master.guess(candidate);
        }
        
        return;
    }
    
    string Rnd(HashSet<string> set) {
        var rnd = new Random();
        return set.Skip(rnd.Next(set.Count)).First();
    }
    
    int Match(string l, string r) {
        var m = 0;
        for (var i = 0; i < l.Length; ++i)
            if (l[i] == r[i]) m++;
        return m;
    }    
}

public static class Program
{
    public static void Main()   
    {

    }

    // private static void Test(int expected, string s)
    // {
    //     var solution = new Solution();
    //     var stopwatch = Stopwatch.StartNew();
    //     var actual = solution.LongestValidParentheses(s);
    //     if (actual != expected)
    //     {
    //         Console.WriteLine($"actual value '{actual}' is not equal to expected value '{expected}'");
    //     }
    //     stopwatch.Stop();
    //     var elapsed = stopwatch.Elapsed.TotalSeconds;
    //     Console.WriteLine($"elapsed: {elapsed} secs");
    // }

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