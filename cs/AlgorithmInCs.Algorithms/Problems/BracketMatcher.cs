using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Andersc.AlgorithmInCs.Common;

namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    public class BracketMatcher
    {
        //private static readonly List<char> Symbols = new List<char>() { '{', '}', '[', ']', '(', ')' };
        private static readonly List<char> OpenSymbols = new List<char>() { '{', '[', '(' };
        private static readonly List<char> CloseSymbols = new List<char>() { '}', ']', ')' };
        private static readonly Dictionary<char, char> Mapping 
            = new Dictionary<char, char>() { { '{', '}' }, { '[', ']' }, { '(', ')' } };

        public bool Solve(string exp)
        {
            var s = new Stack<char>();
            foreach (var ch in exp)
            {
                if (OpenSymbols.Contains(ch))
                {
                    s.Push(ch);
                }
                else if(CloseSymbols.Contains(ch))
                {
                    if (s.Count == 0)
                    {
                        return false;
                    }

                    var open = s.Pop();
                    if (Mapping[open] != ch)
                    {
                        return false;
                    }
                }
            }

            return s.Count == 0;
        }
    }
}