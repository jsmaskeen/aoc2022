class Day3:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n')
        self.input = open(inp).read().split('\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0
        for i in inp:
            c1,c2 = set(i[:len(i)//2]),set(i[len(i)//2:])
            a = list(c1.intersection(c2))[0]
            if a.islower():
                v+= 1 + ord(a) - ord('a')
            else:
                v+= 1 + ord(a) - ord('A')+26


        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        v = 0
        for i in range(len(inp)//3):
            ls = inp[3*i:3*(i+1)]
            a = list(set(ls[0]).intersection(set(ls[1])).intersection(set(ls[2])))[0]
            if a.islower():
                v+= 1 + ord(a) - ord('a')
            else:
                v+= 1 + ord(a) - ord('A')+26

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

solver = Day3('test.txt','input.txt',)
solver.solve()