import allure
import pytest
from Common import Request, Assert, read_excel,Tools
import pymysql

request = Request.Request()
assertions = Assert.Assertions()

# 后台管理地址
url1 = 'http://192.168.1.109/'
# 中台管理地址
url2 = 'http://192.168.1.109:81/zhongtai'

# 创建空的字典
head = {}

deviceid = 0
maccode = 'C0:84:7D:0E:9A:FE'
title = '宜浩佳园3号机'
sequence = '13124'
batchNumber = '2020-11'
address = '竹柏路111弄'
name = '高清摄像头'
code = 'GQSXT__001'

@allure.feature("配置设备")
class Test_info:

    @allure.severity("critical")
    @allure.story("用户登录")
    def test_login(self):
        login_resp = request.post_request(url=url1 + '/api/user/public/pwd/login',
                                          json={"subject": "13800010001", "password": "123456"})

        # 通过状态码进行判断
        assertions.assert_code(login_resp.status_code, 200)

        # 提取响应正文
        login_resp_json = login_resp.json()

        # 通过响应正文进行对比判断
        assertions.assert_in_text(login_resp_json['resMsg'], 'success')

        # 提取token
        data_json = login_resp_json['data']
        # # 重新赋值全局变量 head
        global head
        head = {'console-token': data_json['consoleToken']}

    @allure.severity("critical")
    @allure.story("添加设备")
    def test_add_device(self):
        # 获取种类id




        """ 新增类别 """
        add_class_resp = request.post_request(url=url1 + '/api/device/console/device/part/class/add',
                                               json={"brandName": "千声用品", "categoryId": 3, "code": code,
                                                     "manufacturerName": "千声生厂商","modalNumber": "XH__001",
                                                     "name":name, "providerName": "千声供应商","unit": "个",
                                                     "specification": "{}",
                                                     "img": "https://v3.cdn.qeesen.com/file/ea39476b088b4507ad4acb70983eaf9f.png"},
                                               headers=head)

        assertions.assert_code(add_class_resp.status_code,200)

        add_class_resp_json = add_class_resp.json()

        assertions.assert_in_text(add_class_resp_json ['resMsg'],'success')

        """新增编码"""
        add_part_resp = request.post_request(url=url1 + '/api/device/console/device/part/add',
                                               json={"classId":"3","code":code + "__001","count":"1"},
                                               headers=head)

        assertions.assert_code(add_part_resp.status_code,200)

        add_part_resp_json = add_part_resp.json()

        assertions.assert_in_text(add_part_resp_json['resMsg'],'success')



        # 将携带的参数传给params
        a = {"page" : 1 , "size" : 10 , "fuzzy" : title}

        query_device_info_resp = request.get_request(url=url1 +"/api/device/console/device/info/query/CombinationQuery",
                                                    params= a, headers=head)
        # 通过状态码进行判断
        assertions.assert_code(query_device_info_resp.status_code,200)

        # 提取响应正文
        query_device_info_resp_json = query_device_info_resp.json()

        # 通过响应正文进行对比判断
        assertions.assert_in_text(query_device_info_resp_json['resMsg'],'success')

        # 获取josn中data
        query_device_info_resp_json_data = query_device_info_resp_json['data']

        # 获取data中的list
        query_device_info_resp_json_data_list = query_device_info_resp_json_data['list']

        # 获取list中第一个josn
        list = query_device_info_resp_json_data_list[0]

        # 将deviceID赋予全局变量
        global deviceid
        deviceid = list['id']

    @allure.severity("critical")
    @allure.story('配置设备功能模板')
    def test_add_template(self):
        add_template_resp = request.post_request(url= url1 + '/api/config/console/cms/relation/region/device/template/add',
                            json = {"deviceInfos":[{"deviceId":deviceid,"subRegionId":3000007,"deviceName":title}],"templateId":19},
                            headers= head)

        # 通过状态码进行判断
        assertions.assert_code(add_template_resp.status_code,200)

        # 提取响应正文
        add_template_resp_json = add_template_resp.json()

        # 通过响应正文进行对比判断
        assertions.assert_in_text(add_template_resp_json['resMsg'],'success')

    # @allure.severity('critical')
    # @allure.story('添加售货机')
    # def test_add_Vending_Machine(self):
    #
    #     # 连接数据库
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #
    #     # 使用cursor()方法获取数据库的操作游标
    #     cursor = db.cursor()
    #
    #     # 根据shop_vending_machine_class表中title字段查询classid
    #     cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title in ('新类型1','新类型2')")
    #
    #     # 返回多个元组
    #     bb = cursor.fetchall()
    #
    #     # 通过for循环多次添加售货机
    #     for i in range(2):
    #         # 获取元祖第一个元素即classid
    #         classid = bb[i][0]
    #         # 添加售货机
    #         add_vending_machine_resp = request.post_request(
    #             url=url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
    #             json={"region": 13787, "sequence": sequence, "address": "沈杜公路1000弄", "title": title,
    #             "macAddress": maccode,"deviceId": deviceid, "saleType": 1, "classId": classid,
    #             "batchNumber": batchNumber,"runStatus": 1, "remarks": "", "deviceTitle": title},
    #             headers= head)
    #
    #         # 通过状态码进行判断
    #         assertions.assert_code(add_vending_machine_resp.status_code,200)
    #
    #         # 提取响应正文
    #         add_vending_machine_resp_json = add_vending_machine_resp.json()
    #
    #         # 通过响应正文进行对比判断
    #         assertions.assert_in_text(add_vending_machine_resp_json['resMsg'],"success")
    #
    #     # 获取机器列表
    #     MachinePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
    #         json={"page":1,"size":10,"saleType":1,"title":title},
    #         headers=head)
    #
    #     # 通过状态码进行判断
    #     assertions.assert_code(MachinePage_resp.status_code, 200)
    #
    #     # 提取响应正文
    #     MachinePage_resp_json = MachinePage_resp.json()
    #
    #     # 通过响应正文进行对比判断
    #     assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
    #
    #     # 获取响应正文中data的值
    #     MachinePage_respp_json_data = MachinePage_resp_json['data']
    #
    #     # 获取data中list的值
    #     MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']
    #
    #     # 获取模板列表
    #     MachineTemplatePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
    #         json={"title":"新模板","saleType":1},
    #         headers=head)
    #
    #     assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
    #     # 提示响应json
    #     MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()
    #
    #     assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
    #     # 获取响应中键data的值
    #     MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
    #     # 获取响应中键list的值
    #     MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']
    #
    #     for i in range(2):
    #         list1 = MachinePage_respp_json_data_list[i]
    #         # 获取json中id的值
    #         machineid = list1['id']
    #
    #         # 将machineid 从str类型转换成list类型
    #         machineIds = machineid.split()
    #
    #         # 获取json中classid的值
    #         Machine_class_id = list1['classId']
    #
    #         for j in range(2):
    #             list2 = MachineTemplatePage_resp_json_data_list[j]
    #
    #             # 获取json中id的值
    #             templateid = list2['id']
    #
    #             # 获取json中classid的值
    #             template_class_id = list2['classId']
    #
    #             # 将template_class_id与Machine_class_id进行判断是否能执行模板与设备的绑定关系
    #             if template_class_id != Machine_class_id :
    #                 print ('无法执行')
    #             else:
    #
    #                 # 设备与模板进行绑定
    #                 add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
    #                          json= {"machineIds":machineIds,"templateId":templateid},
    #                          headers= head)
    #
    #                 assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)
    #
    #                 add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()
    #
    #                 assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")

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
                             json= {"region":13798,"sequence":sequence,"address":address,"title":title,
                                    "macAddress":maccode,"deviceId":deviceid,"saleType":2,"classId":classid,
                                    "batchNumber":batchNumber,"runStatus":1,"remarks":"","deviceTitle":title},
                             headers= head)
    #
    #     assertions.assert_code(add_emergency_supplies_resp.status_code,200)
    #
    #     add_emergency_supplies_resp_json = add_emergency_supplies_resp.json()
    #
    #     assertions.assert_in_text(add_emergency_supplies_resp_json["resMsg"],'success')
    #
    #     # 获取机器列表
    #     MachinePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
    #         json={"page":1,"size":10,"saleType":2,"title":title},
    #         headers=head)
    #
    #     assertions.assert_code(MachinePage_resp.status_code, 200)
    #     # 提示响应json
    #     MachinePage_resp_json = MachinePage_resp.json()
    #
    #     assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
    #     # 获取响应中键data的值
    #     MachinePage_respp_json_data = MachinePage_resp_json['data']
    #     # 获取响应中键list的值
    #     MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']
    #
    #     #获取list中的json
    #     MachinePage_respp_json_data_list_json = MachinePage_respp_json_data_list[0]
    #     # 获取json中id的值
    #     machineid = MachinePage_respp_json_data_list_json['id']
    #
    #     # 将machineid 从str类型转换成list类型
    #     machineIds = machineid.split()
    #
    #     # 获取模板列表
    #     MachineTemplatePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
    #         json={"title":"应急物资模板001","saleType":2},
    #         headers=head)
    #
    #     assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
    #     # 提示响应json
    #     MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()
    #
    #     assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
    #     # 获取响应中键data的值
    #     MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
    #     # 获取响应中键list的值
    #     MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']
    #
    #     # 获取list中的json
    #     MachineTemplatePage_resp_json_data_list_json = MachineTemplatePage_resp_json_data_list[0]
    #
    #     # 获取json中id的值
    #     templateid = MachineTemplatePage_resp_json_data_list_json['id']
    #
    #     # 设备与模板进行绑定
    #     add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
    #                              json= {"machineIds":machineIds,"templateId":templateid},
    #                              headers= head)
    #
    #     assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)
    #
    #     add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()
    #
    #     assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")
    #
    # @allure.severity('critical')
    # @allure.story('储物柜设备配置')
    # def test_add_locker(self):
    #     # 获取classId
    #     db = pymysql.Connect("192.168.1.104", "root", "NMvf75#_$%c%BcD$F8l$", "zhhome_db")
    #     cursor = db.cursor()
    #     # 根据shop_vending_machine_class表中title字段查询classid
    #     cursor_execute = cursor.execute("SELECT * FROM `shop_vending_machine_class` WHERE title = '储物柜型号001'")
    #     bb = cursor.fetchone()
    #
    #     classid = bb[0]
    #
    #     # 添加应急物质设备
    #     add_locker_resp = request.post_request(url= url2 + '/api/machineManage/console/shop/vending/machine/addShopVendingMachine',
    #                          json= {"region":13798,"sequence":sequence,"address":address,"title":title,
    #                                 "macAddress":maccode,"deviceId":deviceid,"saleType":3,"classId":classid,
    #                                 "batchNumber":batchNumber,"runStatus":1,"remarks":"","deviceTitle":title},
    #                          headers= head)
    #
    #     assertions.assert_code(add_locker_resp.status_code,200)
    #
    #     add_locker_resp_json = add_locker_resp.json()
    #
    #     assertions.assert_in_text(add_locker_resp_json["resMsg"],'success')
    #
    #     # 获取机器列表
    #     MachinePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/queryShopVendingMachinePage',
    #         json={"page":1,"size":10,"saleType":3,"title":title},
    #         headers=head)
    #
    #     assertions.assert_code(MachinePage_resp.status_code, 200)
    #     # 提示响应json
    #     MachinePage_resp_json = MachinePage_resp.json()
    #
    #     assertions.assert_in_text(MachinePage_resp_json['resMsg'], "success")
    #     # 获取响应中键data的值
    #     MachinePage_respp_json_data = MachinePage_resp_json['data']
    #     # 获取响应中键list的值
    #     MachinePage_respp_json_data_list = MachinePage_respp_json_data['list']
    #
    #     #获取list中的json
    #     MachinePage_respp_json_data_list_json = MachinePage_respp_json_data_list[0]
    #     # 获取json中id的值
    #     machineid = MachinePage_respp_json_data_list_json['id']
    #
    #     # 将machineid 从str类型转换成list类型
    #     machineIds = machineid.split()
    #
    #     # 获取模板列表
    #     MachineTemplatePage_resp = request.post_request(
    #         url=url2 + '/api/machineManage/console/shop/vending/machine/template/queryShopVendingMachineTemplatePage',
    #         json={"title":"储物柜模板001","saleType":3},
    #         headers=head)
    #
    #     assertions.assert_code(MachineTemplatePage_resp.status_code, 200)
    #     # 提示响应json
    #     MachineTemplatePage_resp_json = MachineTemplatePage_resp.json()
    #
    #     assertions.assert_in_text(MachineTemplatePage_resp_json['resMsg'], "success")
    #     # 获取响应中键data的值
    #     MachineTemplatePage_resp_json_data = MachineTemplatePage_resp_json['data']
    #     # 获取响应中键list的值
    #     MachineTemplatePage_resp_json_data_list = MachineTemplatePage_resp_json_data['list']
    #
    #     # 获取list中的json
    #     MachineTemplatePage_resp_json_data_list_json = MachineTemplatePage_resp_json_data_list[0]
    #
    #     # 获取json中id的值
    #     templateid = MachineTemplatePage_resp_json_data_list_json['id']
    #
    #     # 设备与模板进行绑定
    #     add_VendingMachineTemplate_resp = request.post_request(url = url2 + '/api/machineManage/console/shop/vending/machine/template/bindingMachineAndTemplate',
    #                              json= {"machineIds":machineIds,"templateId":templateid},
    #                              headers= head)
    #
    #     assertions.assert_code(add_VendingMachineTemplate_resp.status_code,200)
    #
    #     add_VendingMachineTemplate_resp_json = add_VendingMachineTemplate_resp.json()
    #
    #     assertions.assert_in_text(add_VendingMachineTemplate_resp_json['resMsg'],"success")
