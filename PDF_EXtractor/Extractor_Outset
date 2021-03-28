# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:06:11 2021

@author: SOL
"""

#간소화 되지 않은 아주 날것의 코드입니다. 

import os
root = "C://Users//SOL//Downloads//준성특허법률사무소"
directory = os.path.join(root)
os.chdir(directory)
folder_list = os.listdir()
for folder in folder_list:
    address = directory + "//" + folder
    os.chdir(address)
    file_list = os.listdir()
    for file in file_list:
        new_address = address + "//" + file 
        file_list.insert(file_list.index(file),new_address)
        file_list.remove(file)
    folder_list.insert(folder_list.index(folder),file_list)
    folder_list.remove(folder)


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.pdfpage import PDFPage
from io import StringIO 


def convert_pdf_to_text(pdf_file_path):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()    
    specification = open(pdf_file_path,"rb")

    page_count = 0 
    Page_List = []
    for page in PDFPage.get_pages(specification,pagenos,maxpages=maxpages, 
                                  password = password, caching = caching):

        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        interpreter.process_page(page)
        layout = device.get_result()
        Information_List = []
        # Pattent Certificate is 595.32 X 841.92 Pixel. Check layout. x0, x1, y0, y1.
        for obj in layout:
            if isinstance(obj, LTTextBox):
                x1, y1, x2, y2, text = obj.bbox[0], obj.bbox[1], obj.bbox[2], obj.bbox[3], obj.get_text()
                Information = (x1 + x2)/2, (y1 + y2)/2, text 
            Information_List.append(Information)
        Page_List.append(Information_List)
        
    specification.close()
    device.close()
    return Page_List

Page_List = convert_pdf_to_text(folder_list[0][0])


def List_Sum(List):
    if type(List[0]) == str:
        total = ""
    elif type(List[0]) == int or type(List[0]) == float:
        total = 0
    else :
        total = []
    for element in List:
        total += element
    return total 
        

def Arangement(Page_List):
    
    def Split_LR(Information_List):
        Right_Information_List = []
        Left_Information_List = []
        for information in Information_List:
            x, y, text = information
            if abs(x) > abs(x-595.32):
                Right_Information_List.append(information)
            else : 
                Left_Information_List.append(information)
        Right_Information_List.sort(key=lambda x:-x[1])
        Left_Information_List.sort(key=lambda x:-x[1])
        return (Left_Information_List,Right_Information_List)
    
    def Split_UD(Information_List,criterion_y):
        Above_Information_List = []
        Below_Information_List = []
        for information in Information_List:
            x, y, text = information  
            if y < criterion_y+10:
                Below_Information_List.append(information)
            else:
                Above_Information_List.append(information)
        Above_Information_List.sort(key=lambda x:-x[1])
        Below_Information_List.sort(key=lambda x:-x[1])    
        return (Above_Information_List,Below_Information_List)
    
    Page_Text_List = []
    Summary_Switch = False
    Little_Summary_Switch = False 
    for Information_List in Page_List:    

        Page_Text = ""
        for information in Information_List:
            x,y,text = information
            Page_Text += text        

        Little_Search_List = ["(51)","(52)","(56)","(72)","(73)","(74)"]
        for List in Little_Search_List:
            if List in Page_Text:
                Little_Summary_Switch = True 
                break
                
        
        if "(57)" in Page_Text:
            switch = 0 
            A_Information_List = []
            B_Information_List = []
            C_Information_List = []
            D_Information_List = []
            E_Information_List = []
            while not A_Information_List and not B_Information_List :
                for information in Information_List:
                    x, y, text = information
                    if switch == 0 and "(54)" in text:
                        Else,E_Information_List = Split_UD(Information_List,y)
                        AC_Information_List, BD_Information_List = Split_LR(Else)
                        switch = 1 
                    elif switch == 1 and "(51)" in text:
                        A_Information_List,C_Information_List = Split_UD(AC_Information_List,y)
                        switch = 2
                    elif switch == 2 and "(73)" in text:
                        B_Information_List,D_Information_List = Split_UD(BD_Information_List,y)
                        break 
                    else:
                        pass
            
            Page_Text = ""
            for information in A_Information_List:
                Page_Text += information[2]
            for information in B_Information_List:
                Page_Text += information[2]
            for information in C_Information_List:
                Page_Text += information[2]
            for information in D_Information_List:
                Page_Text += information[2]
            for information in E_Information_List:
                Page_Text += information[2]                
            Page_Text_List.append(Page_Text)
            
            Summary_Switch = True
            Little_Summary_Switch = False 
            
        elif Summary_Switch and Little_Summary_Switch:
            
            A_Information_List = []
            B_Information_List = []
            C_Information_List = []
            x1 , x2, x3, x4, x5, x6 = 0,0,0,0,0,0
            y1 , y2, y3, y4, y5, y6 = 0,0,0,0,0,0

            for information in Information_List:
                x, y, text = information
                if "(51)" in text : 
                    x1, y1, text1 = information
                elif "(52)" in text : 
                    x2, y2, text2 = information 
                elif "(56)" in text: 
                    x3, y3, text2 = information 
                elif "(72)" in text: 
                    x4, y4, text2 = information 
                elif "(73)" in text: 
                    x5, y5, text2 = information 
                elif "(74)" in text: 
                    x6, y6, text2 = information 
            
            y_criterion = max(y1,y2,y3,y4,y5,y6)
            C_Information_List, AB_Information_List = Split_UD(Information_List,y_criterion)
            A_Information_List, B_Information_List = Split_LR(AB_Information_List)
            
            Page_Text = ""
            for information in C_Information_List:
                Page_Text += information[2]            
            for information in A_Information_List:
                Page_Text += information[2]
            for information in B_Information_List:
                Page_Text += information[2]                
            Page_Text_List.append(Page_Text)    
        
            Summary_Switch = False 
            Little_Summary_Switch = False     
            
        else:
            Page_Text = ""
            Information_List.sort(key=lambda x:-x[1])
            for information in Information_List:
                Page_Text += information[2]
            Page_Text_List.append(Page_Text)
            
        
    return Page_Text_List

Page_Text_List = Arangement(Page_List)

def Extraction(Page_Text_List):

    certificate = {}
    certificate["공고일자"] = ""
    certificate["등록번호"] = ""
    certificate["등록일자"] = ""
    certificate["국제특허분류"] = ""
    certificate["CPC특허분류"] = ""
    certificate["출원번호"] = ""
    certificate["출원일자"] = ""
    certificate["공개번호"] = ""
    certificate["공개일자"] = ""
    certificate["선행기술조사문헌"] = ""
    certificate["특허권자"] = []
    certificate["발명자"] = []
    certificate["대리인"] = ""
    certificate["심사관"] = ""
    certificate["청구항의수"] = ""
    certificate["발명의명칭"] = ""
    certificate["요약서"] = ""
    certificate["청구범위"] = []
    certificate["기술분야"] = []
    certificate["배경기술"] = []
    certificate["해결하려는과제"] = []
    certificate["과제의해결수단"] = []
    certificate["발명의효과"] = []
    certificate["도면의간단한설명"] = []
    certificate["발명을실시하기위한구체적인내용"] = []
    certificate["부호의설명"] = []
    certificate["도면"] = []
    certificate["선행기술문헌"]=[]

    def ADD_From_To(Search_List,Line_List):
        
        Package_List = []
        Search_Number_List = []
        Search_List_arranged = []
        for i in range(len(Search_List)):
            Search_Number_List.append(None)        
        
        for List in Search_List:
            for Line in Line_List:
                if List in Line.replace(" ",""):
                    Search_Number_List[Search_List.index(List)] = Line_List.index(Line)
                    Search_List_arranged.append((List,Line_List.index(Line)))
        
        Search_Number_List.sort()
        Search_List_arranged.sort(key=lambda x:x[1])
        Search_List = []
        for List in Search_List_arranged:
            Search_List.append(List[0])
        
        for i in range(len(Search_Number_List)):
            
            if i <= len(Search_Number_List) -2:
                Edited_Line_List = Line_List[Search_Number_List[i]:Search_Number_List[i+1]]
            else :
                Edited_Line_List = Line_List[Search_Number_List[i]:]
                
            Edited_Text = "".join(Edited_Line_List)
            Package = (Search_List[i],Edited_Text,Search_Number_List[i])
            Package_List.append(Package)
        
        return Package_List 
    
    Summary_Switch = False
    Little_Summary_Switch = False

    for Page_Text in Page_Text_List:
        
        Application_Constitution = ["공고일자","등록번호","등록일자","국제특허분류","CPC특허분류","출원번호","출원일자","공개번호","공개일자","선행기술조사문헌","청구항의수","특허권자","발명자","대리인","심사관","발명의명칭","요약"]
        Certificate_Constitution = ["명세서","청구범위","발명의설명","기술분야","배경기술","선행기술문헌","특허문헌","비특허문헌","발명의내용","해결하려는과제","과제의해결수단","발명의효과","도면의간단한설명","발명을실시하기위한구체적인내용","부호의설명"]
        Search_List = ["(19)","(12)","(45)","(11)","(24)","(51)","(52)","(21)","(22)","(65)","(43)","(56)","전체청구항수", "(73)", "(72)", "(74)", "심사관", "(54)", "(57)"]        
        Little_Search_List = ["(51)","(52)","(56)","(72)","(73)","(74)"]
        for List in Little_Search_List:
            if List in Page_Text:
                Little_Summary_Switch = True
                break 
            
   
        if "(57)" in Page_Text:
            
            if "대 표 도" in Page_Text:
                Search_List.append("대표도")
            Page_Line_List = Page_Text.split("\n") 
            Package_List = ADD_From_To(Search_List,Page_Line_List)
            
            certificate["공고일자"] = Package_List[2][1].replace(Search_List[2],"").replace("공고일자","")
            certificate["등록번호"] = Package_List[3][1].replace(Search_List[3],"").replace("등록번호","")
            certificate["등록일자"] = Package_List[4][1].replace(Search_List[4],"").replace("등록일자","")
            certificate["국제특허분류"] = Package_List[5][1].replace(Search_List[5],"").replace("국제특허분류","")
            certificate["CPC특허분류"] = Package_List[6][1].replace(Search_List[6],"").replace("CPC특허분류","")
            certificate["출원번호"] = Package_List[7][1].replace(Search_List[7],"").replace("출원번호","")
            certificate["출원일자"] = Package_List[8][1].replace(Search_List[8],"").replace("출원일자","")
            certificate["공개번호"] = Package_List[9][1].replace(Search_List[9],"").replace("공개번호","")
            certificate["공개일자"] = Package_List[10][1].replace(Search_List[10],"").replace("공개일자","")
            certificate["선행기술조사문헌"] = Package_List[11][1].replace(Search_List[11],"").replace("선행기술조사문헌","")
            certificate["청구항의수"] = Package_List[12][1].replace(Search_List[12],"").replace("청구항의 수","")
            certificate["특허권자"] = Package_List[13][1].replace(Search_List[13],"").replace("특허권자","")
            certificate["발명자"] = Package_List[14][1].replace(Search_List[14],"").replace("발명자","")
            certificate["대리인"] = Package_List[15][1].replace(Search_List[15],"").replace("대리인","")
            certificate["심사관"] = Package_List[16][1].replace(Search_List[16],"").replace("심사관","")
            certificate["발명의명칭"] = Package_List[17][1].replace(Search_List[17],"").replace("발명의 명칭","")
            certificate["요약서"] = Package_List[18][1].replace(Search_List[18],"").replace("요 약","")
            
            page_numbering = "- " + str(Page_Text_List.index(Page_Text)+1) + " -"
            while page_numbering in certificate["요약서"]:
                 certificate["요약서"] = certificate["요약서"].replace(page_numbering,"")
                 
            point1 = certificate["요약서"].rfind("(")
            point2 = certificate["요약서"].rfind("뒷면에 계속")            
            point3 = certificate["요약서"].rfind(")")
            if point1 +1 ==  point2 and point2 +6 == point3:
                Summary_Switch = True 
                Little_Summary_Switch = False
                certificate["요약서"] = certificate["요약서"][:point1] 

        elif Summary_Switch and Little_Summary_Switch:
            
            Search_List_Address = Little_Search_List[:]
            Search_List_Name = Little_Search_List[:]
            for numbering in Little_Search_List:
                if not numbering in Page_Text:
                    Little_Search_List.insert(Little_Search_List.index(numbering),None)
                    Little_Search_List.remove(numbering)

            while None in Little_Search_List:
                Little_Search_List.remove(None)
                
            Page_Line_List = Page_Text.split("\n") 
            Package_List = ADD_From_To(Little_Search_List,Page_Line_List)
            
            for List in Search_List_Address:
                The_Number = Search_List_Address.index(List)
                for Package in Package_List:
                    if List == Package[0]:
                        Search_List_Address[Search_List_Address.index(List)] = Package_List.index(Package)
                if not type(Search_List_Address[The_Number]) == int :
                    Search_List_Address[Search_List_Address.index(List)] = "Nope"
            
            if not Search_List_Address[0] == "Nope":
                certificate["국제특허분류"] = Package_List[Search_List_Address[0]][1].replace(Search_List_Name[0],"").replace("국제특허분류","")          
            if not Search_List_Address[1] == "Nope":
                certificate["CPC특허분류"] = Package_List[Search_List_Address[1]][1].replace(Search_List_Name[1],"").replace("CPC특허분류","")
            if not Search_List_Address[2] == "Nope":
                certificate["선행기술조사문헌"] = Package_List[Search_List_Address[2]][1].replace(Search_List_Name[2],"").replace("선행기술조사문헌","")
            if not Search_List_Address[3] == "Nope":
                certificate["발명자"] = Package_List[Search_List_Address[3]][1].replace(Search_List_Name[3],"").replace("발명자","")
            if not Search_List_Address[4] == "Nope":
                certificate["특허권자"] = Package_List[Search_List_Address[4]][1].replace(Search_List_Name[4],"").replace("특허권자","")
            if not Search_List_Address[5] == "Nope":
                certificate["대리인"] = Package_List[Search_List_Address[5]][1].replace(Search_List_Name[5],"").replace("대리인","")
            Summary_Switch = False
            Little_Summary_Switch = False 
            
            
            page_numbering = "- " + str(Page_Text_List.index(Page_Text)+1) + " -"
            while page_numbering in certificate["요약서"]:
                 certificate["요약서"] = certificate["요약서"].replace(page_numbering,"")
            certificate["요약서"] += "".join(Page_Line_List[1:Package_List[0][2]])

        elif Summary_Switch and not Little_Summary_Switch:
            
            page_numbering = "- " + str(Page_Text_List.index(Page_Text)+1) + " -"
            while page_numbering in certificate["요약서"]:
                 certificate["요약서"] = certificate["요약서"].replace(page_numbering,"")
            
            certificate["요약서"] += Page_Text.replace("등록특허 "+certificate["등록번호"].strip())
            point1 = certificate["요약서"].rfind("(")
            point2 = certificate["요약서"].rfind("뒷면에 계속")            
            point3 = certificate["요약서"].rfind(")")
            if point1 +1 ==  point2 and point2 +6 == point3:
                Summary_Switch = False
                certificate["요약서"] = certificate["요약서"][:point1] 
        
        elif "청구항" in Page_Text:

            page_numbering = "- " + str(Page_Text_List.index(Page_Text)+1) + " -"                 
            Page_Text = Page_Text.replace("청구범위","").replace("명 세 서","").replace("등록특허 "+certificate["등록번호"].strip(),"").replace(page_numbering,"")

            Claim_List = []
            Claim_Number_List = []
            Page_Line_List = Page_Text.split("\n") 
            Description_Line_List = []
            
            # 발명의 설명 이하의 내용은 청구범위 텍스트에서 삭제한다.
            if "발명의 설명" in Page_Text:
                for Line in Page_Line_List:
                    if "발명의 설명" in Line:
                        Description_Line_List = Page_Line_List[Page_Line_List.index(Line):]
                        Page_Line_List = Page_Line_List[:Page_Line_List.index(Line)]
                        break
                    # 혹시 '발명의 설명' 문장이 다른데 붙어있을까봐 
                    elif "기 술 분 야" in Line :
                        Description_Line_List = Page_Line_List[Page_Line_List.index(Line):]                        
                        Page_Line_List = Page_Line_List[:Page_Line_List.index(Line)]
            
            for List in Page_Line_List:
                if List.replace(" ","")[:3] == "청구항":
                    Claim_List.append(List.replace(" ",""))
                    Claim_Number_List.append(Page_Line_List.index(List))
                    Page_Line_List[Page_Line_List.index(List)] = Page_Line_List[Page_Line_List.index(List)].replace(" ","")
            
            # 청구항이 첨부되었지만 최초의 페이지가 아님 
            if certificate["청구범위"]:
                Claim_Dict = certificate["청구범위"].pop()
                Claim,Content = Claim_Dict.popitem() 
                Content += "".join(Page_Line_List[:Claim_Number_List[0]])
                Claim_Dict[Claim] = Content
                certificate["청구범위"].append(Claim_Dict)
                
                Package_List = ADD_From_To(Claim_List,Page_Line_List)
                for Package in Package_List:
                    Claim_Dict = {}
                    Claim_Dict[Package[0]] = Package[1].replace(Package[0],"")
                    certificate["청구범위"].append(Claim_Dict)  
                
            # 청구항이 첨부되었고 최초의 페이지 
            else :
                Package_List = ADD_From_To(Claim_List,Page_Line_List)
                
                for Package in Package_List:
                    Claim_Dict = {}
                    Claim_Dict[Package[0]] = Package[1].replace(Package[0],"")
                    certificate["청구범위"].append(Claim_Dict)
            
            # 발명의 설명과 청구범위의 페이지가 겹쳤을 때 
            if Description_Line_List:
                
                #타이틀과 타이틀 순번을 기재할 리스트를 준비 
                Main_Title_List = [] 
                Main_Title_Line_List = []   
                #Certificate_Constitution : 기술분야=[3],배경기술=[4],특허문헌=[6],비특허문헌=[7],해결하려는과제=[9],과제의해결수단=[10],발명의효과=[11]
                Title_Written_Number_List = [3,4,6,7,9,10,11]
                for List in Description_Line_List:
                    for number in Title_Written_Number_List:
                        if Certificate_Constitution[number] == List.replace(" ",""):
                            Main_Title_List.append(Certificate_Constitution[number])
                            Main_Title_Line_List.append(Description_Line_List.index(List))
         
                # Title 하나에 Allocated_Description_Line_List 하나가 특정                
                for i in range(len(Main_Title_Line_List)):
                    if i == len(Main_Title_Line_List)-1: #마지막 타이틀
                        Allocated_Description_Line_List = Description_Line_List[Main_Title_Line_List[i]+1:]
                    else :
                        Allocated_Description_Line_List = Description_Line_List[Main_Title_Line_List[i]+1:Main_Title_Line_List[i+1]]
                    

                    # 하나의 타이틀에는 여러 개의 헤드 넘버가 가능 
                    Head_Number_List = []
                    for List in Allocated_Description_Line_List:

                        if len(List) < 2:
                            continue
                        if "[" == List.replace(" ","")[0] and "]" == List.replace(" ","")[-1]:
                            Head_Number_List.append(List.replace(" ",""))   

                        
                    Package_List = ADD_From_To(Head_Number_List,Allocated_Description_Line_List) # (헤드넘버,하위 콘텐츠,줄 번호)의 list
                    for Head_Name,Contents,Head_OrderinLine  in Package_List:
                        Description_Dict = {}
                        Description_Dict[Head_Name]=Contents.replace(Head_Name,"")
                        certificate[Main_Title_List[i]].append(Description_Dict)

                # 연속성을 주기 위해 마지막 원소는 남긴다. 
                Last_Title_List = Main_Title_List[-1]
                Last_Head_check = Head_Number_List[-1] 
                            

        else:

            #타이틀과 타이틀 순번을 기재할 리스트를 준비 
            Main_Title_List = [] 
            Main_Title_Line_List = []             
            #발명의 설명 ~ 도면까지 
            page_numbering = "- " + str(Page_Text_List.index(Page_Text)+1) + " -"                 
            Page_Text = Page_Text.replace("발명의 내용","").replace("선행기술문헌","").replace("등록특허 "+certificate["등록번호"].strip(),"").replace(page_numbering,"")
            Page_Line_List = Page_Text.split("\n") 
            
            if "도면1" in Page_Text:
                for line in Page_Line_List:
                    if "도면" in line:
                        Page_Line_List = Page_Line_List[:Page_Line_List.index(line)]
                        break
            #마지막 타이틀 예 : 배경기술 / 마지막 헤드 예 : [0005]를 이전 페이지에서 물려받았다. 페이지 앞줄에 매단다.  
            Page_Line_List.insert(0,Last_Head_check)
            Page_Line_List.insert(0,Last_Title_List)
            

            #Certificate_Constitution : 기술분야=[3],배경기술=[4],선행기술문헌=[5],특허문헌=[6],비특허문헌=[7]
            #발명의내용=[8],해결하려는과제=[9],과제의해결수단=[10],발명의효과=[11]
            #도면의간단한설명=[12],발명을실시하기위한구체적인내용=[13],부호의설명=[14]
            Title_Written_Number_List = list(range(3,15))
            for List in Page_Line_List:
                for number in Title_Written_Number_List:
                    if Certificate_Constitution[number] == List.replace(" ",""):
                        Main_Title_List.append(Certificate_Constitution[number])
                        Main_Title_Line_List.append(Page_Line_List.index(List))
            
            
            # Add from to 함수에 변형을 준 모습 
            for i in range(len(Main_Title_Line_List)):
                if i == len(Main_Title_Line_List)-1: #마지막 타이틀
                    Allocated_Description_Line_List = Page_Line_List[Main_Title_Line_List[i]+1:]
                else :
                    Allocated_Description_Line_List = Page_Line_List[Main_Title_Line_List[i]+1:Main_Title_Line_List[i+1]]
   
                Head_Number_List = []
                for List in Allocated_Description_Line_List:
                    if len(List) < 2:
                        continue
                    if "[" == List.replace(" ","")[0] and "]" == List.replace(" ","")[-1]:
                        Head_Number_List.append(List.replace(" ",""))
                        
                Package_List = ADD_From_To(Head_Number_List,Allocated_Description_Line_List) # (헤드넘버,하위 콘텐츠,줄 번호)의 list
                
                for Head_Name,Contents,Head_OrderinLine  in Package_List:
                    Description_Dict = {}
                    Description_Dict[Head_Name]=Contents.replace(Head_Name,"")
                    if Main_Title_List[i] == Certificate_Constitution[6] or Main_Title_List[i] == Certificate_Constitution[7] :
                        certificate[Certificate_Constitution[5]].append(Description_Dict)
                    else:
                        certificate[Main_Title_List[i]].append(Description_Dict)

            #마지막 타이틀을 다시 물려준다 예: 과제의해결수단 / 마지막 헤드 예 : [0014]를 이전 페이지에서 물려받았다.  
            Last_Title_List = Main_Title_List[-1]
            Last_Head_check = Head_Number_List[-1]            
    
    for key in certificate:
        while "  " in certificate[key]:
            certificate[key] = certificate[key].replace("  "," ")
    
    # Dictionary Key, 즉 청구항 번호가 같으면 글을 합친다. 
    Total_Dict = {}
    for Claim_Dict in certificate["청구범위"]:
        for Claim_Dict2 in [dic for dic in certificate["청구범위"] if not dic == Claim_Dict]:
            if Claim_Dict.keys() == Claim_Dict2.keys():
                Key,Value = Claim_Dict2.popitem()
                certificate["청구범위"].remove(Claim_Dict2)
                Claim_Dict[Key] += Value
        Total_Dict.update(Claim_Dict)
    certificate["청구범위"] = Total_Dict
    
    
    Title_Written_Number_List = [3,4,5,11,10,12]
    for number in Title_Written_Number_List:
        Title = Certificate_Constitution[number]
        Total_Dict = {}
        if Title in certificate.keys() and type(certificate[Title]) == list and type(certificate[Title][0]) ==dict:
            for dic in certificate[Title]:
                for dic2 in [dic2 for dic2 in certificate[Title] if not dic2 == dic]:
                    if dic.keys() == dic2.keys():
                        Key,Value = dic2.popitem()
                        certificate[Title].remove(dic2)
                        dic[Key] += Value
                Total_Dict.update(dic)
        certificate[Title] = Total_Dict                        
        
    return certificate        
        
certificate = Extraction(Page_Text_List)
































