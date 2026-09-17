class Solution:
    def encode(self, strs: List[str]) -> str:
        
        def caesar_cipher(word: str) -> str:
            result = []
            key = 5

            for ch in word:
                if "a" <= ch <= "z":
                    position = ord(ch) - ord("a")
                    new_position = (position + key) % 26
                    result.append(chr(ord("a") + new_position))
                    
                elif "A" <= ch <= "Z":
                    position = ord(ch) - ord("A")
                    new_position = (position + key) % 26
                    result.append(chr(ord("A") + new_position))

                else:
                    result.append(ch)

            return "".join(result)
                    
        
        encoded_cipher = []

        for word in strs:
            encoded_word = caesar_cipher(word)

            encoded_cipher.append(
                str(len(encoded_word)) + "#" + encoded_word
            )
            
        return "".join(encoded_cipher)
            
    
    def decode(self, s: str) -> List[str]:
        key = 5
        result = []
        i = 0

        while i < len(s):
            j = i

            # incrementing j until there is hashtag
            while s[j] != "#":
                j += 1

            word_length = int(s[i:j])
            word_start = j + 1
            word = s[word_start:word_start + word_length]

            word_string = ""

            for ch in word:
                if "a" <= ch <= "z":
                    position = ord(ch) - ord("a") - key
                    new_position = position % 26
                    word_string += chr(new_position + ord("a"))

                elif "A" <= ch <= "Z":
                    position = ord(ch) - ord("A") - key
                    new_position = position % 26
                    word_string += chr(new_position + ord("A"))

                else:
                    word_string += ch

            result.append(word_string)

            #move to the next encoded word
            i = word_start + word_length

        return result


        