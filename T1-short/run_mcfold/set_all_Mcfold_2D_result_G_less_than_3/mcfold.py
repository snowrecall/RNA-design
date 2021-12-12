from sys import exit

class Mcfold:
    pass

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init__(self, fn=None):
        if fn:
            self.read(fn)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def read(self, fn):
        lines = open(fn).readlines()
        hit = filter(lambda x: x[1][:1]=='>', enumerate(lines))
        if not hit:
            print('Cannot find result in MCFold output file!')
            exit(1)
        lines = lines[hit[-1][0]:]
        hit = filter(lambda x: x[1][:1]=='\n', enumerate(lines))
        if len(hit) != 1:
            print('Cannot find blank line in MCFold output file!')
            exit(1)
        lines = lines[:hit[-1][0]]
        self.name = lines[0][1:].strip()
        self.seq = lines[1].strip()
        data = [line.split() for line in lines[2:]]
        self.ss = [[fds[0],float(fds[1])] for fds in data]

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def filter(self, cutoff=3.):
        dG0 = self.ss[0][1]
        for i in range(len(self.ss)):
            self.ss[i][1] -= dG0
        self.ss = filter(lambda x: x[1]<=cutoff, self.ss)
