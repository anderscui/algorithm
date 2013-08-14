using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestLinqToObjects
    {
        [TestCase]
        [ExpectedException(typeof(ArgumentNullException))]
        public void TestAnyForEmptyCollectionException()
        {
            int[] arr = null;
            Assert.That(arr.Any(), Is.False);
        }

        [TestCase]
        public void TestAnyMethodForEmptyCollection()
        {
            int[] arr = new int[0];
            Assert.That(arr.Any(), Is.False);
        }
    }
}
