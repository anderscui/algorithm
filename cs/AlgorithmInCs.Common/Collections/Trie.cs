using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    //public interface ITrie<T>
    //{
    //    void Add(string key, T value);
    //    bool Contains(string key);
    //    T Remove(string key);
    //}

    //public class TrieNode
    //{
    //    public char Key { get; set; }
    //    public int? Value { get; set; }
    //    public TrieNode Next { get; set; }
    //    public List<TrieNode> Children { get; set; }
    //}

    //public class Trie
    //{
    //    public TrieNode Root { get; private set; }


    //}

    public class TrieNode
    {
        public char Key { get; set; }
        public int? Value { get; set; }
        public Dictionary<char, TrieNode> Children { get; set; }
    }

    public class Trie
    {
        private static readonly char RootKey = char.MinValue;
        private static readonly char EndKey = '\0';
        private static readonly int? MissingValue = 0;

        public TrieNode Root { get; private set; }

        public Trie()
        {
            Root = new TrieNode() { Key = char.MinValue, Value = MissingValue, Children = new Dictionary<char, TrieNode>() };
        }

        public void Add(string key, int value)
        {
            if (string.IsNullOrWhiteSpace(key))
            {
                throw new ArgumentException("key must not be null or whitespace");
            }

            key = key.Trim();
            var curNode = Root;
            foreach (var ch in key)
            {
                if (!curNode.Children.ContainsKey(ch))
                {
                    curNode.Children[ch] = new TrieNode() { Key = ch, Value = MissingValue, Children = new Dictionary<char, TrieNode>() };
                }
                curNode = curNode.Children[ch];
            }
            curNode.Value = value;
        }

        public bool ContainsKey(string key)
        {
            if (string.IsNullOrWhiteSpace(key))
            {
                throw new ArgumentException("key must not be null or whitespace");
            }

            key = key.Trim();
            var curNode = Root;
            foreach (var ch in key)
            {
                if (!curNode.Children.ContainsKey(ch))
                {
                    return false;
                }
                curNode = curNode.Children[ch];
            }
            return curNode.Value > 0;
        }
    }
}
