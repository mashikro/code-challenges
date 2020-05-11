# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


def valid_paren(s):

    paren_stack = []

    paren_index = []

    for i in range(len(s)):

        if s[i] == '(':
            paren_stack.append(s[i])
            paren_index.append(i)

        elif s[i] == ')':
            if paren_stack and paren_index and paren_stack[-1] == '(':
                paren_stack.pop()
                paren_index.pop()
            else:
                paren_stack.append(s[i])
                paren_index.append(i)
        # print('stack:', paren_stack)
        # print('index:', paren_index)


    # print(s)
    
    ret = []

    for i in range(len(s)):
        if i not in paren_index:
            ret.append(s[i])
            # print('ret:', ret)

    return ''.join(ret)

# print(valid_paren("lee(t(c)o)de)")) #lee(t(c)o)de
# print(valid_paren("a)b(c)d")) #"ab(c)d"
# print(valid_paren("(a(b(c)d)")) #"a(b(c)d)"
# print(valid_paren("))((")) #''

def valid_paren_faster(s):
    def delete_invalid_closing(string, open_symbol, close_symbol):
        sb = []
        balance = 0
        for c in string:
            if c == open_symbol:
                balance += 1
            if c == close_symbol:
                if balance == 0:
                    continue #no matching opener thus skip adding it
                balance -= 1
            print('balance:', balance)
            sb.append(c)
            print('sb:', sb)
        return "".join(sb)
    # 
    # Note that s[::-1] gets the reverse of s.
    s = delete_invalid_closing(s, "(", ")")
    print('s 1:',s)
    s = delete_invalid_closing(s[::-1], ")", "(")
    print('s 2:',s)
    return s[::-1]

# print(valid_paren_faster("lee(t(c)o)de)"))



def valid_paren_fastest(s):
    # Parse 1: Remove all invalid ")"
    first_parse_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_parse_chars.append(c)
        print('first_parse_chars:', first_parse_chars)
    print('balance:', balance)
    print('open_seen', open_seen)
    print('*******first_parse_chars:', first_parse_chars)

    # Parse 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance # (all operers minus the openers that didnt have closers)
    print('open_to_keep', open_to_keep)
    for c in first_parse_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0: #if c is an opener and we dont have open to keep left then skip it
                continue
        result.append(c)
        print('result:', result)

    return "".join(result)

# print(valid_paren_fastest("lee(t(c)o)de)"))
print(valid_paren_fastest("))((")) #''

