# Last updated: 8/21/2025, 12:24:46 AM
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