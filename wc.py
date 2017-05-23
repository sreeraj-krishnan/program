import sys


wc={}
lc={}

def count( filename):
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
        print "in count" , e


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: count <pattern> <text file name>'
        sys.exit(0)

    filename = str(sys.argv[1])
    
    count(filename)
    try:
        print "LETTER COUNT:"
        for key in lc:
            out = ''
            if key == ' ':
                out = 'spaces : '
            elif key == '\t':
                out = 'tabs : '
            elif key == '\n' or key == '\r':
                out = 'lines : '
            else:
                out = str(key) + ' : '
            print "%32s" % out , str(lc[key])

        print "WORD COUNT"
        for key in wc:
            print "%32s" % str(key) , " : "  , str(wc[key])
    except Exception as e:
        print e
