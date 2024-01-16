import pandas as pd
import re
from collections import Counter
 
# task 2:
def task2(data):
    lstValid = []
    lstData = data.split('\n')
    #2.1. Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.
    print("Total number of lines in the text file are: ",len(lstData))
    print("*** ANALYZING ***")
    #2.2. Báo cáo tổng số dòng dữ liệu không hợp lệ trong tệp.
    #2.3. Nếu một dòng dữ liệu không hợp lệ, bạn nên báo cáo cho người dùng bằng cách in ra một thông báo lỗi.
    lineValid = 0
    lineInvalid = 0
    for i in range(0,len(lstData)):
        studentID = re.findall('([a-zA-Z0-9][a-zA-Z0-9]+)', lstData[i])[0]     # tìm mã sinh viên bằng regex  
        lenStudentID = len(studentID)
        # kiểm tra dữ liệu valid
        if lenStudentID == 9 and len(lstData[i].split(',')) == 26:
            lineValid +=1
            lstValid.append(lstData[i])
        elif lenStudentID != 9:
            lineInvalid +=1
            print('Invalid line of data: N# is invalid')
            print(lstData[i])
        elif len(lstData[i].split(',')) != 26: 
            lineInvalid +=1
            print('Invalid line of data: does not contain exactly 26 values:')
            print(lstData[i])
    print('**** REPORT ****')
    print('Total valid lines of data: ', lineValid)
    print('Total invalid lines of data: ', lineInvalid)
    return lstValid

# task 3:
def task3(data):
    point = 0 
    studentHightScore = 0
    lstSkipQuestion = []
    lstScoreResult = []
    lstScore = []
    lstWrongQuestion = []
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    lstAnswer_key = (answer_key.split(","))
    
    count_row = df.shape[0] #số dòng
    count_col = df.shape[1] #số cột

    for i in range(0,count_row):
        for j in range(1, count_col):
            stdent_answer = data.iloc[i,j] 
            if (stdent_answer == lstAnswer_key[j-1]) and (stdent_answer != ""):
                point = point + 4
            elif stdent_answer != lstAnswer_key[j-1] and (stdent_answer != ""):
                point = point - 1
                lstWrongQuestion.append(j)
            else:
                lstSkipQuestion.append(j)
        if point > 80: #3.1. Đếm số lượng học sinh đạt điểm cao (>80).
            studentHightScore +=1  

        lstScoreResult.append(point)
        lstScore.append(point)
        point = 0

    maxScore = max(lstScore) #3.3. Điểm cao nhất.
    minScore = min(lstScore) #3.4. Điểm thấp nhất.
    meanScore = sum(lstScore)/len(lstScore) #3.2. Điểm trung bình.
    print("Total student of high scores: ", studentHightScore)
    print("Mean (average) score: ", round(meanScore,3))
    print("Highest score:", maxScore)
    print("Lowest score:", minScore )
    print("Range of scores:", maxScore - minScore ) #3.5. Miền giá trị của điểm (cao nhất trừ thấp nhất).

    # 3.6. Giá trị trung vị
    lstScore.sort()
    lenght = len(lstScore)
    if (lenght % 2 != 0):
        print("Medium score:", lstScore[lenght // 2])
    else:
        print("Medium score:", (lstScore[lenght // 2] + lstScore[lenght // 2 - 1]) // 2)

    # 3.7: Tìm các câu hỏi bị bỏ qua nhiều nhất
    skip_answer = []
    lst_skip_answer = [x + 1 for x in lstSkipQuestion]
    counter_lst_skip_answer = Counter(lst_skip_answer)
    most_skip_elements = counter_lst_skip_answer.most_common() # Trả về 1 list ('các câu hỏi bị bỏ qua', 'số lần bỏ qua').
    skip_maxCount = most_skip_elements[0][1]
    len_skip = int(len(most_skip_elements))

    # Tính tỉ lệ bị bỏ qua
    rate_skip_answer = round((skip_maxCount/len(data)),2)

    for s in range(0,len_skip):
        # Sử dụng lệnh if: nếu số câu hỏi bị bỏ qua bằng số câu hỏi bị bỏ qua nhiều nhất thì thêm nó và list skip_answer = []
        if (most_skip_elements[s][1]) == skip_maxCount:
            skip_answer.append(most_skip_elements[s])
            skip_answer[s] = skip_answer[s] + (rate_skip_answer,)
    print("Question that most people skip:",skip_answer)
    
    # 3.8: Tìm các câu hỏi bị sai nhiều nhất
    wr_answer = []
    lst_wr_answer = [x + 1 for x in lstWrongQuestion]
    counter_lst_wr_answer = Counter(lst_wr_answer)
    most_wr_elements = counter_lst_wr_answer.most_common() # Hàm trả về 1 list ('các câu hỏi bị sai', 'số lần sai').
    wr_maxCount = most_wr_elements[0][1]    
    len_wr = int(len(most_wr_elements))
    # Tính tỉ lệ bị sai
    rate_wr_answer = round((wr_maxCount/len(data)),2)

    for s in range(0,len_wr):
        # Sử dụng lệnh if: nếu số câu hỏi sai bằng số câu hỏi sai nhiều nhất thì thêm nó và list wr_answer = []
        if (most_wr_elements[s][1]) == wr_maxCount:
            wr_answer.append(most_wr_elements[s])
            wr_answer[s] = wr_answer[s] + (rate_wr_answer,)
    print("Question that most people answer incorrectly:",wr_answer)

    return lstScoreResult

# task 4:
def task4(data,lst_Score):
    with open(file_out, "w") as f_out:
        count_row = df.shape[0] #số dòng
        count_col = df.shape[1] #số cột
        for i in range(0,count_row):
            lstStudentID = data.iloc[i,0]
            f_out.write("{}, {}\n".format((lstStudentID), lst_Score[i])) 
y = True
while y :
    # task 1:
    try:
        fileName = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        linkFile = 'Data Files/' + fileName + '.txt'
        with open(linkFile, 'r') as file:
            data = file.read()           
            print("Successfully opened " + fileName + '.txt')

        lstDataValid = task2(data)# task 2

        data_list = list() 
        for i in range(0,len(lstDataValid)):  
            data_line = lstDataValid[i].split(',')
            data_list.insert(i,data_line)
        
        # Task 5: tạo dataframe với pandas
        df = pd.DataFrame(data_list)              

        lst_Score = task3(df) #task 3

        file_out = fileName + '_grades.txt' 
        task4(df,lst_Score)

    except IOError:
        print("File cannot be found")
        y = True
