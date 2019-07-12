import sys
from argparse import ArgumentParser

lower = 'abcdefghijklmnopqrstuvwxyz'


# upper = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digit = string.digits           # '0123456789'
# punc = string.punctuation       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# test

class Wordlist:
    def __init__(self):
        self.ins = argparse()
        if self.ins['chars'] is not None:
            self.char = self.ins['chars']
        else:
            self.char = lower
        if self.ins['min'] is None:
            self.minlen = 1
        else:
            self.minlen = self.ins['min']
        self.maxlen = self.ins['max']
        if self.ins['out'] is None:
            self.out = sys.stdout
        else:
            self.out = open(self.ins['out'], 'w', newline='\n')
        self.dic = {}
        self.percent = 0
        self.perc_total = 0

    def character(self):
        for i in range(self.minlen):
            s = "char{}".format(i + 1)
            self.dic[s] = 0
        for i in range(len(self.char) ** self.minlen):
            self.percent += 1
            if self.out != sys.stdout:
                sys.stdout.write("%" + str(self.percent * 100 / self.perc_total)[:4] + '\r')
                sys.stdout.flush()
            write = "".join(self.char[self.dic[f"char{k+1}"]] for k in range(self.minlen))
            print(write, file=self.out)
            self.dic['char{}'.format(self.minlen)] += 1
            for j in range(self.minlen):
                if self.dic[f'char{self.minlen - j}'] == len(self.char):
                    self.dic[f'char{self.minlen - j}'] = 0
                    if (self.minlen - j - 1) != 0:
                        self.dic[f'char{self.minlen - j - 1}'] += 1
                    else:
                        continue

    def main(self):
        if self.maxlen is not None:
            for i in range(self.minlen, self.maxlen + 1):
                self.perc_total += len(self.char) ** i
            while self.minlen <= self.maxlen:
                self.character()
                self.minlen += 1
        else:
            self.character()


def argparse():
    parser = ArgumentParser()
    parser.add_argument('-m', '--min', help='Minimum wordlist length', type=int)
    parser.add_argument('-M', '--max', help='Maximum wordlist length', type=int)
    parser.add_argument('-o', '--out', help='Saves output to specified file')
    parser.add_argument('-c', '--chars', help='select a charset', type=str)
    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    argparse()
    ex = Wordlist()
    ex.main()
    if ex.out != sys.stdout:
        ex.out.close()
