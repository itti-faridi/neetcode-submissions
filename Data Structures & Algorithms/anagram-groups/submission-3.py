class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_frequency = []  # can store mutable objects like dictionaries

        # Make frequency dictionary for each word
        groups = {}

        for word in strs:
            frequency = {}

            for ch in word:
                # Store frequency for each character
                frequency[ch] = frequency.get(ch, 0) + 1

            # Must be outside the character loop so it is added once per word
            word_frequency.append(frequency)

        #print(word_frequency)

        for word, frequency_dih in zip(strs, word_frequency):
            signature = tuple(sorted(frequency_dih.items()))

            if signature not in groups:
                groups[signature] = []  # empty list value for the key

            groups[signature].append(word)

            #print(groups)

        return list(groups.values())