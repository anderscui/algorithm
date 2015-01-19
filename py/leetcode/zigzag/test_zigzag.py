from zigzag import Solution

sln = Solution()
s = 'PAYP'
ns = sln.convert(s, 3)
print(ns)
assert ns == 'PAPY'

s = 'PAYPALISHIRI'
ns = sln.convert(s, 3)
print(ns)
assert ns == 'PAHAPLSIIYIR'

s = 'PAYPALISHIRING'
ns = sln.convert(s, 3)
print(ns)
assert ns == 'PAHNAPLSIIGYIR'


s = 'PAYPALISHIRING'
ns = sln.convert(s, 5)
print(ns)
assert ns == 'PINASGYLHIPIAR'

# even numbers
s = 'A'
ns = sln.convert(s, 2)
print(ns)
assert ns == 'A'

s = 'ABC'
ns = sln.convert(s, 2)
print(ns)
assert ns == 'ACB'

s = 'ABCD'
ns = sln.convert(s, 2)
print(ns)
assert ns == 'ACBD'


s = 'ABCDE'
ns = sln.convert(s, 2)
print(ns)
assert ns == 'ACEBD'

s = 'ABCDE'
ns = sln.convert(s, 4)
print(ns)
assert ns == 'AEBCD'