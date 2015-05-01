using System;
using NUnit.Framework;
using Andersc.AlgorithmInCs.Common.Collections;

namespace Andersc.AlgorithmInCs.Common.Tests.Collections
{
    [TestFixture]
    public class TestLinkedList
    {
        [TestCase]
        public void TestCount()
        {
            var list = new LinkedList<int>();
            Assert.That(list.IsEmpty);

            list.Append(3);
            Assert.That(list.IsEmpty, Is.False);
            Assert.That(list.Count, Is.EqualTo(1));

            list.Append(2);
            Assert.That(list.Count, Is.EqualTo(2));

            list.Append(1);
            Assert.That(list.Count, Is.EqualTo(3));
        }

        [TestCase]
        public void TestFirst()
        {
            var list = new LinkedList<int>();
            Assert.That(list.First, Is.Null);

            list.Append(1);
            Assert.That(list.First, Is.Not.Null);
            Assert.That(list.First.Value, Is.EqualTo(1));
            Assert.That(list.First.Next, Is.Null);
            Assert.That(list.First.Previous, Is.Null);

            list.Append(2);
            Assert.That(list.First.Next, Is.Not.Null);
            Assert.That(list.First.Previous, Is.Null);
        }

        [TestCase]
        public void TestAppend()
        {
            var list = new LinkedList<int>();
            list.Append(3);
            list.Append(2);
            list.Append(1);

            Assert.That(list.Count, Is.EqualTo(3));
            Assert.That(list.First.Value, Is.EqualTo(3));
            Assert.That(list.Last.Value, Is.EqualTo(1));
        }

        [TestCase]
        public void TestClear()
        {
            var list = new LinkedList<int>();
            list.Append(3);
            list.Append(2);
            list.Append(1);
            Assert.That(list.Count, Is.EqualTo(3));

            list.Clear();
            Assert.That(list.IsEmpty);
        }

        [TestCase]
        public void TestClearListOfOneElement()
        {
            var list = new LinkedList<int>();
            list.Append(1);
            Assert.That(list.Count, Is.EqualTo(1));

            list.Clear();
            Assert.That(list.IsEmpty);
        }

        #region Max()

        [TestCase]
        public void TestMaxOfIntList()
        {
            var list = new LinkedList<int>();
            var elems = new[] { 9, 5, 6, 10, 5, 3 };
            foreach (var elem in elems)
            {
                list.Append(elem);
            }

            var max = list.Max();
            Assert.That(max, Is.Not.Null);
            Assert.That(max.Value, Is.EqualTo(10));
        }

        [TestCase]
        public void TestMaxOfStringList()
        {
            var list = new LinkedList<string>();
            var elems = new[] { null, "hello", "world", "test", null, "C#", "Python" };
            foreach (var elem in elems)
            {
                list.Append(elem);
            }

            var max = list.Max();
            Assert.That(max, Is.Not.Null);
            Assert.That(max.Value, Is.EqualTo("world"));
        }

        [TestCase]
        [ExpectedException(typeof(CollectionEmptyException))]
        public void TestMaxOfEmptyList()
        {
            var list = new LinkedList<int>();
            Console.WriteLine(list.Max());
        }

        #endregion

        [TestCase]
        public void TestGetEnumerator()
        {
            var list = new LinkedList<int>();
            list.Append(3);
            list.Append(2);
            list.Append(1);

            foreach (var item in list)
            {
                Console.WriteLine(item);
            }
        }
    }
}
