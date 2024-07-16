#Convert string to only alphanumeric characters and lowercase, check if it is a palindrome, reads the same front to back

def slide_window(s):
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())
    l,r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

def main():
    s = "A man, a plan, a canal: Panama"
    print(slide_window(s))
main()