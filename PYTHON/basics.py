# Python string
# always remember pythin strings are immutable so what we are doing is ,
# every time we try to updtae string be are getting either a subset or copy of that string but not changing it..

x = "this isn't is a example string"

# print(x)

# print(f"hello {3}")

# print(x[-1])

# print(len(x))

# ternary operator
# print(type(x)) if x else print("no value of x id there")


# palindrome
# x = "anurag"
# print(x[::-1])

# list_sample = ["anurag", 1, 3, 4, 5]

# lsit_sample_aonther = list()
# lsit_sample_aonther.append(0)

# for item in range(1, 10):
#     lsit_sample_aonther.append(item)

# print(list_sample, lsit_sample_aonther)


# concat two lists

# reformed_list = []

# while True:
#     for i in list_sample:
#         if i not in reformed_list:
#             reformed_list.append(i)
#     for j in lsit_sample_aonther:
#         if j not in reformed_list:
#             reformed_list.append(j)
#     break

# # another effecient way fo writing above code,
# reformed_list = list(set(list_sample + lsit_sample_aonther))
# print(reformed_list)


# example = [1, 4]
# for i in range(*example):
#     print(i)


# # list methods,
# # count method
# example = [1, "2", 3, 4, 5, 5, 6, 7, 9, 8, 10]s

# print(example.count(5))

# # append
# done

# # reverse
# example.reverse()
# print(example)

# # pop (performs operation in list itself)
# print(example.pop(), example)

# list can be treated as both stack and queue)

# # popleft (removes element from left hand side of list)
# example.popleft()
# print(example)

# # list comprehension
# example2 = [i for i in range(0, 10)]
# print(example2)

# # list comprehension can contain nested loops too..
# example3 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
# print(example3)

"""
Asynchronous programming in Python is a method that allows for running multiple tasks and handling I/O operations more efficiently, particularly in web applications and services. It enables the execution of operations in a non-blocking manner, which means that the Python program can continue executing other code while waiting for other tasks (like network responses, file I/O, or database operations) to complete. This is particularly useful for improving performance in IO-bound and high-latency operations.

Understanding Asynchronous Programming

Synchronous vs. Asynchronous

Synchronous Execution: Tasks are executed one after another. Each task must complete before the next one starts. In a blocking I/O operation, the program must wait for the operation to complete before moving on to the next line of code.

Asynchronous Execution: Allows tasks to be executed out of order or in parallel. While waiting for an I/O operation to complete, the program can move on to another task, making better use of the application's runtime.


Key Concepts in Asynchronous Programming :-

Event Loop: The core of asynchronous programs, which manages and distributes the execution of different tasks. It keeps track of all the running tasks and I/O operations, pausing a task when it awaits an I/O operation and resuming it once the operation is complete.

Coroutine: A special function in Python that can pause and resume its execution. Coroutines are defined with async def and can be paused with await when calling other coroutines.

Await: Used to pause the execution of a coroutine until the result of an awaited operation is available. It allows other tasks to run during the wait time.

Future: An object that represents a future result of an asynchronous operation. A future promises to provide a value or result at some point, allowing the program to continue executing.

Task: A scheduled coroutine. The event loop manages tasks, which represent the execution of coroutines in an asynchronous program.


Introduction to Asyncio
asyncio is a Python library used for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives. Here's a breakdown of the main concepts and components:

Core Concepts

Event Loop : 
The central execution device provided by asyncio.
Manages and distributes the execution of different tasks. It loops and keeps track of all the running tasks.

Coroutines : 
Declared with the async def syntax.
These are the functions that you define to do asynchronous operations. They can be suspended and resumed at many points.

Tasks:
Used to schedule coroutines concurrently. When a coroutine is wrapped into a Task with functions like asyncio.create_task(), it's automatically scheduled to run soon.

Futures:
A low-level awaitable object that represents an eventual result of an asynchronous operation. A Task is a subclass of Future.

Awaitables:
Objects that can be used in an await expression. Includes coroutines and Tasks.


Basic Asyncio Patterns

Running an Event Loop:
Use asyncio.run(main()) to run the highest-level entry point function, which should be a coroutine.

Creating and Awaiting Coroutines:
Use await to call async functions; this suspends the calling function until the awaited function is complete.

Task Creation and Management:
Use asyncio.create_task() to run coroutines concurrently as asyncio Tasks.
"""
import asyncio

"""basic example of using asyncio , making an  async approach which says that everything wil once start from an etry point and will fisnish at it breakpoint"""

# async def to_run_in_between(content):
#     await asyncio.sleep(1)
#     print(content)
#     await asyncio.sleep(1)


# async def main():
#     print("starting")

#     await to_run_in_between("hello")

#     await to_run_in_between("world")

#     print("finished")


# asyncio.run(main())


"""now lets see the concurrency the creating tasks from corotuine (functions that will asyncronously run)"""


# async def first_one(arg):
#     await asyncio.sleep(1)
#     print(arg)
#     print("first task completed")


# async def second(arg2):
#     await asyncio.sleep(3)
#     print(arg2)
#     print("second task completed")


# async def main():

#     task1 = asyncio.create_task(first_one("hello"))
#     print("first task started")

#     task2 = asyncio.create_task(second("world"))
#     print("second task started")

#     # await task1
#     # await task2

#     # another way to await foor multiple async or corotuine are by using gather ..

#     await asyncio.gather(task1, task2)


# asyncio.run(main())


"""theres another topic called task groups its bsically used for collectivley runing tasks from sone pool."""

# ----------------------------------------------------------------------------------------------------------------------------

"""
difference between instance object and method object:

    instance objects : 
        the object that we create from class , holds data specific to object like attributes initialised from class.
    
    method objects  : 
        the objects that we create for using methods defined in class using the instance object
"""

# class ExampleForCheck:

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def sum(self):
#         return self.x + self.y

# ex = ExampleForCheck(2, 2)  # instance objects
# metd_ex = ex.sum  # method object

# print(metd_ex())


# ------------------------------------------------------------------------------------------------------------------

"""
    difference between class variable and instance variable :

        class variable : 
            
            variables that are defined in a class that are ** NOT** specific to any instance but commonly available to all instance of classes
            and are accessible to all by class name.
        
        instance variable  : 

            variables that are only specific to an instance of an class and are accessible via that instances name.
"""

# class ExampleForCheck:

#     # class variable
#     name = "ANURAG"

#     def __init__(self, x, y) -> None:
#         # instance variables
#         self.x = x
#         self.y = y

#     # instance method
#     def sum(self):
#         return self.x + self.y


# ex = ExampleForCheck(2, 2)  # instance objects

# print(ex.x, ex.y, ex.sum())
# print(ExampleForCheck.name)


# ----------------------------------------------------------------------------------------------------------------------------

"""
    Private Variables:
        variables whose name start with "_" they are called private variable , we make variables private so that we couldn't accidently update them.
        and when start with __, it becomes the name mangling and interpreter make thire name starts with class name.
        (it even one level of security of variables)
"""

# --------------------------------------------------------------------------------------------------------------------------


