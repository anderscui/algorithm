using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Andersc.AlgorithmInCs.Common;

namespace Andersc.AlgorithmInCs.Algorithms.Sorting
{
    public class LinkedListSorter
    {
        /// <summary>
        /// Refer to [Sed12] 6.16
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        public static LinkedList<int> Selection(LinkedList<int> list)
        {
            if (list.IsNull())
            {
                return null;
            }

            var outList = new LinkedList<int>();
            while (list.Any())
            {
                var node = list.First;
                var max = node;
                while (node.Next != null)
                {
                    node = node.Next;
                    if (node.Value > max.Value)
                    {
                        max = node;
                    }
                }
                list.Remove(max);
                outList.AddFirst(max);
            }

            return outList;
        }
    }
}
