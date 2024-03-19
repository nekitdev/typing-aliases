"""Various type aliases."""

__description__ = "Various type aliases."
__url__ = "https://github.com/nekitdev/typing-aliases"

__title__ = "typing_aliases"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.9.1"

from typing_aliases.typing import (
    AnyAsyncCallable,
    AnyAsyncContextManager,
    AnyCallable,
    AnyContextManager,
    AnyError,
    AnyErrorType,
    AnyErrorTypes,
    AnyIterable,
    AnyIterator,
    AnySelectors,
    AnySet,
    AnyTuple,
    AnyType,
    AsyncBinary,
    AsyncCallable,
    AsyncCompare,
    AsyncForEach,
    AsyncGenericPredicate,
    AsyncIdentity,
    AsyncInspect,
    AsyncNullary,
    AsyncParse,
    AsyncPredicate,
    AsyncQuaternary,
    AsyncSelectors,
    AsyncTernary,
    AsyncUnary,
    AsyncValidate,
    Attributes,
    Binary,
    Compare,
    Decorator,
    DecoratorIdentity,
    DynamicAsyncCallable,
    DynamicCallable,
    DynamicTuple,
    EmptyTuple,
    ForEach,
    GenericPredicate,
    Headers,
    Identity,
    Inspect,
    IntoAttributes,
    IntoDict,
    IntoHeaders,
    IntoMapping,
    IntoNamespace,
    IntoParameters,
    IntoPath,
    IntoStringDict,
    IntoStringMapping,
    Namespace,
    NormalError,
    NormalErrorType,
    NormalErrorTypes,
    Nullary,
    Pair,
    Pairs,
    Parameters,
    Parse,
    Payload,
    Predicate,
    Primitive,
    Quaternary,
    RecursiveAnyIterable,
    RecursiveAsyncIterable,
    RecursiveIterable,
    Selectors,
    SimpleAsyncContextManager,
    SimpleContextManager,
    StrictPayload,
    StrictPrimitive,
    StringDict,
    StringMapping,
    Ternary,
    Tuple1,
    Tuple2,
    Tuple3,
    Tuple4,
    Tuple5,
    Tuple6,
    Tuple7,
    Tuple8,
    TypeDecorator,
    TypeDecoratorIdentity,
    Unary,
    UnpackBinary,
    UnpackNullary,
    UnpackQuaternary,
    UnpackTernary,
    UnpackUnary,
    Validate,
    is_async_iterable,
    is_async_iterator,
    is_bool,
    is_bytes,
    is_false,
    is_float,
    is_hashable,
    is_instance,
    is_int,
    is_iterable,
    is_iterator,
    is_none,
    is_range,
    is_reversible,
    is_same_or_sub_type,
    is_same_type,
    is_sized,
    is_slice,
    is_string,
    is_subclass,
    is_true,
    required,
)

__all__ = (
    # sets
    "AnySet",
    # types
    "AnyType",
    # tuples
    "EmptyTuple",
    "Tuple1",
    "Tuple2",
    "Tuple3",
    "Tuple4",
    "Tuple5",
    "Tuple6",
    "Tuple7",
    "Tuple8",
    "Pair",
    "DynamicTuple",
    "AnyTuple",
    # errors
    "AnyError",
    "AnyErrorType",
    "NormalError",
    "NormalErrorType",
    "AnyErrorTypes",
    "NormalErrorTypes",
    # context managers
    "AnyContextManager",
    "SimpleContextManager",
    "AnyAsyncContextManager",
    "SimpleAsyncContextManager",
    # functions
    "DynamicCallable",
    "AnyCallable",
    "Nullary",
    "Unary",
    "Binary",
    "Ternary",
    "Quaternary",
    "Identity",
    "Parse",
    "Inspect",
    "ForEach",
    "Validate",
    "Predicate",
    "GenericPredicate",
    "Compare",
    # unpacking functions
    "UnpackNullary",
    "UnpackUnary",
    "UnpackBinary",
    "UnpackTernary",
    "UnpackQuaternary",
    # decorators
    "Decorator",
    "DecoratorIdentity",
    # type decorators
    "TypeDecorator",
    "TypeDecoratorIdentity",
    # async functions
    "AsyncCallable",
    "DynamicAsyncCallable",
    "AnyAsyncCallable",
    "AsyncNullary",
    "AsyncUnary",
    "AsyncBinary",
    "AsyncTernary",
    "AsyncQuaternary",
    "AsyncIdentity",
    "AsyncParse",
    "AsyncInspect",
    "AsyncForEach",
    "AsyncValidate",
    "AsyncPredicate",
    "AsyncGenericPredicate",
    "AsyncCompare",
    # iterables
    "AnyIterable",
    "AnyIterator",
    # selectors
    "Selectors",
    "AsyncSelectors",
    "AnySelectors",
    # recursive iterables
    "RecursiveIterable",
    "RecursiveAsyncIterable",
    "RecursiveAnyIterable",
    # specialization
    "Pairs",
    "StringDict",
    "StringMapping",
    "Attributes",
    "Namespace",
    "Parameters",
    "Headers",
    # specializaion into
    "IntoDict",
    "IntoMapping",
    "IntoStringDict",
    "IntoStringMapping",
    "IntoAttributes",
    "IntoNamespace",
    "IntoParameters",
    "IntoHeaders",
    "IntoPath",
    # payloads
    "Primitive",
    "Payload",
    # strict payloads
    "StrictPrimitive",
    "StrictPayload",
    # iterable type guards
    "is_async_iterable",
    "is_iterable",
    "is_async_iterator",
    "is_iterator",
    "is_reversible",
    # none
    "is_none",
    # builtins
    "is_int",
    "is_float",
    "is_bytes",
    "is_string",
    "is_slice",
    "is_range",
    "is_true",
    "is_false",
    "is_bool",
    # collections
    "is_sized",
    "is_hashable",
    # type guards
    "is_same_type",
    "is_same_or_sub_type",
    # check aliases
    "is_instance",
    "is_subclass",
    # required
    "required",
)
