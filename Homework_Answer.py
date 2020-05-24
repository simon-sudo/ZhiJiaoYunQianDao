import requests
import re
import json

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list
from Rinse_Answer import Rinse


def main(stuid):
    info = get_all_course(stuid)
    homrwork_list = get_homework_list(stuid, info['openClassId'], info['courseOpenId'])
    homeworkId = homrwork_list['homeworkId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
    data = {
        'homeWorkId': homeworkId
    }
    #html = requests.post(url=url, data=data).json()['data']
    html = requests.post(url=url, data=data).text
    html = html.replace('&nbsp;', '')
    html = re.sub('<.*?>', "", html)
    Rinse(json.loads(html)['data'])


if __name__ == '__main__':
    main('')
