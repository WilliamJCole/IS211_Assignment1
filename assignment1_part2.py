#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 Assignment 2."""

class Book(object):
    """book class.
    Args:
        author (str): Author
        title (str): Book
    """
    author = ""
    title = ""

    def __init__(self, author, title):
        """Init Func"""

        self.author = author
        self.title = title

    def display(self):
        """Info about book.
        Returns:
            output (str): names of the author and the book.
        """
        message = "{}, written by {}."
        output = message.format(self.author, self.title)
        return output

BOOK1 = Book("Of Mice and Men", "John Steinbeck")
BOOK2 = Book("To Kill a Mockingbird", "Harper Lee")

print BOOK1.display()
print BOOK2.display()
