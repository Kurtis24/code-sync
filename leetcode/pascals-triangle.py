class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        #what we can do is, make it so that we see how many rows there are, and they based on how many, we can always re-enter into the array, and then add them up, from middle, and side,and then that will give us our desierable array
        while len(result) < numRows:
            prev = result[-1]
            temp = [1]

            l = 0
            r = 1

            while r < len(prev):
                temp.append(prev[l] + prev[r])
                l += 1
                r += 1

            temp.append(1)
            result.append(temp)

        return result