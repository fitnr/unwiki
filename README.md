unwiki
======
Python module to remove wiki markup text.

Unwiki has two methods: `unwiki.load` and `unwiki.loads`

````python
>>> import unwiki

>>> unwiki.loads("[[Wiki Link]]")
"Wiki Link"

>>> with open('wiki.txt') as f:
... result = unwiki.load(f)
````

Use the `compress_spaces` option to remove extra spaces that may sneak in:
```python
>>> unwiki.loads("[[Wiki Link]] {{template}} more")
"Wiki Link  more"

>>> unwiki.loads("[[Wiki Link]] {{template}} more", compress_spaces=True)
"Wiki Link more"
```

## License

GNU Public License. See LICENSE.txt for more.

Inspired by [dewiki](https://github.com/daddyd/dewiki) by Dirk Dierickx.
