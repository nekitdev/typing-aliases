# Changelog

<!-- changelogging: start -->

## 1.10.0 (2024-03-20)

### Features

- Added `is_iterable_with_iter`.

## 1.9.1 (2024-03-19)

### Fixes

- Exported `is_reversible`.

## 1.9.0 (2024-03-19)

### Features

- Added `is_reversible`.

## 1.8.0 (2024-03-15)

### Changes

- `TypeIs` is now used instead of `TypeGuard` for more precise type narrowing.

## 1.7.1 (2024-02-26)

No significant changes.

## 1.7.0 (2024-02-24)

### Features

- Added `is_sized` and `is_hashable` type guards.

## 1.6.0 (2024-02-08)

### Removals

- Removed `assert_never` as `typing_aliases` provides type aliases along with `typing_extensions`,
  and said function should be imported from `typing_extensions` (or `typing`) instead.

## 1.5.0 (2024-02-08)

### Features

- Re-exported `assert_never` from `typing_extensions`.
  ([#15](https://github.com/nekitdev/typing-aliases/pull/15))

- Improved documentation on re-exports.

## 1.4.1 (2023-12-20)

### Features

- Added `StrictPrimitive` and `StrictPayload` (`Primitive` and `Payload` that exclude `None`).

## 1.4.0 (2023-12-20)

### Features

- Added `required` decorator.

## 1.3.1 (2023-12-01)

### Features

- Exported `AnySet[T]`.

## 1.3.0 (2023-12-01)

### Features

- Added `AnySet[T]`.

## 1.2.0 (2023-11-20)

### Internal

- Migrated to Python 3.8.

## 1.1.3 (2023-06-28)

### Fixes

- `IntoPath` was fixed to work on every supported version.

## 1.1.2 (2023-05-21)

### Fixes

- Fixed `DynamicAsyncCallable[R]` type definition.

## 1.1.1 (2023-05-21)

### Fixes

- Fixed `RecursiveIterable[T]` docs.

## 1.1.0 (2023-05-20)

Overall rewrite.

## 1.0.0 (2022-11-26)

Initial release.
