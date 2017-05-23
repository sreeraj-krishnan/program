
import sys


def out( _map ):
    try:
        for key in _map:
            out = ''
            if key == ' ':
                out = 'spaces : '
            elif key == '\t':
                out = 'tabs : '
            elif key == '\n' or key == '\r':
                out = 'lines : '
            else:
                out = str(key) + ' : '
            print "%32s" % out , str(_map[key])

    except Exception as e:
        print e


def count( filename, wc, lc):
    try:
        fileread = open(filename, 'r')
        word=''
        for line in fileread.xreadlines():
            word=''
            for letter in line:
                value = lc.get(letter,int(0))
                lc[letter] = value + 1
                if letter == ' ' or letter == '\n' or letter == '\r':
                    if word != '':
                        value = wc.get(word,int(0))
                        wc[word] = value + 1
                        word = ''
                else:
                    word = word + str(letter)
                
        fileread.close()
    except Exception as e:
        print  e
        sys.exit(1)


def process(filename):
    wc={}
    lc={}
    count(filename,wc,lc)
    print "LETTER COUNT:"
    out(lc)
    print "WORD COUNT"
    out(wc)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python wc.py <text file name>'
        sys.exit(0)

    filename = str(sys.argv[1])
    process( filename )

