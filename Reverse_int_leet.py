class Solution:
    def reverse(self, x: int) -> int:
        def rev(a):
            c=list(str(a))

            i=len(c)-1
            d=[]
            if i<0:
                return 0
            else:
                while i!=-1:
                    d.append(c[i])
                    i-=1
                return (int("".join(map(str,d))))    



        if x<0   :
            x=0-x
            b=0-rev(x)
            if b>= (-2147483648):
                return 0-rev(x)
            return 0
    
            
        
        elif x>=0 :
            b=rev(x)
            if b<=2147483647:
                return rev(x)
            return 0
        
        
        
 
a=Solution()
print(a.reverse(1534236469))
