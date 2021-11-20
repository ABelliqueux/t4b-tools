#!/usr/bin/env python
# Source : https://nachtimwald.com/2010/01/13/cybook-t4b-format-specification/
# ~ Copyright John Schember <john@nachtimwald.com>

# ~ Permission is hereby granted, free of charge, to any person obtaining a copy of
# ~ this software and associated documentation files (the "Software"), to deal in
# ~ the Software without restriction, including without limitation the rights to
# ~ use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# ~ of the Software, and to permit persons to whom the Software is furnished to do
# ~ so, subject to the following conditions:

# ~ The above copyright notice and this permission notice shall be included in all
# ~ copies or substantial portions of the Software.

# ~ THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# ~ IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# ~ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# ~ AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# ~ LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# ~ OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# ~ SOFTWARE.

import sys, os

def get_greys(b):
    if not b:
        return 0, 0

    b = bin(int(ord(b)))
    b = b[2:].zfill(8)

    w = str(int(b[0:4], 2))
    x = str(int(b[4:8], 2))

    return w, x

def main():

    imgWidth = 96
    imgHeight = 144
    
    if len(sys.argv) < 3:
        print('Must have 2 arguments. %s input.epub.thm output.pgm' % sys.argv[0])
        return 0

    if len(sys.argv) == 5:
        imgWidth = int(sys.argv[3])
        imgHeight = int(sys.argv[4])

    t4bfile = open(sys.argv[1], 'rb')
    pgmfile = open(sys.argv[2], 'w')

    pgmfile.write('P2\n' + str(imgWidth) + ' ' + str(imgHeight) + '\n15\n')

    # Read past the t4b header
    t4bfile.read(4)

    for i in range(imgHeight):
        for j in range(int(imgWidth/2)):
            b = t4bfile.read(1)

            vals = get_greys(b)
            pgmfile.write('%s %s ' % (vals[0], vals[1]))
        pgmfile.write('\n')

    pgmfile.close()
    t4bfile.close()

if __name__ == '__main__':
    main()
