# https://www.pluralsight.com/guides/explore-python-libraries:-mypy
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Any, Union, Iterable, Mapping, MutableMapping, Sequence, Callable, Iterator, Optional

a: int = 10
b: float = 20.22
c: bool = True
d: str = 'yokesh'
e: bytes = b'hello'
f: bytearray = bytearray(b'\x02\x03\x05\x07')

# open terminal and use 'mypy TypingModule.py' to run this file using mypy interpreter

# Similarly, we can use list,tuple,dict,set,frozenset also

x_list: list = [1,4.21,'string'] # typically equals to list[Any]
print(x_list)

# NOTE : Can write list / list[Any] , import Any from typing module
# Use Any if you don't know the type of something or it's too
# dynamic to write a type for

y_list: list[Any] = [1,6.43,'hello']
print(y_list)


# If you don't know exactly the size of list and you know the type of all items in the list

z_list: list[float] = [3.12,4.22,99.89]
print(z_list)

# If you don't know exactly the size of list and you don't know the types of items in the list use 'Any'

w_list: list[Any] = ['ok',2,4,6.32,b'hello']
print(w_list)

# If you know the size of the list and elements type, use '|' instead of Union[int,float,str]
# Use Union when something could be one of a few types

u_list: list[int | float | str] = [2,2.00,'two']
print(u_list)

# Union also works,
uu_list: list[int | float | str] = [2,2.00,'two']
print(uu_list)

print("*******************************************************************")
empty_tuple: tuple[()] =()  # Empty Tuple
print(empty_tuple)

x_tuple: tuple = (1,4.21,'string') # typically equals to tuple[Any]
print(x_tuple)

# NOTE : Can write tuple / tuple[Any] , import Any from typing module
# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
# Use Union when something could be one of a few types
y_tuple: tuple[int | float | str , ...] = (1,6.43,'hello')
print(y_tuple)


# If you don't know exactly the size of tuple and you know the type of all items in the list

z_tuple: tuple[float,...] = (3.12,4.22,99.89)
print(z_tuple)

# If you don't know exactly the size of list and you don't know the types of items in the list use 'Any'

w_tuple: tuple[Any, ...] = ('ok',2,4,6.32,b'hello')
print(w_tuple)

u_tuple: tuple[int,float,str] = (2,2.00,'two')
print(u_tuple)

print("*******************************************************************")
# Have you noticed that we cannot use ellipses on list data type . Why??
# According to python docs, list accepts homogenous data types and tuples accepts heterogeneous types
# Homogenous means data of same type like cow milk, buffalo milk, goat milk etc.
# Heterogeneous means different data related with each other as, ('john', 'doe','abraham') which ressembles
# first name, middle name, last name.
# # My question on stackoverflow :
# https://stackoverflow.com/questions/72919422/listint-is-not-working-while-tupleint-is-working-while-im-using-m/72920075#72920075
# Due to their individual properties(homo and hetero) list() constructor did not have ellipses and tuple() supports
# ellipses.
# Go and see list() and tuple() documentation in python docs 3.10.4 for more info.
print("*******************************************************************")

x_dict: dict = {'hello':1,'two':2,3.21:'some float',True:'some bool'}
print(x_dict)

# Use Union when something could be one of a few types

y_dict: dict[str | float | bool , int | str] = {'hello':1,'two':2,3.21:'some float',True:'some bool'}
print(y_dict)

yy_dict: dict[Union[str,float,bool] , Union[int,str]] = {'hello':1,'two':2,3.21:'some float',True:'some bool'}
print(yy_dict)

z_dict: dict[Any , Any] = {'hello':1,'two':2,3.21:'some float',True:'some bool'}
print(z_dict)

# The above x_dict, y_dict, yy_dict and z_dict are equal, we can use any of the format

print("*******************************************************************")

x_set: set[int] = {1,2,3}
print(x_set)

y_set: set[Any] = {1,2.21,'my set',False}
print(y_set)

# Use Union when something could be one of a few types

z_set: set[int | float] = {1,21,3.21}
print(z_set)

p_set: set[Union[int,float]] = {1,21,3.21}
print(p_set)

print("*******************************************************************")
# Iterable can be used in place of any iterables like list,tuple,set,dicts etc
# Iterable[data_type] : iterable object containing ints
# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
it: Iterable = [1,2,3]
print(it)

it1: Iterable = (1,2,3)
print(it)

it2: Iterable = {'one':1, 'two':2}
print(it2)

it3: Iterable = {'one',432,2.21,True}
print(it3)

it4: Iterable = frozenset({'one',432,2.21,True})
print(it4)

# Can use Iterable[type] also as,
it5 : Iterable[int] = [1,2,3,4]
print(it5)

it6 : Iterable[int] = (1,2,3,4)
print(it6)

# it7: Iterable[int] = [1,2,3,4,5,6]
# print(it7)

# it8: Iterable[int, ...] = (1,2,3,4)
# print(it8)

# The above both examples gives error by mypy, for a single item / multiple items use Iterable[type] only.

# Can use 'Any' in Iterable, if we don't know the all types of items in the iterable.

it7: Iterable[Any] = [1,2,3]
print(it7)

it8:Iterable[Any] = (1,2,3)
print(it8)

# Use Union or '|' if Iterable contains variable countable types:
# Use Union when something could be one of a few types

it9 : Iterable[int | str | float] = [1,3.22,'yokesh']  # Can use Union[int,float,str]
print(it9)

