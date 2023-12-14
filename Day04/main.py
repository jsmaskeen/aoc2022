class Day4:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n')
        self.input = open(inp).read().split('\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0
        for i in inp:
            c1,c2 = [set(range(list(map(int,j.split('-')))[0],list(map(int,j.split('-')))[1]+1))  for j  in i.split(',')]
            if c1.issubset(c2) or c2.issubset(c1):
                v+=1

        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        u = 0
        for i in inp:
            c1,c2 = [set(range(list(map(int,j.split('-')))[0],list(map(int,j.split('-')))[1]+1))  for j  in i.split(',')]
            if len(c1.intersection(c2)) != 0:
                u+=1
        print(f'Part2: {u}')



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

solver = Day4('test.txt','input.txt',False)
solver.solve()