using System;
using System.Collections.Generic;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    public class Stack<T> : IEnumerable<T>
    {
        //private static T[] emptyArray = new T[0];
        private static readonly int DefaultCapacity = 4;

        private T[] items;
        private int size;

        #region Constructors

//        static Stack()
//        {
//            emptyArray = new T[0];
//        }

        public Stack() : this(DefaultCapacity) 
        {}

        public Stack(int capacity)
        {
            if (capacity < 0) { throw new ArgumentOutOfRangeException("The capacity must not be negative."); }

            items = new T[capacity];
            size = 0;
        }

        public Stack(IEnumerable<T> enumerable)
        {
            if (enumerable.IsNull())
            {
                throw new ArgumentNullException("enumerable");
            }

            var collection = enumerable as ICollection<T>;
            if (collection.IsNotNull())
            {
                int count = collection.Count;
                items = new T[count];
                collection.CopyTo(items, 0);
                size = count;
                return;
            }

            items = new T[DefaultCapacity];
            size = 0;
            foreach (var item in enumerable)
            {
                Push(item);
            }
        }

        #endregion

        public bool IsEmpty
        {
            get { return (size == 0); }
        }

        public int Count
        {
            get { return size; }
        }

        public T Top
        {
            get
            {
                if (IsEmpty)
                {
                    throw new CollectionEmptyException("The stack is empty");
                }

                return items[size - 1];
            }
        }

        public void Push(T item)
        {
            if (size == items.Length)
            {
                var newCapacity = IsEmpty ? DefaultCapacity : items.Length * 2;
                var array = new T[newCapacity];
                Array.Copy(items, array, size);
                items = array;
            }

            items[size++] = item;
        }

        public T Pop()
        {
            if (IsEmpty)
            {
                throw new StackUnderflowException();
            }

            var result = items[--size];
            items[size] = default(T);
            return result;
        }

        public void Clear()
        {
            Array.Clear(items, 0, size);
            size = 0;
        }

        #region IEnumerable<T> Members

        public IEnumerator<T> GetEnumerator()
        {
            for (int i = size - 1; i >= 0; i--)
            {
                yield return items[i];
            }
        }

        #endregion

        #region IEnumerable Members

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        #endregion
    }
}
