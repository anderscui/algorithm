using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    /// <summary>
    /// A simple implementation of circular doubly linked list.
    /// </summary>
    /// <typeparam name="T">The type of elements in the list.</typeparam>
    [DebuggerDisplay("Count = {Count}"), DebuggerTypeProxy(typeof(LinkedListDebugView<>))]
    public class LinkedList<T> : ICollection<T>
    {
        /// <summary>
        /// head is the first real node instead of a sentinel.
        /// </summary>
        internal LinkedListNode<T> head;
        internal int size;

        public int Count
        {
            get { return size; }
        }

        public bool IsEmpty
        {
            get { return (size == 0); }
        }

        public LinkedListNode<T> First
        {
            get { return head; }
        }

        public LinkedListNode<T> Last
        {
            get
            {
                if (head != null)
                {
                    return head.prev;
                }
                return null;
            }
        }

        public LinkedList()
        {
        }

        public LinkedList(IEnumerable<T> enumerable)
        {
            if (enumerable.IsNull())
            {
                throw new ArgumentNullException("enumerable");
            }

            foreach (T item in enumerable)
            {
                Append(item);
            }
        }

        public LinkedListNode<T> AddAfter(LinkedListNode<T> node, T value)
        {
            ValidateNode(node);

            var newNode = new LinkedListNode<T>(this, value);
            InsertNodeBefore(node.next, newNode);

            return newNode;
        }

        public void AddAfter(LinkedListNode<T> node, LinkedListNode<T> newNode)
        {
            ValidateNode(node);
            ValidateNewNode(newNode);
            InsertNodeBefore(node.next, newNode);
            newNode.list = this;
        }

        public LinkedListNode<T> AddBefore(LinkedListNode<T> node, T item)
        {
            ValidateNode(node);

            var newNode = new LinkedListNode<T>(this, item);
            InsertNodeBefore(node, newNode);
            if (node == head)
            {
                head = newNode;
            }

            return newNode;
        }

        public void AddBefore(LinkedListNode<T> node, LinkedListNode<T> newNode)
        {
            ValidateNode(node);
            ValidateNewNode(newNode);
            InsertNodeBefore(node, newNode);
            newNode.list = this;
            if (node == head)
            {
                head = newNode;
            }
        }

        public LinkedListNode<T> Prepend(T item)
        {
            var newNode = new LinkedListNode<T>(this, item);
            if (IsEmpty)
            {
                InsertNodeIntoEmptyList(newNode);
            }
            else
            {
                InsertNodeBefore(head, newNode);
                head = newNode;
            }

            return newNode;
        }

        public void Prepend(LinkedListNode<T> newNode)
        {
            ValidateNewNode(newNode);
            if (IsEmpty)
            {
                InsertNodeIntoEmptyList(newNode);
            }
            else
            {
                InsertNodeBefore(head, newNode);
                head = newNode;
            }

            newNode.list = this;
        }

        public LinkedListNode<T> Append(T item)
        {
            var newNode = new LinkedListNode<T>(this, item);
            if (IsEmpty)
            {
                InsertNodeIntoEmptyList(newNode);
            }
            else
            {
                InsertNodeBefore(head, newNode);
            }

            return newNode;
        }

        public void Append(LinkedListNode<T> newNode)
        {
            ValidateNewNode(newNode);
            if (IsEmpty)
            {
                InsertNodeIntoEmptyList(newNode);
            }
            else
            {
                InsertNodeBefore(head, newNode);
            }

            newNode.list = this;
        }

        public void Clear()
        {
            var next = head;
            while (next != null)
            {
                var node = next;
                next = next.Next;
                node.Invalidate();
            }

            head = null;
            size = 0;
        }

        public bool Contains(T value)
        {
            return (Find(value) != null);
        }

        public void CopyTo(T[] array, int index)
        {
            if (array == null)
            {
                throw new ArgumentNullException("array");
            }
            if (index < 0 || index > array.Length)
            {
                throw new ArgumentOutOfRangeException("index");
            }
            if (array.Length - index < size)
            {
                throw new ArgumentException("Insufficient space.");
            }

            var next = head;
            if (next != null)
            {
                do
                {
                    array[index++] = next.item;
                    next = next.next;
                }
                while (next != this.head);
            }
        }

        public LinkedListNode<T> Find(T value)
        {
            var next = head;
            var comparer = EqualityComparer<T>.Default;

            while (next != null && !comparer.Equals(next.item, value))
            {
                next = next.next;
                if (next == head)
                {
                    return null;
                }
            }
            return next;
        }

        public LinkedListNode<T> FindLast(T value)
        {
            if (IsEmpty)
            {
                return null;
            }

            var current = head.prev;
            var comparer = EqualityComparer<T>.Default;
            while (current != null && !comparer.Equals(current.item, value))
            {
                current = current.prev;
                if (current == head)
                {
                    return null;
                }
            }
            return current;
        }

        /// <summary>
        /// Remove the first item which has the specified value.
        /// </summary>
        /// <param name="item"></param>
        /// <returns>If the item is found, return true; otherwise, false.</returns>
        public bool Remove(T item)
        {
            var toBeRemoved = Find(item);
            if (toBeRemoved != null)
            {
                RemoveNode(toBeRemoved);
                return true;
            }
            return false;
        }

        public void Remove(LinkedListNode<T> node)
        {
            ValidateNode(node);
            RemoveNode(node);
        }

        public void RemoveFirst()
        {
            if (IsEmpty)
            {
                throw new CollectionEmptyException();
            }
            RemoveNode(head);
        }

        public void RemoveLast()
        {
            if (IsEmpty)
            {
                throw new CollectionEmptyException();
            }
            RemoveNode(head.prev);
        }

        void ICollection<T>.Add(T item)
        {
            Append(item);
        }

        bool ICollection<T>.IsReadOnly
        {
            get { return false; }
        }

        #region Private helpers

        private void ValidateNode(LinkedListNode<T> node)
        {
            if (node == null)
            {
                throw new ArgumentNullException("node");
            }

            if (node.list != this)
            {
                throw new InvalidOperationException("External linked list node.");
            }
        }

        private void ValidateNewNode(LinkedListNode<T> node)
        {
            if (node == null)
            {
                throw new ArgumentNullException("node");
            }

            if (node.list != null)
            {
                throw new InvalidOperationException("Linked list node is already attached.");
            }
        }

        private void RemoveNode(LinkedListNode<T> node)
        {
            if (node.next == node)
            {
                head = null;
            }
            else
            {
                node.next.prev = node.prev;
                node.prev.next = node.next;
                if (head == node)
                {
                    head = node.next;
                }
            }
            node.Invalidate();
            size--;
        }

        private void InsertNodeIntoEmptyList(LinkedListNode<T> newNode)
        {
            newNode.next = newNode;
            newNode.prev = newNode;
            head = newNode;

            size++;
        }

        private void InsertNodeBefore(LinkedListNode<T> node, LinkedListNode<T> newNode)
        {
            newNode.next = node;
            newNode.prev = node.prev;
            node.prev.next = newNode;
            node.prev = newNode;
            this.size++;
        }

        #endregion

        #region IEnumerable<T> Impl

        public IEnumerator<T> GetEnumerator()
        {
            LinkedListNode<T> current = head;
            while (current != null)
            {
                yield return current.item;
                
                current = current.next;
                if (current == head)
                {
                    yield break;
                }
            }
        }

        #endregion

        #region IEnumerable Members

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        #endregion

        public LinkedListNode<T> Max()
        {
            if (IsEmpty)
            {
                throw new CollectionEmptyException();
            }

            return Max(First, Last);
        }

        public LinkedListNode<T> Max(LinkedListNode<T> start, LinkedListNode<T> end)
        {
            if (start == null || end == null)
            {
                throw new InvalidOperationException("No elements found in this range.");
            }

            if (start == end)
            {
                return start;
            }

            var comparer = Comparer<T>.Default;
            var defValue = default(T);

            var pos = start;
            var next = start.Next;
            // If T is a reference type
            if (defValue == null)
            {
                while (next != null && next.Previous != end)
                {
                    if (next.Value != null && comparer.Compare(next.Value, pos.Value) > 0)
                    {
                        pos = next;
                    }
                    next = next.Next;
                }
                return pos;
            }
            else
            {
                while (next != null && next.Previous != end)
                {
                    if (comparer.Compare(next.Value, pos.Value) > 0)
                    {
                        pos = next;
                    }
                    next = next.Next;
                }
                return pos;
            }
        }

        #region Sorting
        
        public void SelectionSort()
        {
            if (size < 2) { return; }

            var h = First;
            var t = Last;
            var i = size;
            while (i > 1)
            {
                var nextMax = Max(h, t);
                if (nextMax != t)
                {
                    var temp = t.Value;
                    t.Value = nextMax.Value;
                    nextMax.Value = temp;
                    t = t.Previous;
                }
                i--;
            }
        }

        public void InsertionSort()
        {
            if (size < 2) { return; }

            var comparer = Comparer<T>.Default;

            var next = First.Next;
            while (next != null)
            {
                Console.WriteLine(next.Value);

                var pos = next.Previous;
                while (pos != null && comparer.Compare(next.Value, pos.Value) < 0)
                {
                    pos = pos.Previous;
                }

                if (pos == null)
                {
                    Prepend(next.Value);
                }
                else
                {
                    AddAfter(pos, next.Value);
                }

                var prev = next.Previous;
                Remove(next);
                next = prev.Next;
            }
        }

        #endregion
    }
}
