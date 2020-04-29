from util.service import Service


class ResourceManagement:

    def __init__(self):
        self.session = Service.get_session()

    def add_resource(self,add_url,add_resource_data):
        return  self.session.post(add_url,add_resource_data)

    def signed_up(self,signed_url,signed_up_data):
        return  self.session.post(signed_url,signed_up_data)

    def query_resource(self,query_resource_url,query_resource_data):
        return  self.session.post(query_resource_url,query_resource_data)

    def modify_CusInfo(self,modify_CusInfo_url,modify_CusInfo_data):
        return self.session.post(modify_CusInfo_url,modify_CusInfo_data)

    def abandon_resource(self,abandon_resource_url,abandon_resource_data):
        return self.session.post(abandon_resource_url,abandon_resource_data)

    #分配资源
    def query_allocate_resources(self,query_allocate_resources_url,query_allocate_resources_data):
        return self.session.post(query_allocate_resources_url,query_allocate_resources_data)
    #分配资源提交
    def save_resource_to_Pool(self,to_pool_url,to_pool_data):
        return self.session.post(to_pool_url,to_pool_data)
    #等比例分配资源
    def equal_distribution(self,equal_distribution_url,equal_distribution_data):
        return self.session.post(equal_distribution_url,equal_distribution_data)
    #公共池查询
    def query_public_resources(self,query_public_resources_url,query_public_resources_data):
        return self.session.post(query_public_resources_url,query_public_resources_data)
    #公共池认领
    def own_public(self,own_public_url,own_public_data):
        return self.session.post(own_public_url,own_public_data)
    #转交资源查询
    def query_transmit(self,query_transmit_url,query_transmit_data):
        return self.session.post(query_transmit_url,query_transmit_data)
    #转交资源
    def updata_transmit(self,updata_transmit_url,updata_transmit_data):
        return self.session.post(updata_transmit_url,updata_transmit_data)