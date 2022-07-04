import re # re library를 이용

def palindrome(seq1):
    
    seq1=seq1.lower() # 대소문자의 구별을 없애기 위해
    
    seq2=seq1
    
    p=re.compile('[a-zA-Z]') # 모든 영문자를 찾아냄
    
    seq1_list=[]
    seq2_list=[]
    
    for x in seq1:
        if p.match(x):
            seq1_list.append(x)
    
    seq1_list.reverse() # 팰린드롬의 의미가 뒤집어도 같은 말이 되는 문장이나 단어이므로

    for x in seq2:
        if p.match(x):
            seq2_list.append(x)
    
    if seq1_list==seq2_list:
        print("palindrome입니다.")
    
    else:
        print("palindrome이 아닙니다.")
