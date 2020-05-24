import requests

from Get_All_Course import get_all_course
from Get_Homework_Grade import get_homework_grade
from Get_Homework_List import get_homework_list


def main(stuId):
    allcourse = get_all_course(stuId)
    openClassId = allcourse['openClassId']
    courseOpenId = allcourse['courseOpenId']
    homeworklist = get_homework_list(stuId, openClassId, courseOpenId)
    if homeworklist == 0:
        print("获取失败")
    else:
        homeworkTermTimeId = homeworklist['homeworkTermTimeId']
        homeworkId = homeworklist['homeworkId']
        grades = get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId)
        if grades != 0:
            index = 1
            for i in grades:
                print(f"【{index}】时间：{i['dateCreated']}\t分数{i['getScore']}")
                index += 1
            target = int(input("请输入要修改的序号：")) - 1
            homeworkStuId = grades[target]['homeworkStuId']
        else:
            input("回车键后退出")
    teaId = input("请输入教师ID")
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/rejectHomework'
    data = {
        'homeworkStuId': homeworkStuId,
        'teaId': teaId,
    }
    result = requests.post(url=url, data=data).json()
    print(result['msg'])
    sele = input("【1】返回首页\n【2】返回上级\n请选择：")
    if sele == 2:
        main(stuId)
    else:
        from Main import main as menu
        menu()
