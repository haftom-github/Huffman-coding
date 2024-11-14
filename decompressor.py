import pickle
import time
def decompress(filename):

    """
    Decompresses a file that was compressed using Huffman encoding and restores the original text file.

    This function reads the compressed file, which contains encoding information and a Huffman tree,
    and decodes the binary data back to the original text. The restored file is saved without the
    `.comp` extension in the same directory.

    :param filename: str - The path to the compressed file.
    :return: int - The number of characters written to the decompressed file.
    """
    
    st=time.time()
    source=open(filename,'rb')
    enc=pickle.load(source)
    destination=open(filename.rstrip('.comp'),'wt',encoding=enc)
    t=pickle.load(source)
    b=bin(source.read(1)[0])[2:].zfill(8)
    i=0
    countchar=0
    temp=t.head
    while True:
        if temp.item:
            if temp.item=='end':
                break
            destination.write(temp.item)
            countchar+=1
            temp=t.head
            continue
        if i==8:
            b=bin(source.read(1)[0])[2:].zfill(8)
            i=0
        if b[i]=='1':
            temp=temp.right
            i+=1
            continue
        temp=temp.left
        i+=1
    print(time.time()-st)
    return countchar

if __name__ == "__main__":
    print(decompress('testsholder.comp'))
