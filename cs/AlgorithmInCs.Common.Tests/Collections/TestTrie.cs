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
            trie.Insert("ann");
            trie.Insert("anders");
            trie.Insert("andy");

            trie.Insert("bill");
            trie.Insert("candy");
            trie.Insert("dove");

            return trie;
        }

        [Test]
        public void TestInsert()
        {
            var trie = GetTestTrie();
            Console.WriteLine(trie);
        }

        [Test]
        public void TestContainsKey()
        {
            var trie = GetTestTrie();
            Assert.That(trie.Contains("anders"));
            Assert.That(trie.Contains("andrew"), Is.False);
            Assert.That(trie.Contains("bily"));
        }
    }
}
