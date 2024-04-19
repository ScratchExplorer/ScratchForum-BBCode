import time
from bs4 import BeautifulSoup
from pygments.lexers import guess_lexer

html = """<span class="bb-bold">Hello!</span><br><br><span class="bb-italic">Test!</span><br><br><span class="bb-underline">123</span><br><br><span class="bb-strikethrough">Stroke</span><br><br><br><br><a href="http://efgh">ijkl</a><br><br><span class="bb-big">BIG</span><br><br><span class="bb-small">SMALL</span><br><br><ul><li> 123<br></li><li> 456<br></li><li> 789<br></li></ul><br><ol><li> 123<br></li><li> 456<br></li><li> 789<br></li></ol><br><blockquote>abcd</blockquote><br><img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/neutral.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/smile.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/sad.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/yikes.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/wink.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/hmm.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/lol.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/tongue.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/mad.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/roll.png"> <img src="//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/cool.png"><br><br><div class="code"><pre><span class="n">Test</span> <span class="n">test</span>
</pre></div><br><div class="code"><pre>import os\n\nprint("Hello!")</pre></div><br><pre class="blocks"><div class="scratchblocks"><svg version="1.1" width="127" height="91"><defs><filter id="bevelFilter" x0="-50%" y0="-50%" width="200%" height="200%"><feGaussianBlur result="blur-1" in="SourceAlpha" stdDeviation="1 1"></feGaussianBlur><feFlood result="flood-2" in="undefined" flood-color="#fff" flood-opacity="0.15"></feFlood><feOffset result="offset-3" in="blur-1" dx="1" dy="1"></feOffset><feComposite result="comp-4" operator="arithmetic" in="SourceAlpha" in2="offset-3" k2="1" k3="-1"></feComposite><feComposite result="comp-5" operator="in" in="flood-2" in2="comp-4"></feComposite><feFlood result="flood-6" in="undefined" flood-color="#000" flood-opacity="0.7"></feFlood><feOffset result="offset-7" in="blur-1" dx="-1" dy="-1"></feOffset><feComposite result="comp-8" operator="arithmetic" in="SourceAlpha" in2="offset-7" k2="1" k3="-1"></feComposite><feComposite result="comp-9" operator="in" in="flood-6" in2="comp-8"></feComposite><feMerge result="merge-10"><feMergeNode in="SourceGraphic"></feMergeNode><feMergeNode in="comp-5"></feMergeNode><feMergeNode in="comp-9"></feMergeNode></feMerge></filter><filter id="inputBevelFilter" x0="-50%" y0="-50%" width="200%" height="200%"><feGaussianBlur result="blur-1" in="SourceAlpha" stdDeviation="1 1"></feGaussianBlur><feFlood result="flood-2" in="undefined" flood-color="#fff" flood-opacity="0.15"></feFlood><feOffset result="offset-3" in="blur-1" dx="-1" dy="-1"></feOffset><feComposite result="comp-4" operator="arithmetic" in="SourceAlpha" in2="offset-3" k2="1" k3="-1"></feComposite><feComposite result="comp-5" operator="in" in="flood-2" in2="comp-4"></feComposite><feFlood result="flood-6" in="undefined" flood-color="#000" flood-opacity="0.7"></feFlood><feOffset result="offset-7" in="blur-1" dx="1" dy="1"></feOffset><feComposite result="comp-8" operator="arithmetic" in="SourceAlpha" in2="offset-7" k2="1" k3="-1"></feComposite><feComposite result="comp-9" operator="in" in="flood-6" in2="comp-8"></feComposite><feMerge result="merge-10"><feMergeNode in="SourceGraphic"></feMergeNode><feMergeNode in="comp-5"></feMergeNode><feMergeNode in="comp-9"></feMergeNode></feMerge></filter><filter id="inputDarkFilter" x0="-50%" y0="-50%" width="200%" height="200%"><feFlood result="flood-1" in="undefined" flood-color="#000" flood-opacity="0.2"></feFlood><feComposite result="comp-2" operator="in" in="flood-1" in2="SourceAlpha"></feComposite><feMerge result="merge-3"><feMergeNode in="SourceGraphic"></feMergeNode><feMergeNode in="comp-2"></feMergeNode></feMerge></filter><path d="M1.504 21L0 19.493 4.567 0h1.948l-.5 2.418s1.002-.502 3.006 0c2.006.503 3.008 2.01 6.517 2.01 3.508 0 4.463-.545 4.463-.545l-.823 9.892s-2.137 1.005-5.144.696c-3.007-.307-3.007-2.007-6.014-2.51-3.008-.502-4.512.503-4.512.503L1.504 21z" fill="#3f8d15" id="greenFlag"></path><path d="M6.724 0C3.01 0 0 2.91 0 6.5c0 2.316 1.253 4.35 3.14 5.5H5.17v-1.256C3.364 10.126 2.07 8.46 2.07 6.5 2.07 4.015 4.152 2 6.723 2c1.14 0 2.184.396 2.993 1.053L8.31 4.13c-.45.344-.398.826.11 1.08L15 8.5 13.858.992c-.083-.547-.514-.714-.963-.37l-1.532 1.172A6.825 6.825 0 0 0 6.723 0z" fill="#fff" id="turnRight"></path><path d="M3.637 1.794A6.825 6.825 0 0 1 8.277 0C11.99 0 15 2.91 15 6.5c0 2.316-1.253 4.35-3.14 5.5H9.83v-1.256c1.808-.618 3.103-2.285 3.103-4.244 0-2.485-2.083-4.5-4.654-4.5-1.14 0-2.184.396-2.993 1.053L6.69 4.13c.45.344.398.826-.11 1.08L0 8.5 1.142.992c.083-.547.514-.714.963-.37l1.532 1.172z" fill="#fff" id="turnLeft"></path><path d="M0 0L4 4L0 8Z" fill="#111" id="addInput"></path><path d="M4 0L4 8L0 4Z" fill="#111" id="delInput"></path><g id="loopArrow"><path d="M8 0l2 -2l0 -3l3 0l-4 -5l-4 5l3 0l0 3l-8 0l0 2" fill="#000" opacity="0.3"></path><path d="M8 0l2 -2l0 -3l3 0l-4 -5l-4 5l3 0l0 3l-8 0l0 2" fill="#fff" opacity="0.9" transform="translate(-1 -1)"></path></g></defs><g><g transform="translate(0 0)"><g transform="translate(2 0)"><path d="M 0 3 L 3 0 L 13 0 L 16 3 L 24 3 L 27 0 L 93 0 L 96 3 L 96 19 L 93 22 L 27 22 L 24 25 L 16 25 L 13 22 L 3 22 L 0 19 Z" class="sb-motion sb-bevel"></path><text x="0" y="10" class="sb-label " transform="translate(6 5)">move</text><g transform="translate(36 4)"><path d="M 6.5 0 L 17.5 0 A 6.5 6.5 0 0 1 17.5 13 L 6.5 13 A 6.5 6.5 0 0 1 6.5 0 Z" class="sb-input sb-input-number"></path><text x="0" y="10" class="sb-label sb-literal-number" transform="translate(5 0)">123</text></g><text x="0" y="10" class="sb-label " transform="translate(64 5)">steps</text></g><g transform="translate(2 22)"><path d="M 0 3 L 3 0 L 13 0 L 16 3 L 24 3 L 27 0 L 107 0 L 110 3 L 110 19 L 107 22 L 27 22 L 24 25 L 16 25 L 13 22 L 3 22 L 0 19 Z" class="sb-motion sb-bevel"></path><text x="0" y="10" class="sb-label " transform="translate(6 5)">turn</text><use xlink:href="#turnRight" transform="translate(29 6)"></use><g transform="translate(48 4)"><path d="M 6.5 0 L 7.5 0 A 6.5 6.5 0 0 1 7.5 13 L 6.5 13 A 6.5 6.5 0 0 1 6.5 0 Z" class="sb-input sb-input-number"></path><text x="0" y="10" class="sb-label sb-literal-number" transform="translate(5 0)"></text></g><text x="0" y="10" class="sb-label " transform="translate(66 5)">degrees</text></g><g transform="translate(2 44)"><path d="M 0 3 L 3 0 L 13 0 L 16 3 L 24 3 L 27 0 L 107 0 L 110 3 L 110 19 L 107 22 L 27 22 L 24 25 L 16 25 L 13 22 L 3 22 L 0 19 Z" class="sb-motion sb-bevel"></path><text x="0" y="10" class="sb-label " transform="translate(6 5)">turn</text><use xlink:href="#turnLeft" transform="translate(29 6)"></use><g transform="translate(48 4)"><path d="M 6.5 0 L 7.5 0 A 6.5 6.5 0 0 1 7.5 13 L 6.5 13 A 6.5 6.5 0 0 1 6.5 0 Z" class="sb-input sb-input-number"></path><text x="0" y="10" class="sb-label sb-literal-number" transform="translate(5 0)"></text></g><text x="0" y="10" class="sb-label " transform="translate(66 5)">degrees</text></g><g transform="translate(2 66)"><path d="M 0 3 L 3 0 L 13 0 L 16 3 L 24 3 L 27 0 L 120 0 L 123 3 L 123 19 L 120 22 L 27 22 L 24 25 L 16 25 L 13 22 L 3 22 L 0 19 Z" class="sb-motion sb-bevel"></path><text x="0" y="10" class="sb-label " transform="translate(6 5)">point</text><text x="0" y="10" class="sb-label " transform="translate(34 5)">in</text><text x="0" y="10" class="sb-label " transform="translate(47 5)">direction</text><g transform="translate(93 4)"><path d="M 6.5 0 L 17.5 0 A 6.5 6.5 0 0 1 17.5 13 L 6.5 13 A 6.5 6.5 0 0 1 6.5 0 Z" class="sb-input sb-input-number-dropdown"></path><text x="0" y="10" class="sb-label sb-literal-number-dropdown" transform="translate(5 0)"></text><polygon points="7 0 3.5 4 0 0" fill="#000" opacity="0.6" transform="translate(14 4)"></polygon></g></g></g></g></svg></div></pre>
"""

