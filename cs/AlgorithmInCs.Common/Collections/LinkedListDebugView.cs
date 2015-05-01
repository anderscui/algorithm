using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    internal class LinkedListDebugView<T>
    {
        private LinkedList<T> list;

        [DebuggerBrowsable(DebuggerBrowsableState.RootHidden)]
        public T[] Items
        {
            get { return list.ToArray(); }
        }

        public LinkedListDebugView(LinkedList<T> list)
        {
            if (list == null)
            {
                throw new ArgumentNullException("list");
            }
            this.list = list;
        }
    }
}
