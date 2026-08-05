words = list(input("Enter the words : ").split())

def find_longest_prefix(words):
    if not words:
        return ""
    word1 = words[0]
    i=1
    while i<= len(word1):
        for j in range(1,len(words)):
            if not words[j].startswith(word1[0:i]):
                prefix = word1[0:i-1]
                return prefix
        i += 1
    return word1

print(f"Longest Common Prefix is : {find_longest_prefix(words)}")