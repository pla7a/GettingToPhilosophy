## Known bugs
Wikipedia disambiguation error is handled by cases but the parsing from Beautiful Soup (in the wikipedia module) results in a runtime warning similar to the following:
```
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser").
This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
To get rid of this warning, change this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "html.parser")

  markup_type=markup_type))
```

This isn't an error as such (as the default choice works), but can cause unwanted text in terminal. To change this, edit the 'wikipedia.py' file (from the wikipedia module) on line 389 from: 

      lis = BeautifulSoup(html).find_all('li')
to

      lis = BeautifulSoup(html, "html.parser").find_all('li')
