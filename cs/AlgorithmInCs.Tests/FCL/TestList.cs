using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestList
    {
        [TestCase]
        public void TestBinarySearchNotFound()
        {
            var list = new List<int>() { 1, 1, 2, 3, 5, 8, 13, 21 };
            Console.WriteLine(list.BinarySearch(5));
            Console.WriteLine(list.BinarySearch(0));
            Console.WriteLine(list.BinarySearch(4));
            Console.WriteLine(list.BinarySearch(30));
        }
    }
}
