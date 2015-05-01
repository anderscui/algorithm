using System;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    [Serializable]
    public class CollectionEmptyException : InvalidOperationException
    {
        public CollectionEmptyException() { }
        public CollectionEmptyException(string message) : base(message) { }
        public CollectionEmptyException(string message, Exception inner) : base(message, inner) { }
    }
}
