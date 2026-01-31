
# ДЗ 8.2. Паліандром

def is_palindrome(text, debug=False):
    def log(*args):
        if debug:
            print(*args)

    left = 0
    right = len(text) - 1

    log("Input:", repr(text))
    log("------")

    while left < right:
        while left < right and not text[left].isalnum():
            log(f"skip left  [{left}] = {repr(text[left])}")
            left += 1

        while left < right and not text[right].isalnum():
            log(f"skip right [{right}] = {repr(text[right])}")
            right -= 1

        l_ch = text[left].casefold()
        r_ch = text[right].casefold()

        log(f"compare left[{left}]={repr(l_ch)}  vs  right[{right}]={repr(r_ch)}")

        if l_ch != r_ch:
            log("Mismatch -> False\n")
            return False

        left += 1
        right -= 1

    log("All matched -> True\n")
    return True

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print('OK')

