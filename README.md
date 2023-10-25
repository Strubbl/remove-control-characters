# Python Remove Control Characters

python script to remove control characters from a file

## Description

This is a quick and dirty python script which can be used to read an input file line by line, remove control characters for every line and finally write it line by line.

It was used to find the control character, which aborted the generation of a feed. The error was `django.utils.xmlutils.UnserializableContentError: Control characters are not supported in XML 1.0` and was reported in the [linkding repository](https://github.com/sissbruecker/linkding/issues/552).

## Usage

`python rcc.py input-file cleaned-file`

