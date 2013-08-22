using System;
using System.Collections.Generic;

using NUnit.Framework;

using Andersc.AlgorithmInCs.Algorithms.Sorting;

namespace Andersc.AlgorithmInCs.Tests.Algorithms
{
    [TestFixture]
    public class TestLinkedListSorter
    {
        private LinkedList<int> GetList()
        {
            var list = new LinkedList<int>();
            int n = 5;
            for (int i = 0; i < n; i++)
            {
                list.AddFirst(2 * i + 1);
                list.AddFirst(8 - 2 * i);
            }
            return list;
        }

        [Test]
        public void TestSelectionSort()
        {
            var list = GetList();
            //foreach (var elem in list)
            //{
            //    Console.WriteLine(elem);
            //}
            var res = LinkedListSorter.Selection(list);
            foreach (var re in res)
            {
                Console.WriteLine(re);
            }
        }
    }
}
