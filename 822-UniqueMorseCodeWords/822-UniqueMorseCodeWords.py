# Last updated: 8/24/2025, 11:55:22 PM
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
        'a':".-", 'b':"-...", 'c':"-.-.", 
        'd':"-..", 'e':".", 'f':"..-.", 
        'g':"--.", 'h':"....", 'i':"..", 
        'j':".---", 'k':"-.-", 'l':".-..", 
        'm':"--", 'n':"-.", 'o':"---", 
        'p':".--.", 'q':"--.-", 'r':".-.", 
        's':"...", 't':"-", 'u':"..-", 
        'v':"...-", 'w':".--", 'x':"-..-", 
        'y':"-.--", 'z':"--.."}

        
        res = set()

        for x in words:
            temp = ""
            for y in x:
                temp += morse.get(y)
            res.add(temp)
        return len(res)