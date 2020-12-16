from typing import List
'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time: O(len(words)) Space: O(len(words))
        morse_list= map(self.convert_to_morse, words)
        return len(set(morse_list))
    def convert_to_morse(self, word):
        morse_table= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet_table= list(string.ascii_lowercase)
        morse_code=''
        for i in word:
            al_index= alphabet_table.index(i)
            morse_code+=morse_table[al_index]
        return morse_code
'''
Question Type: Array
Question Difficulty: Easy
'''