it10 : Iterable[int | str | float] = ('hello world',999,0.321) # Can use Union[int,float,str]
print(it10)

print("*******************************************************************")

# object for all data types
# NOTE : object should not be given any types in square brackets like object[type1,type2]

o1: object = [1,2,3]
print(o1)

o2: object = (1,2,3)
print(o2)

o3: object = {'one':1,'two':2,'three':3}
print(o3)

o4: object = {1,2,3}
print(o4)

o5: object = frozenset({1,2,3})
print(o5)

print("*******************************************************************")

# Mapping[key,value] : mapping from str keys to int values (read-only)
# Use Mapping for dictionary types
# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
map1: Mapping[Any,Any] = {'one':1,2:'two',3.3:'float 3 point 3'}
print(map1)

map2: Mapping[str,int] = {'one':1,'two':2,'three':3}
print(map1)

map3: Mapping[str,str] = {'one':'numeric one','two':'numeric two','three':'numeric three'}
print(map3)

print("*******************************************************************")
# map4: Mapping[int,str] = {1:'one',2:'two'}
# map4[2] = 'numeric two'
# print(map4)
# Un commenting above line raises error as Mapping[] only implements __getitem__ but not __setitem__
# So, Use MutableMapping to clear the error,

map4: MutableMapping[int,str] = {1:'one',2:'two'}
map4[2] = 'numeric two'
print(map4)

print("*******************************************************************")
# Learn more about differences b/w iterables and sequences from below link :
# https://stackoverflow.com/questions/72157296/python-iterable-vs-sequence#:~:text=Iterable%20is%20any%20object%20that,calls%20the%20two%20required%20methods.

# Sequence[bool]  : sequence of booleans (read-only)

seq1: Sequence = [True,False,21]
print(seq1)

seq11: Sequence[bool | int] = [True,False,21]
print(seq11)

seq111: Sequence[Any] = [True,False,21]
print(seq111)

# All 3 sequences are same mentioned above

seq2: Sequence = (True,False,21)
print(seq2)

seq22: Sequence[bool | int] = (True,False,21)
print(seq22)

seq222: Sequence[Any] = (True,False,21)
print(seq222)

# seq3: Sequence[str,int] = {'one':1,'two':2}
# print(seq3)
# o/p:Incompatible types in assignment(expression has type "Dict[str, int]",variable has type "Sequence[Any]")
# dict() is not a sequence

# seq4: Sequence = {True,False,21}
# print(seq4)
# Sets are not sequences so mypy raises error if we run above example

print("*******************************************************************")
# NOTE : Iterable, Sequence, Mapping can be imported from collections.abc module instead from typing module
print("*******************************************************************")

print("*******************************************************************")
# Function Annotations :


def func1(a: int, b: int) -> None:

    print(a+b)


func1(2,3)


def func2(a: int, b:Any) -> str:

    return str(b)+str(a)


print(func2(10,'ok'))


call_alias: Callable[[int,Any],str] = func2
# Callable is used to create alias for a function
# Syntax : Callable[[inputs],output]
print(call_alias(10,'ok'))

# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it


def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


for item in g(5):
    print(item)


# What about iterators ?

iter_one: Iterator[int] = iter([1,2,3,4,5])
for data in iter_one:
    print(data)

iter_two: Iterator[str | int] = iter(['hello',321])
for value in iter_two:
    print(value)

print("*******************************************************************")
# What is Optional[] do ?
# “Optional[str] is just a shorthand or alias for Union[str, None].
# It exists mostly as a convenience to help function signatures look a little cleaner.”
# https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint
# Optional[...] is a shorthand notation for Union[..., None], telling the type checker
# that either an object of the specific type is required, or None is required.

# So, Optional[str] == Union[str,None] == str | None

# All functions by default has a return type of 'None'


def func3(x: Optional[list[int]]) -> None:

    print(x)


func3(None)
func3([1,2,3])

# The above func3 says, takes 1 parameter named 'x' that accepts list[int] or None and returns None by default


def func4(x: Union[list[int],None]) -> None:

    print(x)


func4(None)
func4([1,2,3])

# Both func3 and func4 do the same thing as Optional[list[int]] == Union[list[int],None]

# All default args in a function is of type Optional[<type>]


class Yok:
    pass


def some_func(params: Yok = None):
    print(params)


some_func(params = Yok())

# Hover on params in line 335, it shows params of type Yok | None ,
# Yok | None == Optional[Yok] == Union[Yok,None]

# You can of course split a function annotation over multiple lines


def send_email(address: Union[str, list[str]],
               sender: str,
               cc: Optional[list[str]],
               bcc: Optional[list[str]],
               subject='',
               body: Optional[list[str]] = None
               ) -> bool:

               return True


print(send_email('india','yokesh',None,None,'anniversary'))

print("*******************************************************************")
# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
# print(reveal_type([1,2,3]))
# output of the above line is given by mypy interpreter as,
# OUTPUT = note: Revealed type is "builtins.list[builtins.int]"

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing a type annotation
mangoes_list: list[str] = []
lollipop: Optional[str] = None

# print(reveal_type(mangoes_list))
# print(reveal_type(lollipop))
# TypingModule.py:373: note: Revealed type is "builtins.list[builtins.str]"
# TypingModule.py:374: note: Revealed type is "Union[builtins.str, None]"

print("*******************************************************************")
















