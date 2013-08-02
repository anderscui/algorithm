using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Algorithms
{
    /// <summary>
    /// From book1.
    /// </summary>
    public class Connectivity
    {
        public static int[] QuickFind(List<Tuple<int, int>> pairs)
        {
            var arr = new int[pairs.Count * 2];
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = i;
            }
            
            foreach (var pair in pairs)
            {
                int p = pair.Item1, q = pair.Item2;
                if (arr[p] == arr[q])
                {
                    continue;
                }

                var temp = arr[p];
                for (int j = 0; j < arr.Length; j++)
                {
                    if (arr[j] == temp)
                    {
                        arr[j] = arr[q];
                    }
                }
                Console.WriteLine("{0} {1}", p, q);
            }

            return arr;
        }

        public static int[] QuickUnion(List<Tuple<int, int>> pairs)
        {
            var arr = new int[pairs.Count * 2];
            for (var i = 0; i < arr.Length; i++)
            {
                // initially every node is its own root now.
                arr[i] = i;
            }

            foreach (var pair in pairs)
            {
                int p = pair.Item1, q = pair.Item2;

                // find roots of current nodes;
                int m, n;
                for (m = p; m != arr[m]; m = arr[m]) { }
                for (n = q; n != arr[n]; n = arr[n]) { }

                if (m == n) { continue; }
                
                arr[m] = n;
                Console.WriteLine("{0} {1}", p, q);
            }

            return arr;
        }

        public static int[] WeightedQuickUnion(List<Tuple<int, int>> pairs)
        {
            var id = new int[pairs.Count * 2];
            var sz = new int[id.Length];
            for (var i = 0; i < id.Length; i++)
            {
                // initially every node is its own root now.
                id[i] = i;
                // and every "tree" has only one single node.
                sz[i] = 1;
            }

            foreach (var pair in pairs)
            {
                int p = pair.Item1, q = pair.Item2;

                // find roots of current nodes;
                int m, n;
                for (m = p; m != id[m]; m = id[m]) { }
                for (n = q; n != id[n]; n = id[n]) { }

                if (m == n) { continue; }

                // always attach the smaller tree to the bigger one.
                if (sz[m] < sz[n])
                {
                    id[m] = n;
                    sz[n] += sz[m];
                }
                else
                {
                    id[n] = m;
                    sz[m] += sz[n];
                }
                Console.WriteLine("{0} {1}", p, q);
            }

            return id;
        }
    }
}
