class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        lis = []
        lis1 = []
        distance = tasks[0][1] - tasks[0][0]
        for i in tasks:
            dis = i[1] - i[0]
            if dis == distance:
                lis.append(i)
            else:
                lis1.append(lis[:])
                lis = [i]
                distance = dis
        lis1.append(lis[:])
        for i in lis1:
            i.sort(key=lambda x: x[1], reverse=True)
        lis2 = [item for sublist in lis1 for item in sublist]
        initial = lis2[0][1]
        current = lis2[0][1]
        for i in lis2:
            if current >= i[1]:
                current -= i[0]
            else:
                needed = i[1] - current
                current += needed
                initial += needed
                current -= i[0]
        return initial