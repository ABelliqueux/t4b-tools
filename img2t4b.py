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

import sys
from PIL import Image

REDUCE_MARKS = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]

def reduce_color(c):
    val = 0
    for mark in REDUCE_MARKS:
        if c > mark:
            val += 1
        else:
            break
    return val

def main():
    
    imgWidth = 96
    imgHeight = 144

    if len(sys.argv) < 3:
        print('Must have 2 arguments. %s input.image output.bin' % sys.argv[0])
        return 0

    if len(sys.argv) == 5:
        imgWidth = int(sys.argv[3])
        imgHeight = int(sys.argv[4])

    print(str(imgWidth) + " - " + str(imgHeight))

    outf = open(sys.argv[2], 'wb')

    im = Image.open(sys.argv[1]).convert("L")
    newim = Image.new('L', (imgWidth, imgHeight), 'white')

    x,y = im.size
    newim.paste(im, (0, 0))
    outf.write(bytes('t4bp', 'iso8859_2'))

    px = []
    for p in newim.getdata():
        px.append(p)
        if len(px) == 2:
            byte_val = bin(reduce_color(px[0]))[2:].zfill(4) + bin(reduce_color(px[1]))[2:].zfill(4)
            outf.write(int(byte_val, 2).to_bytes(1,byteorder='big'))
            px = []
        elif len(px) > 2:
            print('Fatal error : px length increased past 2.')
            return 0

    outf.close()

if __name__ == '__main__':
    main()
