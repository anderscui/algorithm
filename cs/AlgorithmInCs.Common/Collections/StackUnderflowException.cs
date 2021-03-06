﻿using System;

namespace Andersc.AlgorithmInCs.Common.Collections
{
    [Serializable]
    public class StackUnderflowException : InvalidOperationException
    {
        public StackUnderflowException() { }
        public StackUnderflowException(string message) : base(message) { }
        public StackUnderflowException(string message, Exception inner) : base(message, inner) { }
        protected StackUnderflowException(
          System.Runtime.Serialization.SerializationInfo info,
          System.Runtime.Serialization.StreamingContext context)
            : base(info, context) { }
    }
}
