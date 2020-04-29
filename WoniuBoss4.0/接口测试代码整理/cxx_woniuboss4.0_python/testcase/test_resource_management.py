
import unittest
from parameterized import parameterized
from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
#print(data_config_info)
add_resource_data = Utility.get_excel_to_tuple(data_config_info[0])
#print(add_resource_data)
signed_up_data = Utility.get_excel_to_tuple(data_config_info[1])
#print(signed_up_data)
query_resource_data = Utility.get_excel_to_tuple(data_config_info[2])
modify_CusInfo_data = Utility.get_excel_to_tuple(data_config_info[3])
abandon_resource_data = Utility.get_excel_to_tuple(data_config_info[4])
query_allocate_resources_data = Utility.get_excel_to_tuple(data_config_info[5])
save_resource_to_Pool_data = Utility.get_excel_to_tuple(data_config_info[6])
equal_distribution_data = Utility.get_excel_to_tuple(data_config_info[7])
query_public_resources_data = Utility.get_excel_to_tuple(data_config_info[8])
own_public_data = Utility.get_excel_to_tuple(data_config_info[9])
query_transmit_data = Utility.get_excel_to_tuple(data_config_info[10])
updata_transmit_data = Utility.get_excel_to_tuple(data_config_info[11])

class ResourceManagementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from common.resource_management import ResourceManagement
        cls.resource_obj = ResourceManagement()

    @classmethod
    def tearDownClass(cls):
        pass

    '''
    # 资源增加的接口测试
    @parameterized.expand(add_resource_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        add_resource_resp = self.resource_obj.add_resource(url, test_data)
        # print(add_resource_resp)
        content = add_resource_resp.text
        print(content)
        if content == "新增成功":
            result = "add success"
        elif content == "该资源现属于超级管理员名下,已更新该资源的信息.":
            result = "already added"
        else:
            result = "add fail"
        self.assertEqual(resp_content, result)
    

    # 修改状态为已报名
    @parameterized.expand(signed_up_data)
    def test_resource_obj(self,url,method,test_data,resp_code,resp_content):
        signed_up_resp = self.resource_obj.signed_up(url,test_data)
        #print(add_resource_resp)
        content = signed_up_resp.text
        print(content)
        if content == "newStudent":
            result = "flow ok"
        else:
            result = "flow fail"
        self.assertEqual(resp_content,result)
    
    # 查询资源
    @parameterized.expand(query_resource_data)
    def test_resource_obj(self,url,method,test_data,resp_code,resp_content):
        query_resource_resp = self.resource_obj.query_resource(url,test_data)
        #print(add_resource_resp)
        content = query_resource_resp.json()
        print(content['totalRow'])
        if content['totalRow'] > 0:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content,result)
    

    # 修改资源信息
    @parameterized.expand(modify_CusInfo_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.modify_CusInfo(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.text
        print(content)
        if content == "修改成功":
            result = "edit success"
        else:
            result = "edit already"
        self.assertEqual(resp_content, result)
    
    # 废弃资源信息
    @parameterized.expand(abandon_resource_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.abandon_resource(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.text
        print(content)
        if content == "废弃资源完成.":
            result = "abandon success"
        else:
            result = "abandon fail"
        self.assertEqual(resp_content, result)
    
    # 查询分配资源信息
    @parameterized.expand(query_allocate_resources_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.query_allocate_resources(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.json()
        print(content["totalRow"])
        if content["totalRow"] > 0:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)
    
    #分配资源提交接口
    @parameterized.expand(save_resource_to_Pool_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.save_resource_to_Pool(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.text
        print(content)
        if content > "0":
            result = "submit ok"
        else:
            result = "submit fail"
        self.assertEqual(resp_content, result)
    
    # 查询公共池资源
    @parameterized.expand(_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.equal_distribution(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.text
        print(content)
        if content == "success":
            result = "allot ok"
        else:
            result = "allot fail"
        self.assertEqual(resp_content, result)


    # 查询分配资源信息
    @parameterized.expand(query_public_resources_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.query_public_resources(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.json()
        print(content["totalRow"])
        if content["totalRow"] > 0:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)
    
    #公共池认领
    @parameterized.expand(own_public_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.own_public(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.json()
        print(content)
        if content > "0":
            result = "owner ok"
        else:
            result = "owner fail"
        self.assertEqual(resp_content, result)
    

    # 查询转交资源信息
    @parameterized.expand(query_transmit_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.query_transmit(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.json()
        print(content["totalRow"])
        if content["totalRow"] > 0:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)
    '''

    # 转交资源
    @parameterized.expand(updata_transmit_data)
    def test_resource_obj(self, url, method, test_data, resp_code, resp_content):
        query_resource_resp = self.resource_obj.updata_transmit(url, test_data)
        # print(add_resource_resp)
        content = query_resource_resp.text
        print(content)
        if content == "success":
            result = "update success"
        else:
            result = "update fail"
        self.assertEqual(resp_content, result)





if __name__ == '__main__':
    unittest.main(verbosity=2)