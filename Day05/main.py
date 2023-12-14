class Day5:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n\n')
        self.input = open(inp).read().split('\n\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = ''
        crats = inp[0].split('\n')
        maax = int(crats[-1].replace(' ','')[-1])
        gg = []
        for j in crats[:-1]:
            tmp = []
            for i in range(maax):
                tmp.append(j[4*i:4*(i+1)].strip('[] '))
            gg.append(tmp)
        rows = [[j for j in i if j!=''][::-1] for i in list(zip(*gg))]
        instruct = inp[1].split('\n')

        for i in instruct:
            qt,fro,to = list(map(int,i.split(' ')[1::2]))
            j = 0
            while j!=qt:
                rows[to-1].append(rows[fro-1].pop())
                j+=1
        
        
        for i in rows:
            v+=i[-1]

        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        v = ''
        crats = inp[0].split('\n')
        maax = int(crats[-1].replace(' ','')[-1])
        gg = []
        for j in crats[:-1]:
            tmp = []
            for i in range(maax):
                tmp.append(j[4*i:4*(i+1)].strip('[] '))
            gg.append(tmp)
        rows = [[j for j in i if j!=''][::-1] for i in list(zip(*gg))]
        instruct = inp[1].split('\n')

        for i in instruct:
            qt,fro,to = list(map(int,i.split(' ')[1::2]))

            x = rows[fro-1]
            
            rows[to-1].extend(x[len(x)-qt:])
            rows[fro-1] = x[:len(x)-qt]

            # while j!=qt:
            #     rows[to-1].append(rows[fro-1].pop())
            #     j+=1


        
        
        for i in rows:
            v+=i[-1]

        print(f'Part2: {v}')



    def tester(self):
        print('TEST'.center(16,'#'))
        self.part1(self.test)
        print()
        self.part2(self.test)
        print('#'*16)
        print()

    def solve(self):
        if self.run_test:
            self.tester()
        else:
            self.part1()
            print()
            self.part2()

solver = Day5('test.txt','input.txt',0)
solver.solve()