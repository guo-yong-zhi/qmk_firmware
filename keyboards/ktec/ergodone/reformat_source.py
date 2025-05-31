from argparse import ArgumentParser
import os
parser = ArgumentParser()
parser.add_argument('--file', default='keymap.c', help='''/home/SENSETIME/guoyongzhi/work/win10/qmk_firmware/bin/qmk-compile-json
处理https://config.qmk.fm生成的json生成的keymap.c''')
args = parser.parse_args()
fn = args.file
if not fn.endswith('.c'):
    fn = os.path.join(fn, 'keymap.c')

n_in_line = [7,7,6,7,5,2,1,3] * 2
n_at_begin = [0,0,0,0,0,5,6,4] + [0,0,1,0,2,0,0,0]

with open(fn) as f:
    code = f.readlines()

def gencode_layout(ks, n_in_line, n_at_begin, maxlen=16):
    ks = [k.replace("KC_TRNS", '_______').replace("KC_NO", 'XXXXXXX') for k in ks]
    ks = [' '*(maxlen-len(k))+k if len(k)<maxlen else k for k in ks]
    code_strs = []
    b = 0
    code_strs.append('\n//=====================left=====================')
    for lnum in range(len(n_in_line)//2):
        code_strs.append('\n'+' '*(maxlen+1)*n_at_begin[lnum])
        code_strs.append(','.join(ks[b:b+n_in_line[lnum]]))
        code_strs.append(',')
        b += n_in_line[lnum]

    code_strs.append('\n\n//=====================right=====================')
    for rnum in range(len(n_in_line)//2, len(n_in_line)):
        code_strs.append('\n'+' '*(maxlen+1)*n_at_begin[rnum])
        code_strs.append(','.join(ks[b:b+n_in_line[rnum]]))
        b += n_in_line[rnum]
        code_strs.append(',')
    code_strs.pop()
    code_strs.append('\n')
    return code_strs

def gencode_line(l, n_in_line, n_at_begin, b, e, maxlen=16):
    code_strs = []
    lc = l[b:e]
    ks = lc.split(', ')
    layoutcode = gencode_layout(ks, n_in_line, n_at_begin, maxlen)
    code_strs.append(l[:b])
    code_strs.extend(layoutcode)
    code_strs.append(l[e:])
    return code_strs

def gencode_lines(code, maxlen=16):
    newcode = code[:9]
    for i,l in enumerate(code[9:-2]):
        newcode.extend('//'*15 + str(i) + '//'*15 +'\n')
        newcode.extend(gencode_line(l, n_in_line, n_at_begin, 22, -3, maxlen))

    newcode.extend('//'*15 + str(i+1) + '//'*15 +'\n')
    newcode.extend(gencode_line(code[-2], n_in_line, n_at_begin, 22, -2, maxlen))
    newcode.extend(code[-1:])
    return newcode
code_strs = gencode_lines(code)
with open(fn, 'wt') as f:
    f.write(''.join(code_strs))

