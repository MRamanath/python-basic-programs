# A Program to display even number within the range.

min , max = [int(x) for x in input('Enter the minimum and maximum range : ').split()]
print('Even numbers are as follows --- ')
for x in range(min, max + 1):
    if x % 2 == 0:
        print(x, end = '\t')
    
# Output
# Enter the minimum and maximum range : 100 200
# Even numbers are as follows ---
# 100     102     104     106     108     110     112     114     116     118     120     122     124     126     128     130     132     134     136
# 138     140     142     144     146     148     150     152     154     156     158     160     162     164     166     168     170     172     174
# 176     178     180     182     184     186     188     190     192     194     196     198     200