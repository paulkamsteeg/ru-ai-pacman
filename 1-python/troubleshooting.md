### Troubleshooting

These are some problems (and their solutions) that new python learners
commonly encounter.

-   **Problem:** ImportError: No module named py

    **Solution:** When using `import`, do not include the `.py` from the
    filename. For example, you should say: `import shop` instead of `import shop.py`.

-   **Problem:** NameError: name `variable-name` is not defined.

    **Solution:** Check if you have imported everything that you need (such as `import math`).
    To access a member of a module, you have to type
    `module-name.member-name`, where
    `module-name` is the name of the `.py`file, and
    `member-name` is the name of the variable
    (or function) you are trying to access.

-   **Problem:** TypeError: 'dict' object is not callable

    **Solution:** Dictionary indexing is done using square brackets `[` and `]`, not using
    parenthesis `(` and `)`.

-   **Problem:** ValueError: too many values to unpack

    **Solution:** Make sure the number of variables you are assigning in a
    `for` loop matches the number of elements in each item of
    the list. Similarly for working with tuples.

    For example, if `pair` is a tuple of two elements (e.g.
    `pair = ('apple', 2.0)`) then the following code would
    cause the "too many values to unpack error":
    `a,b,c = pair` because `pair` only contains two elements.

    Here is a problematic scenario involving a `for` loop:

    ```py
    fruits = [('apples', 2.00), ('oranges', 1.50), ('pears', 1.75)]
    for fruit, price, color in fruits:
        print('%s fruit costs %f and is the color %s' % (fruit, price, color))
    ```

-   **Problem:** AttributeError: 'list' object has no attribute 'length' (or
    something similar)

    **Solution:** Finding length of lists is done using `len(lst)` with `lst` a list.

-   **Problem:** Changes to a file are not taking effect.

    **Solution:**

    1.  Make sure you are saving all your files after any changes.

    2.  If you are editing a file in a window different from the one you
        are using to execute python, make sure you
        `reload(your-module)` to
        guarantee your changes are being reflected. `reload`
        works similar to `import`.

### More References!

-   The place to go for more Python information:
    [www.python.org](http://www.python.org/)

-   A good reference book: [Learning
    Python](http://oreilly.com/catalog/9780596513986/)