import allure
import pytest
from Common import Request, Assert, read_excel,Tools
import pymysql


request = Request.Request()
assertions = Assert.Assertions()


url = 'http://zhongtai.20783378.com'
head = {}
id = 0
code = {}

@allure.feature("获取登录用户信息")
class Test_info():

    @allure.severity("critical")
    @allure.story("登录接口")
    def test_login(self):
        login_resp = request.post_request(url=url + '/api/user/public/pwd/login',
                                          json={"subject": "13800010001", "password": "123456"})

        assertions.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()
        # 打印响应json
        # print(login_resp_json)
        assertions.assert_in_text(login_resp_json['resMsg'], 'success')

        # 提取token
        data_json = login_resp_json['data']

        # # 重新赋值全局变量 head
        global head
        head = {'console-token': data_json['consoleToken']}
        # print(head)

    @allure.severity("critical")
    @allure.story("查询排班部门")
    def test_Schedule(self):
        Schedule_resp = request.post_request(url=url + "/api/user/console/sys/allowSchedule/dept",
                                             json={"pageNum": 1, "pageSize": 10, "page": 1},
                                             headers=head)
        # print( Schedule_resp)
        # 通过响应状态码做断言
        assertions.assert_code(Schedule_resp.status_code,200)

        schedule_resp_json = Schedule_resp.json()
        # 通过响应文本做断言
        assertions.assert_in_text(schedule_resp_json["resMsg"] ,"success")

        print(code)

    @allure.severity("critical")
    @allure.story("阿里巴巴巡检部门排班")
    def test_ali(self):
        ali_resp = request.post_request(url = url + '/api/schedule/console/scheduling/organization/period/page',
                                        json={"deptName": "巡检部门", "entName": "阿里巴巴分公司", "entId": "27", "deptId": "89", "page": 1, "size": 10},
                                        headers = head )
        assertions.assert_code(ali_resp.status_code,200)
        ali_resp_json = ali_resp.json()

        print(ali_resp_json)
        assertions.assert_in_text(ali_resp_json["resMsg"],"success")

        res_code = ali_resp_json['resCode']

        print(res_code)

        global code
        code = {"ad" : res_code}

        # print(code)

    @allure.severity("critical")
    @allure.story("连接数据库")
    def test_sjk(self):
        db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")

        cursor = db.cursor()

        cursor_execute = cursor.execute("SELECT * FROM ad where id = 1562901")

        cursor_fetchone = cursor.fetchone()[0]

        print(cursor_fetchone)






