# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 00:05:39 2023

@author: stuti
"""

import pandas as pd
import random
data=pd.read_csv("finally_final_spyder.csv")
#print(data)

question=data.loc[:,"Question"]
#print(question)

answer=data.loc[:,"Answer"]
#print(answer)


distractor1=data.loc[:,"Distractor 1"]
#print(distractor1)


distractor2=data.loc[:,"Distractor 2"]
#print(distractor2)

distractor3=data.loc[:,"Distractor 3"]
#print(distractor3)

distractor4=data.loc[:,"Distractor 4"]
#print(distractor4)

dl=data.loc[:,"Difficulty"]

import random

def shuffle_questions(question, dl, distractor1, distractor2, distractor3, distractor4, answer):
    shuffled_q = []
    asked_ques = set()
    mcqs = list(zip(question, dl, distractor1, distractor2, distractor3, distractor4, answer))
    random.shuffle(mcqs)  # Shuffle the questions once at the beginning
    for mcq in mcqs:
        ques, dl, d1, d2, d3, d4, ans = mcq
        shuffled_mcq = {
            "Question": ques,
            "Difficulty Level": dl,
            "Distractor 1": d1,
            "Distractor 2": d2,
            "Distractor 3": d3,
            "Distractor 4": d4,
            "Answer": ans
        }
        shuffled_tuple = tuple(shuffled_mcq.items())
        if shuffled_tuple not in asked_ques:
            shuffled_q.append(shuffled_mcq)
            asked_ques.add(shuffled_tuple)
    return shuffled_q


#question=question.tolist()
mcq_list=shuffle_questions(question, dl,distractor1,distractor2,distractor3,distractor4,answer) 
#print(mcq_list)

def get_mcq(shuffled_q):
    if shuffled_q:
        return shuffled_q.pop(0)
    else:
        return None

#n=input("Enter number of questions: ")
#n=(int)(n)
#user_dl=("Enter difficulty level")
q1=[]
dl=[]
d11=[]
d12=[]
d13=[]
d14=[]
a1=[]
def call_func(level):
    for i in range(0,40):
        m=get_mcq(mcq_list)
#for i in range(0,40):
 #       m=get_mcq(mcq_list)
        #if(m['Difficulty Level'].lower()==level.lower()):
        q1.append(m['Question'])
        dl.append(m['Difficulty Level'])
        d11.append(m['Distractor 1'])
        d12.append(m['Distractor 2'])
        d13.append(m['Distractor 3'])
        d14.append(m['Distractor 4'])
        a1.append(m['Answer'])
call_func('Easy')
import re
import string


def modify_values(text,d1,d2,d3,d4,a1):
    
#     def execute_python_code(code_string):
#         try:
#             # Execute the Python code
#             exec(code_string)
#         except Exception as e:
#             print(f"Error executing the code: {e}")
        
#     def change_digit(code_string):
#         digit_to_replace = re.findall(r'\d', code_string)
#         each_digit in digit_to_replace:
#             code_string = code_string.replace(each_digit, random.randint(0, 9))
#         return code_string
    
#     question_text = text
#     string_to_replace = re.findall(r"['\"]+(?!%s)(.*?)['\"]+", text)
#     each_string in string_to_replace:
#         new_replaced_words = []
#         each_word in string_to_replace.split():
#             new_replaced_string += get_random7() 
#         new_replaced_string = ' '.join(new_replaced_words)
#         question_text = question_text.replace(string_to_replace, new_replaced_string)
#     question_text = change_digit(question_text)
#     print("qs->\n", question_text)
#     answer = execute_python_code(question_text)
#     print("a->", answer)
#     option1 = execute_python_code(change_digit(question_text))
#     print("o1->", option1)
#     option2 = execute_python_code(change_digit(question_text))
#     print("o2->", option2)
#     option3 = execute_python_code(change_digit(question_text))
#     print("o3->", option3)
#     option4 = execute_python_code(change_digit(question_text))
#     print("o4->", option4)
    
    
    
    
    
    pattern1=[
        #r",\s?(\d)",
        
        r":(\d)"
        #r"(?<!\[)(?<!\d:)\:(\d)"
        #r"{(?!\d{2}:\d{2})\s*\d+\s*:\s*\d+\s*|\s*\d+\s*:\s*\d+(?<!\d{2}:\d{2})\s*}"
        #r"\[(?!\d{2}:\d{2})\d+:\d+|\d+:\d+(?<!\d{2}:\d{2})\]"
    ]
    pattern2=[
        r"'(?!%s)(.*?)'",
        r'"(?!%s)(.*?)"'
        #r'(?<!x\d\d)x[^\dx]+\d\d(?!x\d\d)|[\'"]([^\'"]+)[\'"]'
        #r'(?<!x\d\d)x[^\dx]+\d\d(?!x\d\d)|([\'"])(?:(?!\1).)+\1'
        #r'(["\'])([a-zA-Z0-9]+)\1'
        #r'(["\'])([a-zA-Z0-9]+)(?!\.)\1'
        #r'\'(\b\w+\b)\'',  # Single-quoted words (e.g., 'word')
        #r'\"(\b\w+\b)\"'   # Double-quoted words (e.g., "word")
       # r'"([^"\n]*\S[^"\n]*)"',
       # r"'([^'\n]*\S[^'\n]*)'"
    ]
    pattern3=[
        r"[A-Z]"
    ]
    pattern4=[
        r"[a-z]"
    ]
    pattern5=[
        r"\d"
    ]
    pattern6=[
        r'\$\d+'
    ]
    pattern7=[
        r"\d+:\d+",
        r"^(\w+)\[(\d+):(\d+):(\d+)\]$"
    ]
    pattern8=[
       r"x = (\d+)"

    ]
    pattern9=[
        r"(\d):",
        #r"(\d)(?!\d:\])(?!\])\:",
        r'print\((\w+)\[-1:\]\)'
    ]
    pattern10=[
        r"::-(\d+)"
    ]
    pattern11=[
        #r'\.([a-zA-Z_]+)\(\)'
        r'\.([a-zA-Z_]+\(\))'
        #r'(?<=\b\w\.)\w+\(\)'
    ]
    pattern12=[
        r"\w+\[:\d+\] \+ '\w+' \+ \w+\[\d+:\]"
    ]
    pattern13=[
       #r'(\w+)\+(\w+)'
        r'"([^"]+)"\s*\+\s*"([^"]+)"',
        r'(".*?"|\'.*?\'|\b\w+\b)\s*\+\s*(\w+)'
    ]
    pattern14=[
        r'\.count',
        r'"(\w+)"\.count\("(\w+)",(\d+),(\d+)\)'
    ]
    pattern15=[
        r',\s?(\d+)'
    ]
    pattern16=[
        r'len\(\[.*?\]\)'
    ]
    pattern17=[
        r'len\(\s*\[(.*?)\]\s*\)'
        
    ]
    pattern18=[
        r'len\((.*?)\)'
    ]
    pattern19=[
        r'print\s+(\w+)'
    ]
    pattern20=[
        r'print\((\w+)\*(\d+)\)',
        #r'(\w+)\[(\d+)\]',
        r'print\((\w+)\s*\[([+-]?\d+)\]\)',
        r'print\((\w+)\[(?:-?\d+)\] \+ \1\[(?:-?\d+)\]\)',
        r'print\((\w+)\[(\d+):(\d+)\] \* (\d+)\)'
    ]
    pattern21=[
        r'print(\((?:print\()*(?:"|\')?(\w+)(?:"|\')?\))*(?:\))',
    ]
    for pattern in pattern8:
        matches = re.findall(pattern, text)
        #print("m",matches)
        for match in matches:
            #print("Rule1 - changes the number after '=' ")
            
            random_value = get_random1()
            text="x = "+random_value+"\n for i in x:\n\tprint(i,end="" "")"
            #print("rv",random_value)
            #match = match.replace(i, random_value)
            d1=""
            d2=""
            for i in random_value:
                d1=d1+" "+i
            for i in range(0,3):
                d2=d2+" "+random_value[0]
            d3="Error"
            d4="No output"
            for i in random_value:
                a1=i+" "
            text = text.replace(match, str(random_value))
            
    c=0
    word1=[]
    random_value=""
    for pattern in pattern2:
        matches = re.findall(pattern, text)
        for match in matches:
            #print("Rule2 - replaces the words with random words from a corpus")
            if len(match)>1:
                random_value=get_random7()
                word1.append(random_value)
                #word=modified_match
                #print(word1)
            else:
                random_value=get_random2()
                word1.append(random_value)
            text = text.replace(match, random_value)
            #print("hi ",text)
    
    #random_value1=""
    #random_value2=""
    '''
    #if word1!=[]:
     #   word=word1[0]  
      #  print(word)
       # for pattern in pattern21:
        #    matches=re.findall(pattern,text)
         #   print(matches)
          #  print("15")
           # d1=word+" None"+" None"
            #d2="None "+word+" None"
            #d3="None "+"None "+word
            #d4="Error"
            #a1=d1
            '''
    
    if word1!=[]:
        word=word1[0]
        #print(word1)
        for pattern in pattern14:
            matches=re.findall(pattern,text)
            if matches:
                #print("Rule3 - changes the values of the question haning count function")
                if re.findall(pattern14[1],text):
                    modified_word=word1[0]+word1[1]+word1[0]
                    c=len(word1[1])
                    c1=len(word1[0])
                    #random_value1=get_random9(c1)
                    #random_value2=get_random10(c)
                    text=text.replace(word1[1],modified_word)
                    for pat in pattern15:
                        matches1=re.findall(pat,text)
                        if matches1:
                            text=text.replace(matches1[0],str(c1))
                            #print(c1+c+1)
                            text=text.replace(matches1[1],str(c1+c+1))
                    #random_value1=int(random_value1)
                    #random_value2=int(random_value2)
                            d1=3
                            #print(word1[1])
                            #print(modified_word)
                            #print(random_value1+1)
                            #print(random_value2)
                            d2=0
                            d3="Error"
                            d4=modified_word.count(word1[1],c1,c1+c+1)
                            a1=modified_word.count(word1[1],c1,c1+c+1)
                else:
                    d1=3
                    #print(word1[1])
                    #print(modified_word)
                    #print(random_value1+1)
                    #print(random_value2)
                    d2=0
                    d3="Error"
                    d4=word[0].count(word1[1])
                    a1=d4
                    
    if len(word1)>1:
        word=word1[0]
        #print(word1)
        #text=word1[0]+"+"+word1[1]
        for pattern in pattern13:
            matches = re.findall(pattern, text)
            #print("t",text)
            if matches:
                #text="print("word1[0]+"+"+word1[1]")"
                #text=text +'for i in x:\n print(i, end=" ") '
                #print("Rule4 - concatenate two strings")
                #print(word1[0]+" ")
                #print(word1[1])
                #print(matches)
                #word2 = word1[0]
                #word3 = word1[1]
                #print(f"word1: {word2}")
                #print(f"word2: {word3}")
                d1=""
                d2=""
                d3=""
                d4=""
               # print(text)
                for i in range(0,len(word1)):
                    d1 = d1+" "+word1[i] 
                    d2 = word1[i]+d2
                    d3 = d3+word1[i]
                    d4 = word1[i] + " " + d4
                if re.findall(pattern13[1],text):
                    a1=d2
                else:
                    a1 = d3
    
    if word1!=[]:
        word=word1[0]
        c=len(word)
        random_value1=""
        #random_value2=""
        for pattern in pattern12:
            matches=re.findall(pattern,text)
            for match in matches:
                #print("Rule5 - ")
                for pat in pattern9: 
                    matches1=re.findall(pat,match)
                    random_value1=get_random6(c)
                    for m in matches1:
                        text=text.replace(m,random_value1)
                    #print(text)
                    random_value1=(int)(random_value1)
                    #print( word[(random_value1+1):] +" ")
                    #print(random_value1)
                    d1 =word[:(random_value1-1)] + str(word1[1]) +  word[(random_value1+1):] 
                    d2 = word[:(random_value1)]  + str(word1[1]) +  word[(random_value1-1):]
                    #print( word[(random_value1+1):] +" ")
                    d3 = word[:(random_value1+1)] + str(word1[1]) + word[(random_value1+2):]
                    d4 = word[:(random_value1)] + str(word1[1]) + word[(random_value1):]
                    a1 = word[:(random_value1)]+ str(word1[1]) + word[(random_value1):] 
                    #print(d3)
    
    if word1!=[]:                    
        word=word1[0]
        c=len(word)
        #word=word1[0]
        random_value=""
        #print("printing",word)
        random_value = ""
        m=re.findall(pattern9[1],text)
        for pattern in pattern9:
            matches=re.findall(pattern, text)
            for match in matches:
                #print("Rule6 - ")
                random_value=get_random6(c)
                text=text.replace(match,random_value) 
                random_value=(int)(random_value)
                if m:
                    d1=d1=word[(random_value+1)*-1:]
                    d2=word[(random_value-1)*-1:]
                    d3=word[(random_value+2)*-1:]
                    if (random_value+2)>=c:
                        d3="Error"
                    d4=word[(random_value)*-1:]
                    a1=word[(random_value)*-1:]
                    
                elif len(word1)>1:
                    d1=word[(random_value+1):]+word1[1]
                    d2=word[(random_value-1):]+word1[1]
                    d3=word[(random_value+2):]+word1[1]
                    if (random_value+2)>=c:
                        d3="Error"
                    d4=word[(random_value):]+word1[1]
                    a1=word[(random_value):]+word1[1]
                else:
                    d1=word[(random_value+1):]
                    d2=word[(random_value-1):]
                    d3=word[(random_value+2):]
                    if (random_value+2)>=c:
                        d3="Error"
                    d4=word[(random_value):]
                    a1=word[(random_value):]
                    word=a1
                    print(word)
                    
        word=word1[0]
        c=len(word)        
        random_value = ""    
        for pattern in pattern1:
            matches=re.findall(pattern, text)
            for match in matches:
                #print("Rule7")
                random_value=get_random6(c)
                #print(random_value)
                text=text.replace(match,random_value) 
                random_value=(int)(random_value)
                if len(word1)>1:
                    d1=word[:(random_value)]+word1[1]
                    d2=word[:(random_value-2)]+word1[1]
                    d3=word[:(random_value+1)]+word1[1]
                    d4=word[:(random_value-1)]+word1[1]
                    a1=word[:(random_value)]+word1[1]
                else:
                    d1=word[:(random_value)]
                    d2=word[:(random_value-2)]
                    d3=word[:(random_value+1)]
                    d4=word[:(random_value-1)]
                    a1=word[:(random_value)]
                    word=a1
                    #print(word)
        
        word=word1[0]
        c=len(word)           
        random_value = ""
        f=0
        for pattern in pattern7:
            
            matches=re.findall(pattern,text)
            maches2=re.findall(pattern7[1],text)
            if re.findall(r'-\d+',text):
                    f=1
                    #print("yo")
            random_value1="2"
            random_value2="1"
            
            for match in matches:
                #print("match")
                if ":" in match:
                   # print("Rule8")
                    start, end = match.split(":")
                    while random_value1>=random_value2:
                        random_value1 = get_random6(c)
                        #print(random_value1)
                        random_value2 = get_random6(c)
                        #print(random_value2)
                    #print(random_value1+" "+random_value2)
                    modified_expression=f'{random_value1}:{random_value2}'
                    #print(modified_expression)
                    text=text.replace(match,modified_expression)
                    if f==1:
                        random_value1=(int)(random_value1)*-1
                        #print("rv ",random_value1)
                        random_value2=(int)(random_value2)*-1
                    else:
                        random_value1=(int)(random_value1)
                        #print("rv ",random_value1)
                        random_value2=(int)(random_value2)
                    r=random_value2-random_value1
                    
                    if r==1:
                        d1=word[(random_value1):(random_value2+1)]
                    else:
                        d1=word[(random_value1+1):(random_value2+1)]
                    d2=word[(random_value1):(random_value2)]
                    if random_value1 != 0 and random_value2 != c-1:
                        d3=word[(random_value1-1):(random_value2+1)]
                    else:
                        d3="No Output"
                    
                    d4="Error"
                    a1=word[(random_value1):(random_value2)]
                    word=a1
                    ##print(word)
                    
                    
        
    '''
    #for pattern in pattern6:
      #  matches=re.findall(pattern, text)
       # for match in matches:
            
        #    random_value=get_random5()
         #   text=text.replace(match,random_value)
    '''
    if word1!=[]:
        #word=word1[0]
        c=len(word)
        random_value=""
        for pattern in pattern10:
            matches=re.findall(pattern, text)
            #print("matches",matches)
            for match in matches:
                #print("Rule9")
                random_value=get_random6(c)
                #print(random_value)
                text=text.replace(match,random_value)
                #print("t",text)
                #text=""
                random_value=(int)(random_value)*-1#if statements
                #print(random_value)
                d1=word[::(random_value)]
                d2="Error"
                d3=word[::(random_value-2)]
                d4=word[::(random_value-1)]
                a1=word[::(random_value)]
                word=a1
    
    
    if word1!=[]:
        ##word=word1[0]
        #print(word)
        #c=len(word)
        random_value=""
        for pattern in pattern11:
            matches=re.findall(pattern,text)
            #print(matches)
            for match in matches:
                #print("Rule10")
                random_value=get_random8()
                #print(random_value)
                text=text.replace(match,random_value)
                if len(word1)==1:
                    if random_value == 'title()':
                        d1=word.title()
                        a1=word.title()
                    elif random_value == 'upper()':
                        d1=word.upper()
                        a1=word.upper()
                    elif random_value == 'lower()':
                        d1=word.lower()
                        a1=word.lower()
                    elif random_value == 'swapcase()':
                        d1=word.swapcase()
                        a1=word.swapcase()
                    elif random_value == 'titlecase()':
                        d1=word.titlecase()
                        a1=word.titlecase()
                    elif random_value == 'strip()':
                        d1=word.strip()
                        a1=word.strip()
                    elif random_value == 'split()':
                        d1=word.split()
                        a1=word.split()
                    elif random_value == 'isalpha()':
                        d1=word.isalpha()
                        a1=word.isalpha()
                    elif random_value == 'isidentifier()':
                        d1=word.isidentifier()
                        a1=word.isidentifier()
                else:
                    d1=[]
                    a1=[]
                    for i in range(0,len(word1)):

                        if random_value == 'title()':
                            d1.append(word1[i].title())
                            a1.append(word1[i].title())
                        elif random_value == 'upper()':
                            d1.append(word1[i].upper())
                            a1.append(word1[i].upper())
                        elif random_value == 'lower()':
                            d1.append(word1[i].lower())
                            a1.append(word1[i].lower())
                        elif random_value == 'swapcase()':
                            d1.append(word1[i].swapcase())
                            a1.append(word1[i].swapcase())
#                         elif random_value == 'titlecase()':
#                             d1.append(word1[i].title())
#                             a1.append(word1[i].title())
                        elif random_value == 'strip()':
                            d1.append(word1[i].strip())
                            a1.append(word1[i].strip())
                        elif random_value == 'split()':
                            d1.append(word1[i].split())
                            a1.append(word1[i].split())
                        elif random_value == 'isalpha()':
                            d1 = word1[i].isalpha()
                            a1 = word1[i].isalpha()
                        elif random_value == 'isidentifier()':
                            d1 = word1[i].isidentifier()
                            a1 = word1[i].isidentifier()

                d2 = word.lower()
                if d1==d2:
                    d2=d1[0]
                d3 = "Error"
                d4 = "No output"
                
    random_value=""
    for pattern in pattern17:
        matches=re.findall(pattern,text)
        for match in matches:
                #print("Rule11")
                print(match)
                if match:
                    modified_m=[]
                    modified_m.append(match)
                    print(modified_m)
                    random_value=get_random4()
                    for i in range(0,int(random_value)):
                        modified_m.append(get_random1())
                        print(modified_m)
                    text=text.replace(match,str(modified_m))
                    d1="Error"
                    d2=len(modified_m)-1
                    d3=len(modified_m)
                    d4=len(modified_m)+1
                    a1=len(modified_m)
                    
    if word1!=[]:
        #word=word1[0]
        for pattern in pattern18:
            matches=re.findall(pattern,text)
            if matches:
                #print('Rule12')
                d1="Error"
                d2="No Output"
                d3=len(word)
                d4=len(word)+2
                a1=len(word)
                
    if word1!=[]:
        #word=word1[0]  
        #print(word)
        for pattern in pattern19:
            matches=re.findall(pattern,text)
            #print(matches)
            for i in matches:
                #print('Rule13')
                d1=i
                d2=word
                d3="{word}"
                d4="Error"
                a1=d4
    
    random_value=""
    m=re.findall(pattern20[1],text)
   # print("m",m)
    m1=re.findall(pattern20[3],text)
    m3=re.findall(pattern20[2],text)
    for pattern in pattern20:
        matches=re.findall(pattern,text)
        #print(matches)
        #print("t",text)
        if m1:
            #print("yes")
            for match1 in m1:
                vn,n1,n2,k=match1
            random_val=get_random4()
            text=text.replace(k,random_val)
            #print(random_val)
            #print("tt",text)
            d1=""
            for j in range(0,int(random_val)):
                d1=d1+word
            d2=word
            d3="No Output"
            d4="Error"
            a1=d1
            break
        else:                    
            for i in matches:
                #print('Rule14')
               # print(i)               
                for k in i:
                    if m:
                        if k.startswith('-'):
                            if k[1:].isdigit():
                                random_val=get_random4()
                                text=text.replace(k,"-"+random_val)
                                #print(random_val)
                                random_val=int(random_val)*-1   
                                #print(random_val)
                                d1=word[random_val]
                        elif k.isdigit():
                            random_val=get_random4()
                            text=text.replace(k,random_val)
                            d1=word[int(random_val)-1]
                    elif m3:
                        #print("yeye")
                        w1=""
                        w2=""
                        #print(k)
                        if k.startswith('-'):
                            #print("y")
                            if k[1:].isdigit():
                                #print("y1")
                                random_val=get_random4()
                                text=text.replace(k,"-"+random_val)
                                random_val=int(random_val)*-1   
                                w1=word[random_val]
                                #print(w1)
                        if k.isdigit():
                            #print("y2")
                            random_val=get_random4()
                            text=text.replace(k,random_val)
                            w2=word[int(random_val)-1]
                            #print(w2)
                        d1=""
                        d1=w1+w2
                    elif k.isdigit():
                        random_val=get_random4()
                        #print(random_val)
                        text=text.replace(k,random_val)
                        d1=""
                        for j in range(0,int(random_val)):
                            d1=d1+word
                d2=word
                d3="No Output"
                d4="Error"
                a1=d1
    
    
    

    
    
    
    
    
    return text, d1, d2, d3, d4, a1



import nltk

nltk.download('words')




from nltk.corpus import words
import random

word_list = words.words()
import random

def get_random1():
    return str(random.randint(1,1000))
def get_random2():
    return random.choice(string.ascii_letters)
def get_random3():
    return random.choice(string.ascii_lowercase)
def get_random4():
    return str(random.randint(2,5))
def get_random5():
    return 'Rs'
def get_random6(c):
    return str(random.randint(1,c-1)) 
#def get_random7(num1,num2):
def get_random7():
    str1=""
    str1=random.choice(word_list)
    return str1
def get_random8():
    l=['title()','upper()','lower()','swapcase()','strip()','split()','isalpha()','isidentifier()']
    return random.choice(l)
#def get_random9(c1):
  #  return str(random.randint(c1,3))
#def get_random10(c,c1):
  #  return str(random.randint(20,30))

    
    
    
    

# import re
# import string
# import contextlib
# import io


# def modify_values(text):
    
#     def execute_python_code(code_string):
#         output_stream = io.StringIO()
#         try:
#             # Execute the Python code and capture the standard output
#             with contextlib.redirect_stdout(output_stream):
#                 exec(code_string)
#             # Get the captured output and convert it to a string
#             captured_output = output_stream.getvalue()
#             return captured_output
#         except Exception as e:
#             return f"Error executing the code: {e}"
        
#     def change_digit(code_string):
#         digit_to_replace = re.findall(r'\d', code_string)
#         for each_digit in digit_to_replace:
#             code_string = code_string.replace(each_digit, str(random.randint(1, 9)))
#         return code_string
    
#     question_text = text
#     string_to_replace = re.findall(r"['\"]+(?!%s)(.*?)['\"]+", text)
#     print ('string_to_replace -> ', string_to_replace)
#     for each_string in string_to_replace:
# #         print ('each String ->', each_string)
#         new_replaced_words = []
#         for each_word in each_string.split(' '):
# #             print('each word->', each_word)
#             new_replaced_words.append(get_random7()) 
# #             print('new word->', new_replaced_words)
#         new_replaced_string = ' '.join(new_replaced_words)
#         print('new string->',new_replaced_string )
#         question_text = question_text.replace(each_string, new_replaced_string)
#     question_text = change_digit(question_text)
#     print("qs->\n", question_text)
#     answer = execute_python_code(question_text)
#     print("a->", answer)
#     #option1 = execute_python_code(change_digit(question_text))
#     print("o1->", answer)
#     option2 = execute_python_code(change_digit(question_text))
#     print("o2->", option2)
#     #option3 = execute_python_code(change_digit(question_text))
#     print("o3-> Error")
#     #option4 = execute_python_code(change_digit(question_text))
#     print("o4-> No output")
    
    
    
# for x in q1:
#     modify_values(x)

def new_mcqs(q1,d11,d12,d13,d14,a1):
    #q1 = q1 or ""
    #d11 = d11 or ""
    #d12 = d12 or ""
    #d13 = d13 or ""
    #d14 = d14 or ""
    #a1 = a1 or ""
    options=[]
    options.append(d11)
    options.append(d12)
    options.append(d13)
    options.append(d14)
    new_q1,new_d11,new_d12,new_d13,new_d14,new_a1=modify_values(q1,d11,d12,d13,d14,a1) 
    
    #print(new_q1)
    '''new_mcq={ 
        "Question": new_q1, 
        "Difficulty Level: ",dl,
        "Distractor 1": new_d11, 
        "Distractor 2": new_d12, 
        "Distractor 3": new_d13, 
        "Distractor 4": new_d14, 
        "Answer": new_a1 } '''
    return new_q1, new_d11, new_d12, new_d13, new_d14, new_a1
def new_mcq_func(num_ques:int, num_papers:int):
    mcqs_array ={

    }

    for j in range(0, num_ques):
        ques = []
        dist1 = []
        dist2 = []
        dist3 = []
        dist4 = []
        ans = []
        mcqs={}
        print("Original Question: ",q1[j])
        print("A. ",d11[j])
        print("B. ",d12[j])
        print("C. ",d13[j])
        print("D. ",d14[j])
        print("\n")
        print("\n")
        for i in range(0, num_papers):
            #print("qqq111: ",q1[j])
            new_q1, new_d11, new_d12, new_d13, new_d14, new_a1 = new_mcqs(q1[j], d11[j], d12[j], d13[j], d14[j], a1[j])
            print(f"Question {i+1}: ",new_q1)
            print("A. ",new_d11)
            print("B. ",new_d12)
            print("C. ",new_d13)
            print("D. ",new_d14)
            print("\n")
            ques.append(new_q1)
            dist1.append(new_d11)
            dist2.append(new_d12)
            dist3.append(new_d13)
            dist4.append(new_d14)
            ans.append(new_a1)

        mcqs = {
            "ques": ques,
            "dist1": dist1,
            "dist2": dist2,
            "dist3": dist3,
            "dist4": dist4,
            "ans": ans
        }
        mcqs_array[f"mcq{j+1}"] = mcqs
    #print("\naaaaaaaaannnnnnnnnnnnnnnnnnnssssssssssssssssssssssssss : ",mcqs_array)
    return mcqs_array
soln=(new_mcq_func(5,5))
'''print("hello")
for i in range(0, 5):  
    print(f'Question{i+1}.: {soln[f"mcq{i+1}"][f"ques"][i]}')
    print("\n")
'''     


#print(mcqs)



'''import csv

new_q1 = []
new_dl = []
new_d11 = []
new_d12 = []
new_d13 = []
new_d14 = []
new_a1 = []
header=["Question","Difficulty","Answer","Distractor 1","Distractor 2","Distractor 3","Distractor 4"]
for i in range(0, n):
    print("\n")
    new_q, new_dl_val, new_d11_val, new_d12_val, new_d13_val, new_d14_val, new_a = new_mcqs(q1[i], dl[i], d11[i], d12[i], d13[i], d14[i], a1[i])
    new_q1.append(new_q)
    new_dl.append(new_dl_val)
    new_d11.append(new_d11_val)
    new_d12.append(new_d12_val)
    new_d13.append(new_d13_val)
    new_d14.append(new_d14_val)
    new_a1.append(new_a)
    data=[new_q, new_dl_val, new_a, new_d11_val, new_d12_val, new_d13_val, new_d14_val]
    with open("finally_final.csv","a",newline="",encoding="utf-8") as csvfile:
        writer=csv.writer(csvfile)
        #writer.writerow(header)
        writer.writerow(data)
for i in range(0, n):

    print("\n")
    
    print("Question: ",new_q1[i])
    print("Difficulty Level: ",dl[i])
    print("A. ",new_d11[i])
    print("B. ",new_d12[i])
    print("C. ",new_d13[i])
    print("D. ",new_d14[i])
    print("ANS. ",new_a1[i])




    #newRow = "\n%s,%s,%s,%s,%s,%s,%s\n" % (new_q1, dl, new_a1, new_d11, new_d12, new_d13, new_d14)
    #with open("abcd2.csv", "a") as f:
        #f.write(newRow)
    #print(new_q1, dl, new_d11, new_d12, new_d13, new_d14, new_a1)
'''
'''def final_question_paper(num):
    for i in range(0,5):
        print("Ques: "+question[i])
        print("Difficulty Level: "+dl[i])
        print("Option 1: "+distractor1[i])
        print("Option 2: "+distractor2[i])
        print("Option 3: "+distractor3[i])
        print("Option 4: "+distractor4[i])
        print("\n")
'''


'''
from fpdf import FPDF
class PDF(FPDF):
    
    def header(self):
        self.set_font('arial','BIU',16)
        self.cell(0,10,'Question Paper',border=0,ln=1,align='C')
        self.ln(8)
        self.set_font('arial','B',14)
        self.cell(0,10,'Topic - String (Python)',border=0,ln=1,align='C')
        self.set_font('arial','B',12)
        self.cell(0,10,'Name: ....................',border=0,ln=1)
        self.cell(0,10,'Enrollment Number: ...................',border=0,ln=1)
        self.cell(0,10,"---------------------------------------------------------------------------------------------------------------------------------------------------------------",border=0,ln=1)
        self.ln(20)
    def footer(self):
        self.set_y(-15)
        self.set_font('arial','',8)
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')
pdf=PDF('P','mm','Letter')
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True,margin=15)

pdf.add_page()








def check_error(text):
    try:
        # Try encoding the text using 'latin-1'
        encoded_text = text.encode('latin-1', errors='replace')
        print(encoded_text.decode('latin-1'))
    except UnicodeEncodeError as e:
        print(f"Error: {e}")




        




pdf.set_font('times','',12)
for i in range(0, n):
    pdf.cell(0,8,f'Question{i+1}.: {new_q1[i]}',ln=1)
    #check_error(new_q1[i])
    pdf.cell(0,5,f'Option A. : {new_d11[i]}',ln=1)
    #check_error(new_d11[i])
    pdf.cell(0,5,f'Option B. : {new_d12[i]}',ln=1)
    #check_error(new_d12[i])
    pdf.cell(0,5,f'Option C. : {new_d13[i]}',ln=1)
    #check_error(new_d13[i])
    pdf.cell(0,5,f'Option D. : {new_d14[i]}',ln=1)
    #check_error(new_d14[i])
    pdf.ln(10)
pdf.output('qp_2.pdf')
'''
















