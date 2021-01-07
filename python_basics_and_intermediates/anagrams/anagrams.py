from wordsets import english_words, english_words_small


def find_anagrams(letters, words):
    """
    Find a collection of anagrams of given letters from a given word bank.
    
    Parameter:
        letters -> string : The letters from which to form anagrams.
        words -> iterables : A set of lowercase, alphabetic English words in a word bank.
        
    Returns -> iterables: A set of anagrams of the given letters found in the word bank.
    
    """
    lookup = {}
    for word in words:
        key  = ''.join(sorted(set(word)))
        if key not in lookup:
            lookup[key] = set()
            lookup[key].add(word)
        else:
            lookup[key].add(word)
    
    return lookup.get(''.join(sorted(letters)), set())
                   


if __name__ == '__main__':
    letters = input("What letters would you like to find the anagram of? ").lower().strip()
    while letters != "q":
        for anagram in find_anagrams(letters, english_words_small):
            print(anagram)
            
        letters = input("What letters would you like to find the anagram of? ").lower().strip()
        
