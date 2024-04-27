# ScratchForum-BBCode

Convert HTML in the Scratch Forum posts to BBCode easily!

**Note: The converted result may not exactly match with the original post BBCode**

**Note: scratch-blocks cannot be easily converted from their HTML form to text form so this converter will give a weird
text (all the text without any separators) whenever scratch-blocks code is being converted**

## Usage

Install the following dependencies:
```
beautifulsoup4
pygments
```

Then download the `scratch_html_bbcode.py` file in the `src` directory and then import it in your program and use
the `html_to_bbcode(html)` function to convert the HTML

**Example:**

```python
from scratch_html_bbcode import html_to_bbcode

html_string = "<your html string here>"

print(html_to_bbcode(html_string))
```

## Alternatives

**Scratch has an endpoint to get the original BBCode source of a Forum post. You can use it...**

But what if the post ID is unknown? That's why this program was created.

## Bug reporting

Found some bugs? Feel free to open an Issue!

## Thank you!