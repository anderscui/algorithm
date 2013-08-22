using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestLinkedList
    {
        [TestCase]
        [ExpectedException(typeof(NullReferenceException))]
        public void TestFirstOfEmptyList()
        {
            var list = new LinkedList<int>();
            Console.WriteLine(list.First.Value);
        }
    }
}
