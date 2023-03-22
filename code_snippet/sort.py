# Note:: The problem is taken from Berkeley's CS61B.
# Reference: https://github.com/Berkeley-CS61B/lectureCode-sp23/blob/main/lec6_testing/Sort.java

# Definition of Lexicographic
# case 1: a = "aa" and b = "ab" --> a[1] < b[1] --> output: ["aa", "ab"]
# case 2: a = "bc" and b = "cd" --> a[0] < b[0] --> output: ["bc", "cd"]
# case 3: (excessive length) a = "aa" and b = "aaa" --> a < b --> output: ["aa", "aaa"]
# a = "aaa" b = "aa"
def check_is_lexicographic_sorted(input_a, input_b):
    # assign simple letters
    a,b = input_a, input_b
    # ensure that length of a is lesser than b
    if len(a) > len(b):
        a, b = b, a
    # left pointer for input_a, and right pointer for input_b
    l, r = 0, 0
    while l < len(a):
        # Case 3: Since both strings are the same, we return 
        if input_a[0:len(a)] == input_b[0:len(a)]:
            l = len(input_a)
            r = len(input_b)
        # handle case 1
        elif ord(input_b[r]) < ord(input_a[l]):
            return False
        # handle the case where both are the same character
        elif ord(input_a[l]) == ord(input_b[r]):
            l += 1
            r += 1
        else:
            break
    # if right pointer of input_b reaches end the first; then input_b is smaller than input_a
    if l >= len(input_a) and r < len(input_b):
        return False
    if l >= len(input_a) and r >= len(input_b) and len(input_a) > len(input_b):
        return False
    return True

# Testing
print('~~~~~ testing of lexicographic_sorted ~~~~~')
print(check_is_lexicographic_sorted("aaa", "aa")) # Expected: False
print(check_is_lexicographic_sorted("aa", "ab"))  # Expected: True
print(check_is_lexicographic_sorted("ab", "aa"))  # Expected: False
print(check_is_lexicographic_sorted("aab", "aa"))  # Expected: False
print(check_is_lexicographic_sorted("h", "i"))  # Expected: True
print(check_is_lexicographic_sorted('conchis','agoyatis')) #Expected: False
print(check_is_lexicographic_sorted('the','is')) #Expected: False

def sort(l_arr, r_arr):
    res = []
    # l-pointer for l_arr, and r-pointer for r_arr
    l, r = 0, 0
    while l < len(l_arr) and r < len(r_arr):
        # check if l < r
        if check_is_lexicographic_sorted(l_arr[l], r_arr[r]):
            res.append(l_arr[l])
            l += 1
        else:
            res.append(r_arr[r])
            r += 1
    # gather remainder item(s)
    if l < len(l_arr):
        res.extend(l_arr[l:])
    if r < len(r_arr):
        res.extend(r_arr[r:])
    return res


def merge_sort(cur_arr):
    if len(cur_arr) <= 1:
        return cur_arr
    # post-order traversal sorting
    mid = len(cur_arr) // 2
    l_part = merge_sort(cur_arr[0:mid])
    r_part = merge_sort(cur_arr[mid:] )
    res = sort(l_part, r_part)
    return res


# Testing
print('~~~~~ testing of merge_sort ~~~~~')
print(merge_sort(["the", "he", "is"])) # Expected: ["he", "is", "the"]
print(merge_sort(["aaa", "aa", "aaaa", "aaaaaaaa"])) # Expected: ['aa', 'aaa', 'aaaa', 'aaaaaaaa']
sample_input = ["he", "is", "the", "agoyatis", "of", "mr.", "conchis"]
print(merge_sort(sample_input)) # Expected: ['agoyatis', 'conchis', 'he', 'is', 'mr.', 'of', 'the']
    

    



