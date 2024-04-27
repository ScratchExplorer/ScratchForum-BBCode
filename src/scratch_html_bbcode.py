"""
Scratch-HTML-BBCode
-----------------------------
Convert the HTML in Scratch forums to BBCode. This is not 100% perfect converter!
Some results may not be 100% accurate!
>> Use with credit <<
Tags source: https://en.scratch-wiki.info/wiki/BBCode

-----------------------------
Created by @Sid72020123 on Scratch
License: MIT License
"""

from bs4 import BeautifulSoup
from pygments.lexers import guess_lexer  # Used to detect the programming language for code tags

# Some Scratch Emojis
scratch_emojis = {
    "/djangobb_forum/img/smilies/neutral.png": ":|",
    "/djangobb_forum/img/smilies/smile.png": ":)",
    "/djangobb_forum/img/smilies/sad.png": ":(",
    "/djangobb_forum/img/smilies/yikes.png": ":o",
    "/djangobb_forum/img/smilies/wink.png": ";)",
    "/djangobb_forum/img/smilies/hmm.png": ":/",
    "/djangobb_forum/img/smilies/lol.png": ":lol:",
    "/djangobb_forum/img/smilies/tongue.png": ":P",
    "/djangobb_forum/img/smilies/mad.png": ":mad:",
    "/djangobb_forum/img/smilies/roll.png": ":rolleyes:",
    "/djangobb_forum/img/smilies/cool.png": ":cool:"
}


def guess_language(code: str) -> str:
    """
    Guesses the programming language from a string. This is not accurate for short strings. 'pygments' is used to
    guess code here because many other language detectors cannot detect the language properly (based on my tests)
    """
    guessed = guess_lexer(code).name
    if guessed == "Text only":
        return None
    return guessed.lower()


def _html_to_bbcode(tag):
    # Source: https://en.scratch-wiki.info/wiki/BBCode
    result = ""
    if hasattr(tag, 'children'):
        for child in tag.children:
            if isinstance(child, str):
                result += child
            else:
                result += _html_to_bbcode(
                    child)  # Default recursion depth is 1000 in Python. The function may not work for very very long strings

    if tag.name == "span":
        if "class" in list(tag.attrs.keys()):
            tag_type = tag["class"][0]
            if tag_type == "bb-bold":  # bold
                result = f"[b]{result}[/b]"
            elif tag_type == "bb-italic":  # italic
                result = f"[i]{result}[/i]"
            elif tag_type == "bb-underline":  # underline
                result = f"[u]{result}[/u]"
            elif tag_type == "bb-strikethrough":  # strikethrough
                result = f"[s]{result}[/s]"
            elif tag_type == "bb-big":  # big
                result = f"[big]{result}[/big]"
            elif tag_type == "bb-small":  # small
                result = f"[small]{result}[/small]"
        elif "style" in list(tag.attrs.keys()):
            if "color" in tag["style"]:  # color
                result = f"[color={tag['style'].replace('color:', '')}]{result}[/color]"
    elif tag.name == "br":  # line break
        result = "\n"
    elif tag.name == "a":  # url
        result = f"[url={tag['href']}]{result}[/url]"
    elif tag.name == "img":  # img
        src = tag['src']
        is_scratch_image = False
        i = 0
        for image_url in list(scratch_emojis.keys()):
            if src.find(image_url) != -1:
                result = scratch_emojis[list(scratch_emojis.keys())[i]]
                is_scratch_image = True
                break
            i += 1
        if not is_scratch_image:
            result = f"[img]{src}[/img]"
    elif tag.name == "ul":  # unordered list
        result = f"[list]\n{result}[/list]"
    elif tag.name == "li":  # list item
        result = f"[*] {result}"
    elif tag.name == "ol":  # ordered list
        result = f"[list=1]\n{result}[/list]"  # Started from 1 as I can't find the tag property...
    elif tag.name == "blockquote":  # quote
        quote_author = tag.find("p", {"class": "bb-quote-author"})
        if quote_author is not None:
            quote_author_name = str(quote_author.get_text()).replace(" wrote:", "")
            quote_author = "=" + quote_author_name
        else:
            quote_author = ""
        result = f"[quote{quote_author}]{result}[/quote]"
    elif tag.name == "p":
        if "class" in list(tag.attrs.keys()):  # remove "<username> wrote:" string from a quote
            if "bb-quote-author" in tag["class"]:
                result = ""
        else:
            result = f"[p]{result}[/p]"  # p
    elif tag.name == "div":
        if "class" in list(tag.attrs.keys()):
            if "code" in tag["class"]:  # code
                language = guess_language(tag.get_text())
                if language is None:
                    language = ""
                else:
                    language = "=" + language
                result = f"[code{language}]{result}[/code]"
            # This converter cannot convert scratchblocks html to scratchblocks bbcode
            elif "scratchblocks" in tag["class"]:  # scratchblocks
                result = f"[scratchblocks]{tag.get_text()}[/scratchblocks]"
        elif "style" in list(tag.attrs.keys()):
            if "text-align:center;" in tag["style"]:  # center
                result = f"[center]{result}[/center]"
    return result


def html_to_bbcode(html: str) -> dict:
    try:
        soup = BeautifulSoup(html, "lxml")  # lxml is the fastest
        return {"Error": False, "Message": None, "result": _html_to_bbcode(soup)}
    except Exception as E:
        return {"Error": True, "Message": E, "result": None}
