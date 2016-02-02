using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    // Refer to: https://github.com/brianfromoregon/trie
    public class TrieNode
    {
        public char Char { get; set; }
        public int Frequency { get; set; }
        public Dictionary<char, TrieNode> Children { get; set; }

        public TrieNode(char ch)
        {
            Char = ch;
            Frequency = 0;
            
            // TODO: or an empty dict?
            //Children = null;
        }

        public int Insert(string s, int pos, int freq = 0)
        {
            if (string.IsNullOrEmpty(s) || pos >= s.Length)
            {
                return 0;
            }

            if (Children == null)
            {
                Children = new Dictionary<char, TrieNode>();
            }

            var c = s[pos];
            if (!Children.ContainsKey(c))
            {
                Children[c] = new TrieNode(c);
            }

            var curNode = Children[c];
            if (pos == s.Length - 1)
            {
                curNode.Frequency++;
                return curNode.Frequency;
            }
            else
            {
                return curNode.Insert(s, pos + 1);
            }
        }

        public TrieNode Search(string s, int pos)
        {
            if (string.IsNullOrEmpty(s))
            {
                return null;
            }

            if (pos >= s.Length || Children == null)
            {
                return null;
            }
            else if (pos == s.Length - 1)
            {
                return Children[s[pos]];
            }
            else
            {
                return Children.ContainsKey(s[pos]) ? Children[s[pos]].Search(s, pos + 1) : null;
            }
        }
    }

    public interface ITrie
    {
        //string BestMatch(string word, long maxTime);
        bool Contains(string word);
        int Frequency(string word);
        int Insert(string word);
        //bool Remove(string word);
        int Size();
    }

    public class Trie : ITrie
    {
        private static readonly char RootChar = '\0';
        private static readonly char EndKey = '\0';
        private static readonly int? MissingValue = 0;

        private readonly TrieNode Root;

        public int Count { get; private set; }

        public Trie()
        {
            Root = new TrieNode(RootChar);
            Count = 0;
        }

        public bool Contains(string word)
        {
            CheckWord(word);

            var node = Root.Search(word.Trim(), 0);
            return node.IsNotNull();
        }

        public int Frequency(string word)
        {
            CheckWord(word);

            var node = Root.Search(word.Trim(), 0);
            return node.IsNull() ? 0 : node.Frequency;
        }

        public int Insert(string word)
        {
            CheckWord(word);

            var i = Root.Insert(word.Trim(), 0);
            if (i > 0)
            {
                Count++;
            }

            return i;
        }

        public int Size()
        {
            return Count;
        }

        private void CheckWord(string word)
        {
            if (string.IsNullOrWhiteSpace(word))
            {
                throw new ArgumentException("word must not be null or whitespace");
            }
        }
    }
}
