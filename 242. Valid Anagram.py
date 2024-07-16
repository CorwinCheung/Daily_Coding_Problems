#Return if s and t are valid anagrams
def check_dist(s,t):
    d1 = {}
    for c in s:
        if c in d1:
            d1[c]+=1
        else:
            d1[c]=1
    d2 = {}
    for c in t:
        if c in d2:
            d2[c]+=1
        else:
            d2[c]=1
    return d1 == d2

def main():
    s = "anagram"
    t = "nagaram"
    print(check_dist(s,t))

main()