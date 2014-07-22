
class Numbers(object):
    """docstring for Numbers"""
    def __init__(self, input_str):
        input_str = input_str.strip()
        lines = input_str.split("\n")
        self.data = []
        for line in lines:
            temp_list = []
            nums = line.split()
            for num in nums:
                num = num.strip()
                temp_list.append(num)
            self.data.append(temp_list)

    @property
    def lines(self):
        lines = []
        for i in range(len(self.data[0])-1):
            for j in range(i+1, len(self.data[0])):
                mark = "%d %d" % (i+1, j+1)
                combs = []
                for row in self.data:
                    comb = Comb(row[i], row[j])
                    combs.append(comb)
                line = Line(combs, mark)
                lines.append(line)
        return lines

    def get_result(self):
        result_str = ""
        for line in self.lines:
            result4, result3, result2 = line.get_result()
            result_str += "%s:    %s    %s    %s\n" % (line.mark, result4, result3, result2)
        result_str = result_str.strip()
        return result_str#[:-2] + "**" 



class Comb(object):
    """docstring for Comb"""
    def __init__(self, num1, num2):
        self.num1 = str(num1)
        self.num2 = str(num2)

    def __repr__(self):
        return self.num1 + self.num2

    def __eq__(self, other):
        if isinstance(other, Comb):
            return self.value == other.value
        return False

    def __ne__(self, other):
        return not self.__eq__()

    @property
    def value(self):
        return sorted([self.num1, self.num2])



class Line(object):
    """docstring for Line"""
    def __init__(self, combs, mark=""):
        self.combs = combs
        self.original = combs[:]
        self.mark = mark
        self.result4 = []
        self.result3 = []
        self.result2 = []

    def __repr__(self):
        s = ""
        for comb in self.original:
            s += str(comb) + "."
        return s[:-1]

    @property
    def line_singles(self):
        singles = []
        for comb in self.combs:
            if not isinstance(comb, Comb):
                continue
            if comb.num1 not in singles:
                singles.append(comb.num1)
            if comb.num2 not in singles:
                singles.append(comb.num2)
        return sorted(singles)

    @property
    def count(self):
        return len(self.line_singles)

    def remove(self, comb):
        #print self.combs, "-", comb
        self.combs.remove(comb)
        if self.count == 4:
            self.result4 = self.line_singles
        elif self.count == 3:
            self.result3 = self.line_singles
        elif self.count == 2:
            self.result2 = self.line_singles

    def get_singles(self, temp_combs):
        singles = []
        for comb in temp_combs:
            if comb.num1 not in singles:
                singles.append(comb.num1)
            if comb.num2 not in singles:
                singles.append(comb.num2)
        return singles

    def is_repeat(self, comb):
        temp_combs = self.combs[:]
        temp_combs.remove(comb)
        singles = self.get_singles(temp_combs)
        if comb.num1 in singles and comb.num2 in singles:
            return True
        else:
            return False

    def filter1(self):
        for i in range(len(self.combs)):
            if self.combs[i] in self.combs[:i]:
                self.combs[i] = "-"
        while self.combs.count("-"):
            self.remove("-")

    def filter2(self):
        flag = True
        for comb in self.combs[:]:
            if not self.is_repeat(comb):
                self.remove(comb)
                flag = False
        if flag and self.combs:
            self.remove(self.combs[0])

    def get_result(self):
        self.filter1()
        while self.count >= 2:
            self.filter2()
        result4 = ".".join(self.result4)
        result3 = ".".join(self.result3)
        result2 = ".".join(self.result2)
        return result4, result3, result2



if __name__ == "__main__":

    input_str = """04   06   10   11   05
    01   04   08   03   05
    03   11   01   08   10
    09   04   08   10   02
    01   04   11   08   05
    01   06   08   10   02
    03   05   10   07   09
    08   05   04   06   09
    08   11   09   02   07
    06   04   11   09   08"""

    input_str = """06   05   11   01   02
09   04   06   07   08
07   05   04   03   10
04   02   01   08   11
05   01   02   04   08
11   03   08   10   04
07   03   11   08   06
05   11   01   03   08
09   04   03   10   05
09   03   06   05   10"""

    n = Numbers(input_str)

    print n.get_result()

