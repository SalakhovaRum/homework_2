import argparse
parser=argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("search_text")
args=parser.parse_args()
text1=args.text
text2=args.search_text

idx=0

def Search(text1,text2):
    for j in range(len(text1)-len(text2)+1):
        mark=0
        for i in range(len(text2)+1):
            if (text1[j+i]==text2[i]):
                mark+=1
            else:
                mark=0
                break
            if mark==len(text2):
                print(j)
                return j
Search(text1, text2)
