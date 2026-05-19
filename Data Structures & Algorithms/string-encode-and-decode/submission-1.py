class Solution:

    def encode(self, strs: List[str]) -> str:
        # dummy_input = ["Hello","World"]
        # we might need to shift each char by one ord distance away
        # first loop iterate through the words in char
        # second loop iterate through the char in words
        ## for each char in words, find the equivalent char with "ord + 1", append to empty list
        ## append to list, "".join list of strings
        # on decode function, reverse the addition, lookup original char

        encoded_list = []
        for i in strs:
            encoded_list.append(str(len(i)) + "#")
            for c in i:
                # c = chr(ord(c)+1)
                encoded_list.append(c)
        
        # it should look like "5zzzzz5zzzzz"

        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            curr_word_len = int(s[i:j])

            decoded_list.append(s[j+1:j+curr_word_len+1])
            i = j + curr_word_len + 1 # 0 + 1 + 5 = 6
        return decoded_list