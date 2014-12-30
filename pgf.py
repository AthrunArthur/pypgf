#author : Athrun Arthur

def make_standalone(fig):
    '''This is used to wrap a fig with tex headers
    '''
    header = '\\documentclass[border=3mm]{standalone}\n'
    header += '\\usepackage{pgfplots}\n'
    header += '\\pgfplotsset{compat=newest}\n'
    header += '\\pagestyle{empty}\n'
    header += '\\begin{document}\n'
    header += '\\begin{tikzpicture}\n'

    end = '\\end{tikzpicture}\n'
    end += '\\end{document}'

    return header + fig + end

class PlotSet:
    def __init__(self, name):
        self.ps_name = name

    def name(self):
        return self.ps_name

class Plot:
    def __init__(self):
        self.hs = '\\begin{axis}'
        self.plotset = None
        self.es = '\\end{axis}\n'
        self.legends = []
        self.plots = []

    def config(self, ps):
        self.plotset = ps

    def addplot(self, data, xfunc, yfunc, style='', legend=''):
        if len(data) == 0:
            return

        s = '\\addplot '
        if len(style) != 0:
            s += '[ ' + style + ' ]'
        s += ' plot coordinates {\n'
        for d in data:
            s += '(' + str(xfunc(d)) + ', ' + str(yfunc(d)) + ')\n'
        s += '};'

        self.plots.append(s)
        if len(legend) != 0:
            self.legends.append(legend)

    def dump(self):
        rs = ''
        rs += self.hs
        if not self.plotset is None:
            rs += ' [' + self.plotset.name() + ']'
        rs += ' \n'

        for p in self.plots:
            rs += p

        if len(self.legends) != 0:
            rs += '\\legends{'
        for l in self.legends :
            rs += l + ','
        if len(self.legends) != 0:
            rs = rs.strip(',') + '}\n'

        rs += self.es
        return rs


if __name__ == '__main__':
    p = Plot()

    import math
    p.addplot(range(0, 1000), lambda x: x, lambda x : round(math.sin(x*math.pi/180), 2))
    s = p.dump()
    s = make_standalone(s)
    import os
    if not os.path.exists('tt'):
        os.mkdir('tt')
    open('tt/xx.tex', 'w').write(s)

