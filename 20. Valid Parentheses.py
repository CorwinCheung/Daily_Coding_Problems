def dictionary_solution(s):
    map = {'(':')',
           '{':'}',
           '[':']'}
    stack = []
    for c in s:
        if c in map:
            stack.append(c)
        else:
            if not stack or map[stack.pop()]!=c:
                return False
    if not stack:
        return True
    return False


def list_solution(s):
    open_parens = ['(','{','[']
    closed_parens = [')','}',']']
    stack = []
    for c in s:
        if c in open_parens:
            stack.append(c)
        elif c in closed_parens:
            if c != closed_parens[open_parens.index(stack.pop())]:
                return False
    return not stack

def main():
    s1 = "()[]{}"
    s2 = "(]"
    print(dictionary_solution(s1))
    print(dictionary_solution(s2))
    print(list_solution(s1))
    print(list_solution(s2))

main()