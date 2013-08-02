using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Algorithms
{
    /// <summary>
    /// From b1, ch 01.
    /// Given N objects and M pairs, this algorithm checks connectivity property of them, and output pairs.
    /// Abstract operations: { 
    ///     find: checks whether a new pair input is connected;
    ///     union: if connection is not found, union two collections; }
    /// These methods use a tree(implemented by an array) to represent the connectivity between objects.
    /// </summary>
    public class Connectivity
    {
        public static int[] QuickFind(List<Tuple<int, int>> pairs)
        {
            var id = new int[pairs.Count * 2];
            for (int i = 0; i < id.Length; i++)
            {
                id[i] = i;
            }
            
            foreach (var pair in pairs)
            {
                int p = pair.Item1, q = pair.Item2;
                if (id[p] == id[q])
                {
                    continue;
                }

                var temp = id[p];
                for (int j = 0; j < id.Length; j++)
                {
                    if (id[j] == temp)
                    {
                        id[j] = id[q];
                    }
                }
                Console.WriteLine("{0} {1}", p, q);
            }

            return id;
        }

        public static int[] QuickUnion(List<Tuple<int, int>> pairs)
        {
            var id = new int[pairs.Count * 2];
            for (var i = 0; i < id.Length; i++)
            {
                // initially every node is its own root now.
                id[i] = i;
            }

            foreach (var pair in pairs)
            {
                int p = pair.Item1, q = pair.Item2;

                // find roots of current nodes;
                int m, n;
                for (m = p; m != id[m]; m = id[m]) { }
                for (n = q; n != id[n]; n = id[n]) { }

                if (m == n) { continue; }
                
                id[m] = n;
                Console.WriteLine("{0} {1}", p, q);
            }

            return id;
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