scratch_emojis = {
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/neutral.png": ":|",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/smile.png": ":)",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/sad.png": ":(",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/yikes.png": ":o",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/wink.png": ";)",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/hmm.png": ":/",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/lol.png": ":lol:",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/tongue.png": ":P",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/mad.png": ":mad:",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/roll.png": ":rolleyes:",
    "//cdn.scratch.mit.edu/scratchr2/static/__74e70580e9dbe93ce1c3f8422dde592d__/djangobb_forum/img/smilies/cool.png": ":cool:"
}


def guess_language(code):
    guessed = guess_lexer(code).name
    print("GUESSED:", guessed)
    if guessed == "Text only":
        return None
    return guessed.lower()


def html_to_bbcode(tag):
    result = ""

    if hasattr(tag, 'children'):
        for child in tag.children:
            if isinstance(child, str):
                result += child
            else:
                result += html_to_bbcode(child)

    if tag.name == "span":
        tag_type = tag["class"][0]
        if tag_type == "bb-bold":
            result = f"[b]{result}[/b]"
        elif tag_type == "bb-italic":
            result = f"[i]{result}[/i]"
        elif tag_type == "bb-underline":
            result = f"[u]{result}[/u]"
        elif tag_type == "bb-strikethrough":
            result = f"[s]{result}[/s]"
        elif tag_type == "bb-big":
            result = f"[big]{result}[/big]"
        elif tag_type == "bb-small":
            result = f"[small]{result}[/small]"
    elif tag.name == "br":
        result = "\n"
    elif tag.name == "a":
        result = f"[url={tag['href']}]{result}[/url]"
    elif tag.name == "img":
        src = tag['src']
        if src in list(scratch_emojis.keys()):
            result = scratch_emojis[src]
        else:
            result = f"[img]{src}[/img]"
    elif tag.name == "ul":
        result = f"[list]\n{result}[/list]"
    elif tag.name == "li":
        result = f"[*] {result}"
    elif tag.name == "ol":
        result = f"[list]\n{result}[/list]"
    elif tag.name == "blockquote":
        quote_author = tag.find("p", {"class": "bb-quote-author"})
        if quote_author is not None:
            quote_author = "=" + quote_author.get_text()
        else:
            quote_author = ""
        result = f"[quote{quote_author}]{result}[/quote]"
    elif tag.name == "div" and ("code" in tag["class"]):
        language = guess_language(tag.get_text())
        if language is None:
            language = ""
        else:
            language = "=" + language
        result = f"[code{language}]{result}[/code]"
    elif tag.name == "div" and ("scratchblocks" in tag["class"]):
        result = f"[scratchblocks]{tag.get_text()}[/scratchblocks]"
    return result


start = time.time()
soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())

print(html_to_bbcode(soup))
end = time.time()

print(f"Converted in {end - start:.3f} seconds!")
