class Day6:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read()
        self.input = open(inp).read()
        self.run_test = run_test

    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0

        for i in range(3,len(inp)):
            if len(set(inp[i-4:i])) == 4:
                v = i
                break
            

        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        u = 0
        for i in range(13,len(inp)):
            if len(set(inp[i-14:i])) == 14:
                u = i
                break
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

solver = Day6('test.txt','input.txt',0)
solver.solve()