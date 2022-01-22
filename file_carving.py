import sys

def main(argv):

    #Checks that start offset argument is a '-' and that the other arguments are not, and then computes it
    if argv[1]=="-" and argv[2]!="-" and argv[3]!="-":
        end_offset = int(argv[2], 16)
        length = int(argv[3], 10)
        so = end_offset - length
        print("New start offset is " + hex(so))
    
    #Checks that end offset argument is a '-' and that the other arguments are not, and then computes it
    elif argv[2]=="-" and argv[1]!="-" and argv[3]!="-":
        start_offset = int(argv[1], 16)
        length = int(argv[3], 10)
        eo = start_offset + length
        print("New end offset is " + hex(eo))
    
    #Checks that length argument is a '-' and that the other arguments are not, and then computes it
    elif argv[3]=="-" and argv[1]!="-" and argv[2]!="-":
        start_offset = int(argv[1], 16)
        end_offset = int(argv[2], 16)
        kl = end_offset - start_offset
        print("Length is " + str(kl) + " bytes")
    
    else:
        print("Check that at least two arguments have been provided and that the one you want is a '-'.")

if __name__=="__main__":
    main(sys.argv)
