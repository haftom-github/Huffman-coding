import Huffman
import pickle
import time
def compress(filename,enc='utf-8'):
    """
    Compresses a file using Huffman encoding and saves the compressed output to a new file with a `.comp` extension.

    This function generates a Huffman tree based on character frequency in the specified file,
    encodes the file contents accordingly, and writes the compressed binary data to a new file.
    The encoded data, encoding used, and Huffman tree are saved at the beginning of the file 
    for decompression purposes.

    :param filename: str - The path to the file to be compressed.
    :param enc: str - The encoding of the source file (default is 'utf-8').
    :return: int - The size of the compressed file in bytes.
    """
    t=Huffman.generateTree(Huffman.generateWeightDict(filename))
    d=Huffman.generateDict(t)
    st=time.time()
    byteno=0
    source=open(filename,'rt',encoding=enc)
    des=open(filename+'.comp','wb')
    pickle.dump(enc,des)
    pickle.dump(t,des)
    chunk=source.read(100)
    b=''
    while chunk:
       for ch in chunk:
           b+=d[ch]
           if len(b)>=16:
               des.write(bytes([int(b[0:8],base=2),int(b[8:16],base=2)]))
               b=b[16:]
               byteno+=2
       chunk=source.read(100)
    b+=d['end']
    while len(b)>=8:
        des.write(bytes([int(b[0:8],base=2)]))
        b=b[8:]
        byteno+=1
    if len(b)>0:
        des.write(bytes([int(b+'0'*(8-len(b)),base=2)]))
        byteno+=1
    des.close()
    source.close()
    print(time.time()-st)
    return byteno
print(compress('testsholder', ))