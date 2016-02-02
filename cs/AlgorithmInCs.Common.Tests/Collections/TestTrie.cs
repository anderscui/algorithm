using System;
using NUnit.Framework;

using Andersc.AlgorithmInCs.Common.Collections;

namespace Andersc.AlgorithmInCs.Common.Tests.Collections
{
    [TestFixture]
    public class TestTrie
    {
        private Stack<int> GetEmptyStack()
        {
            return new Stack<int>();
        }

        private Trie GetTestTrie()
        {
            var trie = new Trie();
            trie.Add("ann", 1);
            trie.Add("anders", 3);
            trie.Add("andy", 5);

            trie.Add("bill", 7);
            trie.Add("candy", 9);
            trie.Add("dove", 9);

            return trie;
        }

        [Test]
        public void TestAdd()
        {
            var trie = GetTestTrie();
            Console.WriteLine(trie);
        }

        [Test]
        public void TestContainsKey()
        {
            var trie = GetTestTrie();
            Assert.That(trie.ContainsKey("anders"));
            Assert.That(trie.ContainsKey("andrew"), Is.False);
            Assert.That(trie.ContainsKey("bily"));
        }
    }
}
