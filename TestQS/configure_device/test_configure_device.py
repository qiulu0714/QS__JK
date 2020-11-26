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
maccode = '212'
title = '千声机器201'
sequence = '13124'
batchNumber = '2020-11'
address = '沈杜公路1000号'
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
    #   db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #   cursor = db.cursor()
    #
    #   cursor_execute = cursor.execute("SELECT * FROM `sys_region` WHERE name = '上海市'")
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
    #
    @allure.severity("critical")
    @allure.story("添加设备")
    def test_add_device(self):
        add_device_resp = request.post_request(url=url1 + '/api/device/console/device/info/add',
                                          json ={"enteId":32,"deptId":98,"address":"沈杜公路1000弄",
                                                 "appVersion":"3.0","batchCode":"2020-11","provinceId":9,
                                                 "cityId":104,"countyId":1134,"townId":13787,
                                                 "centerId":1000022,"communityId":3000007,
                                                 "deviceVersion":"1.0","emergencyContactUserId":351,
                                                 "gasNumber":"123456","lat":39.910925,"lon":116.413384,
                                                 "macCode":maccode,"netType":"1,2,3","remark":"","romVersion":"1",
                                                 "title":title,"phone":"17323926305","time":"2020-11-23 00:00:00",
                                                 "villageName":"中金海棠湾居委会"},headers=head)

        assertions.assert_code(add_device_resp.status_code,200)

        add_device_resp_json = add_device_resp.json()

        assertions.assert_in_text(add_device_resp_json['resMsg'],'success')

        #将携带的参数传给params
        a = {"page" : 1 , "size" : 10 , "fuzzy" : title}

        query_device_info_resp = request.get_request(url=url1 +"/api/device/console/device/info/query/CombinationQuery",
                                                    params= a, headers=head)

        assertions.assert_code(query_device_info_resp.status_code,200)

        query_device_info_resp_json = query_device_info_resp.json()

        assertions.assert_in_text(query_device_info_resp_json['resMsg'],'success')

        query_device_info_resp_json_data = query_device_info_resp_json['data']

        query_device_info_resp_json_data_list = query_device_info_resp_json_data['list']

        list = query_device_info_resp_json_data_list[0]

        # 将设备ID赋予全局变量
        global deviceid
        deviceid = list['id']
        print(deviceid)

    @allure.severity("critical")
    @allure.story('配置设备功能模板')
    def test_add_template(self):
        add_template_resp = request.post_request(url= url1 + '/api/config/console/cms/relation/region/device/template/add',
                            json = {"deviceInfos":[{"deviceId":deviceid,"subRegionId":3000007,"deviceName":title}],"templateId":19},
                            headers= head)

        assertions.assert_code(add_template_resp.status_code,200)

        add_template_resp_json = add_template_resp.json()

        assertions.assert_in_text(add_template_resp_json['resMsg'],'success')


    @allure.severity('critical')
    @allure.story('添加售货机')
    def test_add_Vending_Machine(self):

        # 获取classId
        db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
        cursor = db.cursor()

        # 根据shop_vending_machine_class表中title字段查询classid
        cursor_execute = cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title in ('新类型1','新类型2')")
        bb = cursor.fetchall()

        for i in range(2):

            classid = bb[i][0]
            # print(classid)

            add_vending_machine_resp = request.post_request(
                url=url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
                json={"region": 13787, "sequence": sequence, "address": "沈杜公路1000弄", "title": title,
                  "macAddress": maccode,"deviceId": deviceid, "saleType": 1, "classId": classid,
                  "batchNumber": batchNumber,"runStatus": 1, "remarks": "", "deviceTitle": title},
                headers= head)

            assertions.assert_code(add_vending_machine_resp.status_code,200)

            add_vending_machine_resp_json = add_vending_machine_resp.json()

            assertions.assert_in_text(add_vending_machine_resp_json['resMsg'],"success")

        # 获取机器列表
        MachinePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
            json={"page":1,"size":10,"saleType":1,"title":title},
            headers=head)

        assertions.assert_code(MachinePage_resp.status_code, 200)
        # 提示响应json
        MachinePage_resp_json = MachinePage_resp.json()

        assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachinePage_respp_json_data = MachinePage_resp_json['data']
        # 获取响应中键list的值
        MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']

        # 获取模板列表
        MachineTemplatePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
            json={"title":"新模板","saleType":1},
            headers=head)

        assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
        # 提示响应json
        MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()

        assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
        # 获取响应中键list的值
        MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']

        for i in range(2):
            list1 = MachinePage_respp_json_data_list[i]
            # 获取json中id的值
            machineid = list1['id']

            # 将machineid 从str类型转换成list类型
            machineIds = machineid.split()

            # 获取json中classid的值
            Machine_class_id = list1['classId']

            for j in range(2):
                list2 = MachineTemplatePage_resp_json_data_list[j]

                # 获取json中id的值
                templateid = list2['id']

                # 获取json中classid的值
                template_class_id = list2['classId']

                # 将template_class_id与Machine_class_id进行判断是否能执行模板与设备的绑定关系
                if template_class_id != Machine_class_id :
                    print ('无法执行')
                else:

                    # 设备与模板进行绑定
                    add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
                             json= {"machineIds":machineIds,"templateId":templateid},
                             headers= head)

                    assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)

                    add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()

                    assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")

    @allure.severity('critical')
    @allure.story('应急物资设备配置')
    def test_add_emergency_supplies(self):
        # 获取classId
        db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
        cursor = db.cursor()
        # 根据shop_emergency_supplies_class表中title字段查询classid
        cursor_execute = cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title = '应急物资型号001'")
        bb = cursor.fetchone()

        classid = bb[0]
        # 添加应急物质设备
        add_emergency_supplies_resp = request.post_request(url= url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
                             json= {"region":13787,"sequence":sequence,"address":address,"title":title,
                                    "macAddress":maccode,"deviceId":deviceid,"saleType":2,"classId":classid,
                                    "batchNumber":batchNumber,"runStatus":1,"remarks":"","deviceTitle":title},
                             headers= head)

        assertions.assert_code(add_emergency_supplies_resp.status_code,200)

        add_emergency_supplies_resp_json = add_emergency_supplies_resp.json()

        assertions.assert_in_text(add_emergency_supplies_resp_json["resMsg"],'success')

        # 获取机器列表
        MachinePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
            json={"page":1,"size":10,"saleType":2,"title":title},
            headers=head)

        assertions.assert_code(MachinePage_resp.status_code, 200)
        # 提示响应json
        MachinePage_resp_json = MachinePage_resp.json()

        assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachinePage_respp_json_data = MachinePage_resp_json['data']
        # 获取响应中键list的值
        MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']

        #获取list中的json
        MachinePage_respp_json_data_list_json = MachinePage_respp_json_data_list[0]
        # 获取json中id的值
        machineid = MachinePage_respp_json_data_list_json['id']

        # 将machineid 从str类型转换成list类型
        machineIds = machineid.split()

        # 获取模板列表
        MachineTemplatePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
            json={"title":"应急物资模板001","saleType":2},
            headers=head)

        assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
        # 提示响应json
        MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()

        assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
        # 获取响应中键list的值
        MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']

        # 获取list中的json
        MachineTemplatePage_resp_json_data_list_json = MachineTemplatePage_resp_json_data_list[0]

        # 获取json中id的值
        templateid = MachineTemplatePage_resp_json_data_list_json['id']

        # 设备与模板进行绑定
        add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
                                 json= {"machineIds":machineIds,"templateId":templateid},
                                 headers= head)

        assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)

        add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()

        assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")

    @allure.severity('critical')
    @allure.story('储物柜设备配置')
    def test_add_locker(self):
        # 获取classId
        db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
        cursor = db.cursor()
        # 根据shop_vending_machine_class表中title字段查询classid
        cursor_execute = cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title = '测试型号'")
        bb = cursor.fetchone()

        classid = bb[0]

        # 添加应急物质设备
        add_locker_resp = request.post_request(url= url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
                             json= {"region":13787,"sequence":sequence,"address":address,"title":title,
                                    "macAddress":maccode,"deviceId":deviceid,"saleType":3,"classId":classid,
                                    "batchNumber":batchNumber,"runStatus":1,"remarks":"","deviceTitle":title},
                             headers= head)

        assertions.assert_code(add_locker_resp.status_code,200)

        add_locker_resp_json = add_locker_resp.json()

        assertions.assert_in_text(add_locker_resp_json["resMsg"],'success')

        # 获取机器列表
        MachinePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
            json={"page":1,"size":10,"saleType":3,"title":title},
            headers=head)

        assertions.assert_code(MachinePage_resp.status_code, 200)
        # 提示响应json
        MachinePage_resp_json = MachinePage_resp.json()

        assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachinePage_respp_json_data = MachinePage_resp_json['data']
        # 获取响应中键list的值
        MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']

        #获取list中的json
        MachinePage_respp_json_data_list_json = MachinePage_respp_json_data_list[0]
        # 获取json中id的值
        machineid = MachinePage_respp_json_data_list_json['id']

        # 将machineid 从str类型转换成list类型
        machineIds = machineid.split()

        # 获取模板列表
        MachineTemplatePage_resp = request.post_request(
            url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
            json={"title":"测试模板","saleType":3},
            headers=head)

        assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
        # 提示响应json
        MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()

        assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
        # 获取响应中键data的值
        MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
        # 获取响应中键list的值
        MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']

        # 获取list中的json
        MachineTemplatePage_resp_json_data_list_json = MachineTemplatePage_resp_json_data_list[0]

        # 获取json中id的值
        templateid = MachineTemplatePage_resp_json_data_list_json['id']

        # 设备与模板进行绑定
        add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
                                 json= {"machineIds":machineIds,"templateId":templateid},
                                 headers= head)

        assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)

        add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()

        assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")