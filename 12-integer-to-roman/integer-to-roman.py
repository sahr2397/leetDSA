class Solution:
    def intToRoman(self, num: int) -> str:

        def roman(num,pow):
            roman_num=''
            mapper={
                1:'I', 4:'IV', 5:'V', 9:'IX',
                10:'X', 40:'XL', 50:'L', 90:'XC',
                100:'C', 400:'CD', 500:'D', 900:'CM',
                1000:'M'

            }
            start_value=num//(10**pow)
            if start_value<4: roman_num=mapper[10**pow]*start_value
            elif start_value>=4 and start_value<=5: roman_num=mapper[start_value*(10**pow)]
            elif start_value>5 and start_value<9: 
                roman_num+=mapper[5*(10**pow)]
                roman_num+=mapper[(10**pow)]*(start_value-5)
            elif start_value==9: roman_num=mapper[start_value*(10**pow)]
            
            return roman_num



        n=num
        res=[]
        for pow in range(1,len(str(num))+1):

            rem=n%(10**pow)
            res.append(roman(rem,pow-1))
            n-=rem

        return ''.join(res[-1::-1])

