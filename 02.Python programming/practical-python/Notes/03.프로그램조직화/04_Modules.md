[Contents](../Contents.md) \| [Previous (3.3 Error Checking)](03_Error_checking.md) \| [Next (3.5 Main Module)](05_Main_module.md)

# 3.4 Modules

This section introduces the concept of modules and working functions that span multiple files.

### Modules and import

Any Python source file is a module.

```python
# foo.py
def grok(a):
  ...
def spam(b):
  ...
```

The `import` statements loads and *executes* a module.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

### Namespaces

A moudle is a collection of named values and is sometimes said to be a *namespace*.

The names are all of the global and functions defined in the source file. After importing, the module names is used as a prefix. Hence the *namespace*.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

The module name is directly tied to the file name(foo --> foo.py).

### Global Definitions

Everything defined in the *global scope* is what populates the module snamespace. Considier two modules that define the same variable `x`.

```python
# foo.py
x = 42
def grok(a):
  ...
```

```python
# bar.py
x = 37
def spam(a):
  ...
```

In this case, the `x` definitions refer to different variables. One is `foo.x` and the other is `bar.x`. Different modules can use the same names and those names won't conflic with each other.

**Modules are lsolated**

### Moduels as Environments

Modules form an enclosing environment for all of the code defined inside.

```python
# foo.py
x = 42
def grok(a):
  print(x)
```

*Global* variables are always bound to the enclosing module(same file). Each source file is its own little universe.

#### Module Execution

When a module is imported, *all of the statements in the module execute* one after another until the end of the file is reached. The concepts of the module namespace are all of the *global* names that are still defined at the end of the execution process.

If there are scripting statements that carry out tasks in the global scope(printing, creating files, etc.) you will see them run on import.

**`import as`** statement

You can change the name of a module as you import it:

```python
def retangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    
    return x, y
```

It works the same as a normal import. It just renames the module in that one file.

**`from`** module import

This picks selected symbols out of a module and  makes them available locally.

```python
from math import sin, cos

def rectangular(r, theta):
  x = r.cos(theta)
  y = r.sin(theta)
  return x, y
```

This allows parts of a module to be used without having to type the module prefix. It's usefule for frequentyle used names.

### Comments on importing

Variations on import do *not* change the way that modules work.

```

```



[Contents](../Contents.md) \| [Previous (3.3 Error Checking)](03_Error_checking.md) \| [Next (3.5 Main Module)](05_Main_module.md)