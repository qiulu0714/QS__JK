import allure
import pytest
import pymysql.cursors
from Common import Request, Assert, read_excel

request = Request.Request()
assertions = Assert.Assertions()
head = {}
ids = 0
url = 'http://zhongtai.20783378.com'


@allure.feature("获取登录用户信息")
class Test_info():
     @allure.story("登录接口")
     def test_login(self):
        login_resp = request.post_request(url=url + '/api/user/public/pwd/login',
                                          json={"subject": "13800010001", "password": "123456"})

        assertions.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()
        # 打印响应json
        print(login_resp_json)
        assertions.assert_in_text(login_resp_json['resMsg'], 'success')

        # 提取token
        data_json = login_resp_json['data']

        # # 重新赋值全局变量 head
        global head
        head = {'console-token': data_json['consoleToken']}
        print(head)

@allure.feature("排班管理")
class Test_dept:

    @allure.story("查询排班部门")
    def test_Schedule(self):
        Schedule_resp = request.post_request(url=url + "/api/user/console/sys/allowSchedule/dept",
                                             json={"pageNum": 1, "pageSize": 10, "page": 1},
                                             headers=head)
        print( Schedule_resp)
        # 通过响应状态码做断言
        assertions.assert_code(Schedule_resp.status_code,200)

        schedule_resp_json = Schedule_resp.json()
        # 通过响应文本做断言
        assertions.assert_in_text(schedule_resp_json["resMsg"] ,"success")












# @allure.feature("产品管理模块")
# class Test_product:
#
#     @allure.story("新建产品")
#     def test_new(self):
#         rp_resp = request.post_request(url=url + '/consoleapi/console/app-pk',
#                                        json={"appInfoIds": [18], "appPkName": "ws测试产品", "appPkDesc": "测试",
#                                                "isVisible": 0, "isQualified": "true"},
#                                        headers=head)
#
#         assertions.assert_code(rp_resp.status_code, 200)
#         rp_resp_json = rp_resp.json()
#         assertions.assert_in_text(rp_resp_json['message'], 'Success')
#
#     @allure.story("查询产品")
#     def test_find(self):
#         rp_resp = request.get_request(url=url + '/consoleapi/console/app-pk',
#                                       params={'appPackageName': 'ws测试产品', 'pageSize': 6, 'pageNum': 1},
#                                       headers=head)
#         assertions.assert_code(rp_resp.status_code, 200)
#         rp_resp_json = rp_resp.json()
#         assertions.assert_in_text(rp_resp_json['message'], 'Success')
#         assertions.assert_in_text(rp_resp_json['data']['total'], 1)
#         print(rp_resp_json)
#
#     @allure.story("修改产品")
#     def test_change(self):
#         # 连接mysql数据库
#         connection = pymysql.connect(host='MYSQL', port=3306, user='root', password='Pass1234', db='ziyun-idm',
#                                      cursorclass=pymysql.cursors.DictCursor)
#         # 通过cursor创建游标,进行每一步操作
#         cursor = connection.cursor()
#         # 发起请求
#         sql = 'SELECT * FROM `app_package` where app_pk_name = "ws测试产品";'
#         cursor.execute(sql)
#         # 获取数据
#         res = cursor.fetchone()
#         print(res)
#         global ids
#         ids = str(res['id'])
#         cursor.close()
#         connection.close()
#         info_resp = request.put_request(url=url + '/consoleapi/console/app-pk',
#                                         json={"appPkId": ids, "appInfoIds": [18], "appPkName": "ws测试产品",
#                                                 "appPkDesc": "自动化测试", "isQualified": "true"},
#                                         headers=head)
#         assertions.assert_code(info_resp.status_code, 200)
#         info_resp_json = info_resp.json()
#         assertions.assert_in_text(info_resp_json['message'], 'Success')
#         assertions.assert_text(info_resp_json['data']['appPkDesc'], '自动化测试')
#         print(info_resp_json)
#
#     @allure.story("查询修改产品")
#     def test_find(self):
#         info_resp = request.get_request(url=url + '/consoleapi/console/app-pk',
#                                         params={'appPackageName': 'ws测试产品', 'pageSize': 6, 'pageNum': 1},
#                                         headers=head)
#         assertions.assert_code(info_resp.status_code, 200)
#         info_resp_json = info_resp.json()
#         assertions.assert_in_text(info_resp_json['message'], 'Success')
#         assertions.assert_text(info_resp_json['data']['list'][0]['appPkDesc'], "自动化测试")
#         print(info_resp_json)
#
#     @allure.story("删除产品")
#     def test_find(self):
#         # 连接mysql数据库
#         connection = pymysql.connect(host='MYSQL', port=3306, user='root', password='Pass1234', db='ziyun-idm',
#                                      cursorclass=pymysql.cursors.DictCursor)
#         # 通过cursor创建游标,进行每一步操作
#         cursor = connection.cursor()
#         # 发起请求
#         sql = 'SELECT * FROM `app_package` where app_pk_name = "ws测试产品";'
#         cursor.execute(sql)
#         # 获取数据
#         res = cursor.fetchone()
#         print(res)
#         global ids
#         ids = str(res['id'])
#         cursor.close()
#         connection.close()
#
#         info_resp = request.delete_request(url=url + '/consoleapi/console/app-pk/' + ids,
#                                            headers=head)
#         assertions.assert_code(info_resp.status_code, 200)
#         info_resp_json = info_resp.json()
#         assertions.assert_in_text(info_resp_json['message'], 'Success')
#         print(info_resp_json)
