import sys
from abc import abstractmethod as required
from builtins import isinstance as is_instance
from builtins import issubclass as is_subclass
from os import PathLike
from typing import (
    AbstractSet,
    Any,
    AsyncContextManager,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    Callable,
    ContextManager,
    Dict,
    Hashable,
    Iterable,
    Iterator,
    List,
    Literal,
    Mapping,
    Optional,
    Reversible,
    Sized,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import ParamSpec, TypeIs

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
    "is_iterable_with_iter",
    "is_async_iterator",
    "is_iterator",
    "is_reversible",
    # builtins
    "is_none",
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

# type variables

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

R = TypeVar("R")

P = ParamSpec("P")

# sets

AnySet = AbstractSet[T]
"""Represents any sets."""

# types

AnyType = Type[Any]
"""Represents any types."""

# tuples

EmptyTuple = Tuple[()]
"""Represents empty tuples `()`."""

Tuple1 = Tuple[T]
"""Represents homogeneous 1-tuples `(T)`."""
Tuple2 = Tuple[T, T]
"""Represents homogeneous 2-tuples `(T, T)`."""
Tuple3 = Tuple[T, T, T]
"""Represents homogeneous 3-tuples `(T, T, T)`."""
Tuple4 = Tuple[T, T, T, T]
"""Represents homogeneous 4-tuples `(T, T, T, T)`."""
Tuple5 = Tuple[T, T, T, T, T]
"""Represents homogeneous 5-tuples `(T, T, T, T, T)`."""
Tuple6 = Tuple[T, T, T, T, T, T]
"""Represents homogeneous 6-tuples `(T, T, T, T, T, T)`."""
Tuple7 = Tuple[T, T, T, T, T, T, T]
"""Represents homogeneous 7-tuples `(T, T, T, T, T, T, T)`."""
Tuple8 = Tuple[T, T, T, T, T, T, T, T]
"""Represents homogeneous 8-tuples `(T, T, T, T, T, T, T, T)`."""

Pair = Tuple[T, T]
"""Represents homogeneous pairs `(T, T)`."""

DynamicTuple = Tuple[T, ...]
"""Represents homogeneous tuples of any length `(T, ...)`."""
AnyTuple = DynamicTuple[Any]
"""Represents any tuples `(Any, ...)`."""

# errors

AnyError = BaseException
"""Represents any errors."""
AnyErrorType = Type[AnyError]
"""Represents any error types."""

NormalError = Exception
"""Represents normal errors."""
NormalErrorType = Type[NormalError]
"""Represents normal error types."""

AnyErrorTypes = DynamicTuple[AnyErrorType]
"""Represents tuples of any error types `(AnyErrorType, ...)`."""
NormalErrorTypes = DynamicTuple[NormalErrorType]
"""Represents tuples of normal error types `(NormalErrorType, ...)`."""

# context managers

AnyContextManager = ContextManager[Any]
"""Represents any context managers."""
SimpleContextManager = ContextManager[None]
"""Represents simple context managers that do not return anything on entering."""

AnyAsyncContextManager = AsyncContextManager[Any]
"""Represents any async context managers."""
SimpleAsyncContextManager = AsyncContextManager[None]
"""Represents simple async context managers that do not return anything on entering."""

# functions

DynamicCallable = Callable[..., R]
"""Represents dynamic callables `(...) -> R`."""
AnyCallable = DynamicCallable[Any]
"""Represents any callables `(...) -> Any`."""

Nullary = Callable[[], R]
"""Represents nullary functions `() -> R`."""
Unary = Callable[[T], R]
"""Represents unary functions `(T) -> R`."""
Binary = Callable[[T, U], R]
"""Represents binary functions `(T, U) -> R`."""
Ternary = Callable[[T, U, V], R]
"""Represents ternary functions `(T, U, V) -> R`."""
Quaternary = Callable[[T, U, V, W], R]
"""Represents quaternary functions `(T, U, V, W) -> R`."""

Identity = Unary[T, T]
"""Represents identity functions `(T) -> T`."""

Parse = Unary[str, T]
"""Represents parsing functions `(str) -> T`."""

Inspect = Unary[T, None]
"""Represents inspect functions `(T)`."""

ForEach = Unary[T, None]
"""Represents for-each functions `(T)`."""

Validate = Unary[T, None]
"""Represents validation functions `(T)`."""

Predicate = Unary[T, bool]
"""Represents predicates `(T) -> bool`."""

GenericPredicate = Callable[P, bool]
"""Represents generic predicates `(**P) -> bool`."""

Compare = Binary[T, U, bool]
"""Represents comparison functions `(T, U) -> bool`."""

# unpacking functions

UnpackNullary = Unary[EmptyTuple, R]
"""Represents unpacking nullary functions `(()) -> R`."""
UnpackUnary = Unary[Tuple[T], R]
"""Represents unpacking unary functions `((T)) -> R`."""
UnpackBinary = Unary[Tuple[T, U], R]
"""Represents unpacking binary functions `((T, U)) -> R`."""
UnpackTernary = Unary[Tuple[T, U, V], R]
"""Represents unpacking ternary functions `((T, U, V)) -> R`."""
UnpackQuaternary = Unary[Tuple[T, U, V, W], R]
"""Represents unpacking quaternary functions `((T, U, V, W)) -> R`."""

# decorators

F = TypeVar("F", bound=AnyCallable)
G = TypeVar("G", bound=AnyCallable)

Decorator = Unary[F, G]
"""Represents decorators `(F) -> G`."""
DecoratorIdentity = Identity[F]
"""Represents identity decorators `(F) -> F`."""

# type decorators

C = TypeVar("C", bound=AnyType)
D = TypeVar("D", bound=AnyType)

TypeDecorator = Unary[C, D]
"""Represents type decorators `(C) -> D`."""
TypeDecoratorIdentity = Identity[C]
"""Represents identity type decorators `(C) -> C`."""

# async functions

AsyncCallable = Callable[P, Awaitable[R]]
"""Represents async callables `async (**P) -> R`."""
DynamicAsyncCallable = Callable[..., Awaitable[R]]
"""Represents dynamic async callables `async (...) -> R`."""
AnyAsyncCallable = DynamicAsyncCallable[Any]
"""Represents any async callables `async (...) -> Any`."""

AsyncNullary = Nullary[Awaitable[R]]
"""Represents async nullary functions `async () -> R`."""
AsyncUnary = Unary[T, Awaitable[R]]
"""Represents async unary functions `async (T) -> R`."""
AsyncBinary = Binary[T, U, Awaitable[R]]
"""Represents async binary functions `async (T, U) -> R`."""
AsyncTernary = Ternary[T, U, V, Awaitable[R]]
"""Represents async ternary functions `async (T, U, V) -> R`."""
AsyncQuaternary = Quaternary[T, U, V, W, Awaitable[R]]
"""Represents async quaternary functions `async (T, U, V, W) -> R`."""

AsyncIdentity = AsyncUnary[T, T]
"""Represents async identity functions `async (T) -> T`."""

AsyncParse = AsyncUnary[str, T]
"""Represents parsing functions `async (str) -> T`."""

AsyncInspect = AsyncUnary[T, None]
"""Represents async inspect functions `async (T)`."""

AsyncForEach = AsyncUnary[T, None]
"""Represents async for-each functions `async (T)`."""

AsyncValidate = AsyncUnary[T, None]
"""Represents async validation functions `async (T)`."""

AsyncPredicate = AsyncUnary[T, bool]
"""Represents async predicates `async (T) -> bool`."""

AsyncGenericPredicate = AsyncCallable[P, bool]
"""Represents async generic predicates `async (**P) -> bool`."""

AsyncCompare = AsyncBinary[T, U, bool]
"""Represents async comparison functions `async (T, U) -> bool`."""

# iterables

AnyIterable = Union[AsyncIterable[T], Iterable[T]]
"""Represents any iterable, async or not."""
AnyIterator = Union[AsyncIterator[T], Iterator[T]]
"""Represents any iterator, async or not."""

# selectors

Selectors = Iterable[bool]
"""Represents selectors."""
AsyncSelectors = AsyncIterable[bool]
"""Represents async selectors."""
AnySelectors = AnyIterable[bool]
"""Represents any selectors, async or not."""

# recursive iterables

RecursiveIterable = Union[T, Iterable["RecursiveIterable[T]"]]
"""Represents recursive iterables."""
RecursiveAsyncIterable = Union[T, AsyncIterable["RecursiveAsyncIterable[T]"]]
"""Represents recursive async iterables."""
RecursiveAnyIterable = Union[T, AnyIterable["RecursiveAnyIterable[T]"]]
"""Represents recursive iterables, async or not."""

# specialization

Pairs = Iterable[Tuple[T, U]]
"""Represents iterables of pairs `(T, U)`."""

StringDict = Dict[str, T]
"""Represents string dictionaries."""
StringMapping = Mapping[str, T]
"""Represents string mappings."""

Attributes = StringDict[Any]
"""Represents attributes."""
Namespace = StringDict[Any]
"""Represents namespaces."""

Parameters = StringMapping[Any]
"""Represents parameters."""
Headers = StringMapping[Any]
"""Represents headers."""

Q = TypeVar("Q", bound=Hashable)

IntoDict = Union[Mapping[Q, T], Pairs[Q, T]]
"""Represents types that can be converted into dictionaries."""
IntoMapping = Union[Mapping[T, U], Pairs[T, U]]
"""Represents types that can be converted into mappings."""

IntoStringDict = IntoDict[str, T]
"""Represents types that can be converted into string dictionaries."""
IntoStringMapping = IntoMapping[str, T]
"""Represents types that can be converted into string mappings."""

IntoAttributes = IntoStringDict[Any]
"""Represents types that can be converted into attributes."""
IntoNamespace = IntoStringDict[Any]
"""Represents types that can be converted into namespaces."""

IntoParameters = IntoStringMapping[Any]
"""Represents types that can be converted into parameters."""
IntoHeaders = IntoStringMapping[Any]
"""Represents types that can be converted into headers."""


if sys.version_info >= (3, 9):
    IntoPath = Union[str, PathLike[str]]
    """Represents types that can be converted into [`Path`][pathlib.Path]."""

else:
    IntoPath = Union[str, PathLike]  # type: ignore[type-arg]
    """Represents types that can be converted into [`Path`][pathlib.Path]."""


Primitive = Optional[Union[bool, int, float, str]]
"""Represents primitive types."""

Payload = Union[Primitive, List["Payload"], StringDict["Payload"]]
"""Represents payloads."""

StrictPrimitive = Union[bool, int, float, str]
"""Represents strict pritimive types (which exclude [`None`][None])."""

StrictPayload = Union[StrictPrimitive, List["StrictPayload"], StringDict["StrictPayload"]]
"""Represents strict payloads (which exclude [`None`][None])."""

# iterable type guards


def is_async_iterable(iterable: AnyIterable[T]) -> TypeIs[AsyncIterable[T]]:
    """Checks if an [`AnyIterable[T]`][typing_aliases.typing.AnyIterable] is an
    [`AsyncIterable[T]`][typing.AsyncIterable].

    Arguments:
        iterable: The iterable to check.

    Returns:
        Whether the iterable is an [`AsyncIterable[T]`][typing.AsyncIterable].
    """
    return is_instance(iterable, AsyncIterable)


def is_iterable(iterable: AnyIterable[T]) -> TypeIs[Iterable[T]]:
    """Checks if an [`AnyIterable[T]`][typing_aliases.typing.AnyIterable] is an
    [`Iterable[T]`][typing.Iterable].

    Arguments:
        iterable: The iterable to check.

    Returns:
        Whether the iterable is an [`Iterable[T]`][typing.Iterable].
    """
    return is_instance(iterable, Iterable)


def is_iterable_with_iter(iterable: AnyIterable[T]) -> TypeIs[Iterable[T]]:
    """Checks if an [`AnyIterable[T]`][typing_aliases.typing.AnyIterable] is an
    [`Iterable[T]`][typing.Iterable] via calling [`iter`][iter] on it.

    Arguments:
        iterable: The iterable to check.

    Returns:
        Whether the iterable is an [`Iterable[T]`][typing.Iterable].
    """
    try:
        iter(iterable)  # type: ignore[arg-type]

    except TypeError:
        return False

    else:
        return True


def is_async_iterator(iterator: AnyIterator[T]) -> TypeIs[AsyncIterator[T]]:
    """Checks if an [`AnyIterator[T]`][typing_aliases.typing.AnyIterator] is an
    [`AsyncIterator[T]`][typing.AsyncIterator].

    Arguments:
        iterator: The iterator to check.

    Returns:
        Whether the iterator is an [`AsyncIterator[T]`][typing.AsyncIterator].
    """
    return is_instance(iterator, AsyncIterator)


def is_iterator(iterator: AnyIterator[T]) -> TypeIs[Iterator[T]]:
    """Checks if an [`AnyIterator[T]`][typing_aliases.typing.AnyIterator] is an
    [`Iterator[T]`][typing.Iterator].

    Arguments:
        iterator: The iterator to check.

    Returns:
        Whether the iterator is an [`Iterator[T]`][typing.Iterator].
    """
    return is_instance(iterator, Iterator)


def is_reversible(iterable: Iterable[T]) -> TypeIs[Reversible[T]]:
    """Checks if the given iterable is reversible.

    Arguments:
        iterable: The iterable to check.

    Returns:
        Whether the given iterable is reversible.
    """
    return is_instance(iterable, Reversible)


# builtins


def is_none(item: Any) -> TypeIs[None]:
    """Checks if the given item is [`None`][None].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is [`None`][None].
    """
    return item is None


def is_int(item: Any) -> TypeIs[int]:
    """Checks if the given item is of type [`int`][int].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`int`][int].
    """
    return is_instance(item, int)


def is_float(item: Any) -> TypeIs[float]:
    """Checks if the given item is of type [`float`][float].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`float`][float].
    """
    return is_instance(item, float)


def is_bytes(item: Any) -> TypeIs[bytes]:
    """Checks if the given item is of type [`bytes`][bytes].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`bytes`][bytes].
    """
    return is_instance(item, bytes)


def is_string(item: Any) -> TypeIs[str]:
    """Checks if the given item is of type [`str`][str].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`str`][str].
    """
    return is_instance(item, str)


def is_slice(item: Any) -> TypeIs[slice]:
    """Checks if the given item is of type [`slice`][slice].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`slice`][slice].
    """
    return is_instance(item, slice)


def is_range(item: Any) -> TypeIs[range]:
    """Checks if the given item is of type [`range`][range].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`range`][range].
    """
    return is_instance(item, range)


def is_true(item: Any) -> TypeIs[Literal[True]]:
    """Checks if the given `item` is [`True`][True].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is [`True`][True].
    """
    return item is True


def is_false(item: Any) -> TypeIs[Literal[False]]:
    """Checks if the given `item` is [`False`][False].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is [`False`][False].
    """
    return item is False


def is_bool(item: Any) -> TypeIs[bool]:
    """Checks if the given item is of type [`bool`][bool].

    This is equivalent to:

    ```python
    is_true(item) or is_false(item)
    ```

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is of type [`bool`][bool].
    """
    return is_true(item) or is_false(item)


# collections


def is_sized(item: Any) -> TypeIs[Sized]:
    """Checks if the given item is sized.

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is sized.
    """
    return is_instance(item, Sized)


def is_hashable(item: Any) -> TypeIs[Hashable]:
    """Checks if the given item is hashable.

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is hashable.
    """
    return is_instance(item, Hashable)


# type guards


def is_same_type(item: Any, other: T) -> TypeIs[T]:
    """Checks if the item is of the same type `T` as the other item.

    Arguments:
        item: The item to check.
        other: The other item to check against.

    Returns:
        Whether the item is of the same type `T` as the other item.
    """
    return type(item) is type(other)


def is_same_or_sub_type(item: Any, other: T) -> TypeIs[T]:
    """Checks if the item is of the sub- or same type `T` as the other item.

    Arguments:
        item: The item to check.
        other: The other item to check against.

    Returns:
        Whether the item is of the sub- or same type `T` as the other item.
    """
    return is_instance(item, type(other))
