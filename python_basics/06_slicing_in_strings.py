s1 = "ABC DEF GHI JKL MNO PQR STU VWX Y&Z"
"""
syntax of indexing: string[index]
syntax of slicing: string[start:end:step]
-start: starting index at which the slicing operations starts
-end: ending index at which the slicing operations ends (excluded)
-step: integer that specifies the steps for the slicing
"""
print(s1[2:6:1])
"""
by running the code output would be:
C DE
because ABC DEF GHI JKL MNO PQR STU VWX Y&Z
        0123456789
slicing starts from 2 that is C and ends at 6 but it is not included (excluded) so not F it is E
and step 1 represnts it need to move next character with taht many steps so it is reaching next if step was 2 then it world be differnt              
"""
print(s1[2:8:2])
""" 
outtput here if you see we get 
CDF 
Because starts from 2 that is C and end at 8 but not included so ends at " " space
it skipped one one character in between and sliced ...
"""
print(s1[2:45:1])
"""
in this case last index is at 34 may be but 45 it cant go that place beacuse it is not existing it slices till last index but there will be no error
slicwe of a string output is also a string
"""
s1_string = (s1[2:45:1])
print(type(s1_string))
