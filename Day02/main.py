class Day2:
    def __init__(self,test,inp,run_test=False) -> None:
        self.test = open(test).read().split('\n')
        self.input = open(inp).read().split('\n')
        self.run_test = run_test
    
    def part1(self,inp=None):
        if not inp:inp=self.input
        v = 0
        mp = {'X':1,'Y':2,'Z':3}
        x = list('XYZ')
        a = list('ABC')
        for i in inp:
            o,m = i.split(' ')
            cs = mp[m]
            if x.index(m) == a.index(o):
                cs+=3
            elif (o == 'A' and m == 'Y') or (o=='B' and m == 'Z') or (o=='C' and m=='X'):
                cs+=6
            v+=cs

        print(f'Part1: {v}')

        

    def part2(self,inp=None):
        if not inp:inp=self.input
        v = 0

        for i in inp:
            cs=0
            o,m = i.split(' ')
            if m == 'X':
                if o == 'A':
                    cs+=3
                elif o == 'B':
                    cs+=1
                elif o == 'C':
                    cs+=2
            elif m =='Y':
                if o == 'A':
                    cs+=1
                elif o == 'B':
                    cs+=2
                elif o == 'C':
                    cs+=3
                cs+=3
            elif m == 'Z':
                if o == 'A':
                    cs+=2
                elif o == 'B':
                    cs+=3
                elif o == 'C':
                    cs+=1
                cs+=6
            
            v+=cs
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

solver = Day2('test.txt','input.txt',0)
solver.solve()