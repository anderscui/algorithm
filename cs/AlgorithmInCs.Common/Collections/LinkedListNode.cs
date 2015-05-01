using System;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    // TODO: ISerializable
    [Serializable]
    public sealed class LinkedListNode<T>
    {
        internal LinkedList<T> list;
        internal LinkedListNode<T> next;
        internal LinkedListNode<T> prev;
        internal T item;

        public LinkedListNode(T value)
        {
            item = value;
        }

        internal LinkedListNode(LinkedList<T> list, T value)
        {
            this.list = list;
            this.item = value;
        }

        public LinkedList<T> List
        {
            get
            {
                return list;
            }
        }

        public T Value
        {
            get { return item; }
            set { item = value; }
        }

        public LinkedListNode<T> Next
        {
            get
            {
                if (next != null && next != list.head)
                {
                    return next;
                }
                return null;
            }
        }

        public LinkedListNode<T> Previous
        {
            get
            {
                if (prev != null && this != list.head)
                {
                    return prev;
                }
                return null;
            }
        }

        internal void Invalidate()
        {
            list = null;
            next = null;
            prev = null;
        }
    }
}
