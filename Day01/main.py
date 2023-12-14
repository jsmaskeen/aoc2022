class Day1:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n\n')
        self.input = open(inp).read().split('\n\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0
        for i in inp:
            v = max(v,sum(list(map(int,i.split('\n')))))
        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        u = 0
        l = []
        for i in inp:
            f = sum(list(map(int,i.split('\n'))))
            l.append(f)
        l.sort(reverse=True)
        u = sum(l[:3])
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

solver = Day1('test.txt','input.txt',)
solver.solve()