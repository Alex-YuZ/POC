# Anagrams

An **anagram** is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. That is to say, **all words in an anagram family have the same collection of letters**. For example, the words *`stone`, `notes`, `onset`, `tones`* constitute an anagram.  

This program allows you to input any word you'd like to output those words which share the same anagrams. 
<br></br>

# Quickstart

1. Run the `anagrams.py` file in the terminal.
```
$ python anagrams.py
```
2. Type in any word you'd like in the terminal to check the other words in its anagrams.
```
$ python anagrams.py
What letters would you like to find the anagram of? notes
notes
stone
tones
onset
What letters would you like to find the anagram of? 
```
<br></br>

# How it works
There are three other files in spite of this README file under the folder of this repo.  
- `wordsets.py` is the program that load the raw data (the words bank) into appropriate data struture (a `set` in this example). There are **two word banks** with which you can test the function: the `english_words` variable refers to a set of mostly all English words (it's stored in the `words.txt` file). The `english_words_small` variable refers to a set of the following 13 english words:
```
open
peon
nope
stone
notes
onset
tones
cone
pots
post
stop
opts
tops
```
You can use it as an example test or proof of concept.

- `words.txt` is the words dictionary. You can load it by `wordsets.py` program.
- `anagrams.py` is the main program that takes in your entry and feedsback the anagram words accordingly.

