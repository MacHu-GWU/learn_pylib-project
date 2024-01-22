Circular Reference Factory Method
==============================================================================
有的时候我们会在两个模块中定义两个不同的类. 如果在需要 type hint 的场合就可以用 ``if typing.TYPE_CHECKING:`` 的技巧引入 type hint. 但有的时候, 我们需要让两个类互相转化. 例如, 让 A 类的实例 + 上一些数据变成 B 类. 这种情况有下面几种做法:

1. 是在 A 中创建一个普通方法 ``def to_b(self) -> "B"``
2. 是在 B 中创建一个 ``@classmethod`` ``def from_a(cls, a: "A") -> "B"``.
3. 是单独创建两个函数 ``def from_a_to_b(a: "A") -> "B":`` 和 ``def from_b_to_a(b: "B") -> "A":``.

这具体该用哪个方法呢?

这里我们首先强调一下前提条件. 如果我们把两个类放在一个模块内, 则不存在循环引用的问题, 那么我们怎么做都可以.

然后我们思考一下, 如果我们用 3 的话. 那显然是可以的. 只不过我们在使用 A, B 两个类的时候需要单独 import 这两个函数, 比较麻烦. 那有没有只用到 A, B 两个类的方法, 又能避免循环引用呢?

答案是用工厂函数. 也就是说, 你不要实现 ``def to_a(self, ...)``, ``def to_b(self, ...)``, 而是实现 ``def from_a(cls, ...)``, def from_b(cls, ...)`` 这两个工厂函数. 我们拿 A 类举例, 我们需要把 B 转化为 A. 那么就可以实现一个 ``def from_b(cls, b: "B")`` 的 ``@classmethod``. 里面的 b 的 type hint 可以继续用 ``if typing.TYPE_CHECKING:`` 的技巧, 不需要真正的 import. 如果你要给 B 类实现 ``def to_a(self, ...)``, 这样就必须真正 import A, 因为你需要用 A 这个类来初始化. 这样就会导致循环引用. 下面的三个模块共同给出了示例代码.

``module_a.py``

.. literalinclude:: ./module_a.py
   :language: python
   :linenos:

``module_b.py``

.. literalinclude:: ./module_b.py
   :language: python
   :linenos:

``test.py``

.. literalinclude:: ./test.py
   :language: python
   :linenos:
