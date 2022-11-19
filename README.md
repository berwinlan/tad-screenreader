# tad-screenreader
Berwin Lan's TAD FA22 Deep Dive

In my deep dive, I wanted to spend my time creating a primitive screen reader to understand the technical side of why it may be difficult to create the perfect screen reader. My topic selection was driven by what I've learned about the deficiencies of existing screen readers and a personal interest in the potential of technical solutions for accessibility. I obviously was not able to create anything close to a fully functional screen reader, but I learned a lot about the structure of web pages and discovered many of the challenges that come up when trying to make the web more accessible.

## Computational Setup
Clone this repo and run
```sh
$ pip install -r requirements.txt
```
to install all dependencies. Then, run `main.py`.

## Reflection
Having put some time into this project, I can point to some of the challenges I encountered:
* One thing I'm running into is that all webpages are formatted in different ways, both visually (and in the underlying HTML). For example, class names aren't standardized (like not all headers have `header` as their class ID). This makes it difficult to parse through pages and organize them hierarchically, because there are so many different ways to establish that hierarchy.
* My implementation just reads through pages chronologically, in the order that the DOM provides. However, as a visual reader, the order I read in doesn't match up with the DOM. I am curious how commercial screen readers organize their text so it's presented in a natural, logical order to their user.
    * ex. Wikipedia pages will go to the inset text on the right of the page before reading through the first paragraph of text
* Every page is different, and thinking about the range of pages a screen reader has to work on with high consistency is daunting. Even with a sample of 5 pages, several of which were from the same site (Wikipedia), my screen reader would fail on some of them (at various points in the process). To make a useful tool, it must also be reliable.
I now have a greater appreciation for web access standards, like W3C, and the importance of following them when developing websites.

## Next steps
This is obviously a highly extensible project that has a long way to go before approaching the caliber of existing screen readers like JAWS and NVDA. Some immediate improvements I could make are the following:
* Take user input to navigate through text
    * I know Pygame can take user keystrokes as input: one way of implementing this would be mapping the right arrow to the next line, and the down arrow to the next paragraph. In code, the right arrow would immediately skip to the next string in the array, and the down arrow would skip to the next empty string in the array (and pick up there).
* Instead of reading in-order, I would like to create some sort of tree representation of the document for the screen reader to navigate. My hope is to better replicate the visual experience of scanning headers and deciding where to drill down.
* Investigate interacting with pages themselves, for buttons, links, forms, drop-downs, etc.
* If the codebase grew any bigger than it is now, especially if user input was being taken in, I would refactor into something resembling an MVC architecture or similar.