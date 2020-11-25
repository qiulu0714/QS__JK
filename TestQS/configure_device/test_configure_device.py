import allure
import pytest
from Common import Request, Assert, read_excel,Tools
import pymysql


request = Request.Request()
assertions = Assert.Assertions()

url1 = 'http://guanjia.20783378.com'
url2 = 'http://zhongtai.20783378.com'
head = {}
# id_1 = 0
# id_2 = 0
# id_3 = 0
# id_4 = 0
# id_5 = 0
# id_6 = 0
# id_7 = 0
# id_8 = 0
# id_9 = 0
# id_10 = 0
# id_11 = 0
# id_12 = 0
# id_13 = 0
deviceid = 0
maccode = '4'
title = '千声机器'
sequence = '13124'
batchNumber = '2020-11'
# classid = 0
@allure.feature("获取登录用户信息")
class Test_info:

    @allure.severity("critical")
    @allure.story("用户登录")
    def test_login(self):
        login_resp = request.post_request(url=url1 + '/api/user/public/pwd/login',
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




    # @allure.severity("critical")
    # @allure.story("获取省ID")
    # def test_province(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute = cursor.execute("SELECT * FROM `sys_region` WHERE name = '上海市'")
    #
    #     # 将省ID赋予全局变量
    #     global id_1
    #     id_1 = cursor.fetchone()[0]
    #     print(id_1)
    #     return id_1
    #
    # @allure.severity("critical")
    # @allure.story("获取市ID")
    # def test_city(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute = cursor.execute("SELECT * FROM `sys_region` WHERE parent_id = 'id_1'")
    #
    #     # 将市ID赋予全局变量
    #     global id_2
    #     id_2 = cursor.fetchone()[0]
    #     print(id_2)
    #
    # @allure.severity("critical")
    # @allure.story("获取区ID")
    # def test_district(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute = cursor.execute("SELECT * FROM `sys_region` WHERE parent_id = 'id_2' and name = '浦东新区'")
    #
    #     # 将区ID赋予全局变量
    #     global id_3
    #     id_3 = cursor.fetchone()[0]
    #
    # @allure.severity("critical")
    # @allure.story("获取镇ID")
    # def test_town(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute = cursor.execute("SELECT * FROM `sys_region` WHERE parent_id = 1134 and name = '周浦镇'")
    #
    #     # 将镇ID赋予全局变量
    #     global id_4
    #     id_4 = cursor.fetchone()[0]
    #
    #
    # @allure.severity("critical")
    # @allure.story("获取中心ID")
    # def test_centre(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute = cursor.execute("SELECT * FROM `sys_region_center` WHERE town_id = 13787 and deleted = 0 ")
    #
    #     # 将中心ID赋予全局变量
    #     global id_5
    #     id_5 = cursor.fetchone()[0]
    #
    #
    # @allure.severity("critical")
    # @allure.story("获取居委ID")
    # def test_committee(self):
    #         db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #         cursor = db.cursor()
    #
    #         cursor_execute = cursor.execute("SELECT * FROM `sys_region_committee` WHERE name LIKE '%中金海棠%'")
    #
    #         # 将居委ID赋予全局变量
    #         global id_6
    #         id_6 = cursor.fetchone()[0]
    #
    # @allure.severity("critical")
    # @allure.story("获取公司ID")
    # def test_ente(self):
    #         db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #         cursor = db.cursor()
    #
    #         cursor_execute = cursor.execute("SELECT * FROM `sys_ente` WHERE title = '上海千声网络科技有限公司'")
    #
    #         # 将公司ID赋予全局变量
    #         global id_7
    #         id_7 = cursor.fetchone()[0]
    #
    # @allure.severity("critical")
    # @allure.story("获取部门ID")
    # def test_dept(self):
    #         db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #         cursor = db.cursor()
    #
    #         cursor_execute = cursor.execute("SELECT * FROM  sys_dept WHERE ente_id = 32 and title = '巡检一组'")
    #
    #         # 将部门ID赋予全局变量
    #         global id_8
    #         id_8 = cursor.fetchone()[0]
    #
    # @allure.severity("critical")
    # @allure.story("获取人员ID")
    # def test_dept(self):
    #         db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #         cursor = db.cursor()
    #
    #         cursor_execute = cursor.execute("SELECT * FROM `sys_user` WHERE ente_id = 32 AND dept_id = 98 AND realname = '邱露'")
    #
    #         # 将人员ID赋予全局变量
    #         global id_9
    #         id_9 = cursor.fetchone()[0]

    # @allure.severity("critical")
    # @allure.story("添加设备")
    # def test_add_device(self):
    #     add_device_resp = request.post_request(url=url1 + '/api/device/console/device/info/add',
    #                                       json ={"enteId":32,"deptId":98,"address":"沈杜公路1000弄",
    #                                              "appVersion":"3.0","batchCode":"2020-11","provinceId":9,
    #                                              "cityId":104,"countyId":1134,"townId":13787,
    #                                              "centerId":1000022,"communityId":3000007,
    #                                              "deviceVersion":"1.0","emergencyContactUserId":351,
    #                                              "gasNumber":"123456","lat":39.910925,"lon":116.413384,
    #                                              "macCode":maccode,"netType":"1,2,3","remark":"","romVersion":"1",
    #                                              "title":title,"phone":"17323926305","time":"2020-11-23 00:00:00",
    #                                              "villageName":"中金海棠湾居委会"},headers=head)
    #
    #     assertions.assert_code(add_device_resp.status_code,200)
    #
    #     add_device_resp_json = add_device_resp.json()
    #
    #     assertions.assert_in_text(add_device_resp_json['resMsg'],'success')
    #
    # @allure.severity("critical")
    # @allure.story("获取设备ID")
    # def test_centre(self):
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     cursor = db.cursor()
    #
    #     cursor_execute_1 = cursor.execute("SELECT id ,title  FROM `device_info` WHERE mac_code = '4' AND deleted = 0 ")
    #
    #     aa = cursor.fetchone()
    #     print(aa)
    #     # 将设备ID赋予全局变量
    #     global deviceid
    #     deviceid = aa[0]
    #     print(deviceid)
    #
    # @allure.severity("critical")
    # @allure.story('配置设备功能模板')
    # def test_add_template(self):
    #     add_template_resp = request.post_request(url= url1 + '/api/config/console/cms/relation/region/device/template/add',
    #                         json = {"deviceInfos":[{"deviceId":deviceid,"subRegionId":3000007,"deviceName":title}],"templateId":19},
    #                         headers= head)
    #
    #     assertions.assert_code(add_template_resp.status_code,200)
    #
    #     add_template_resp_json = add_template_resp.json()
    #
    #     assertions.assert_in_text(add_template_resp_json['resMsg'],'success')


    # @allure.severity('critical')
    # @allure.story('配置售货机')
    # def test_add_VendingMachine(self):
    #
    #     # 获取classId
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #     cursor = db.cursor()
    #
    #     # 根据shop_vending_machine_class表中title字段查询classid
    #     cursor_execute = cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title in ('新模板1','新模板2')")
    #     bb = cursor.fetchall()
    #
    #     for i in range(2):
    #
    #         classid = bb[i][0]
    #         # print(classid)
    #
    #         add_vending_machine_resp = request.post_request(
    #             url=url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
    #             json={"region": 13787, "sequence": sequence, "address": "沈杜公路1000弄", "title": title,
    #               "macAddress": maccode,"deviceId": deviceid, "saleType": 1, "classId": classid,
    #               "batchNumber": batchNumber,"runStatus": 1, "remarks": "", "deviceTitle": title},
    #             headers= head)
    #
    #         assertions.assert_code(add_vending_machine_resp.status_code,200)
    #
    #         add_vending_machine_resp_json = add_vending_machine_resp.json()
    #
    #         assertions.assert_in_text(add_vending_machine_resp_json['resMsg'],"success")
    #
    @allure.severity('critical')
    @allure.story('售货机绑定模板')
    def test_add_VendingMachineTemplate(self):


        add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
                             json= {"machineIds":["295412425602109440"],"templateId":295412645756932096},
                             headers= head)

        assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)

        add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()

        print(add_VendingMachineTemplate_resp_json)

        assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")

