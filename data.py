dir_in='source_data'
dir_nxdomain_byday='result_data/1_nxdomain_byday'
dir_out='result_data'

#qr
Num_query=0
Num_response=0
Dic_rcode={}

#NXDomain
Dic_nxdomain_dic={}     #当日NXDomain对应的数量
Dic_nxdomain_dic_all={} #合并后一周的

#Fail
Dic_fail_type_dic={}    #不同查询类型的all/1/28的all/success Dic_fail_type_dic['all']['all']
Dic_fail_domain_dic={}  #不同域名的不同查询类型all/1/28的all/success
Dic_fail_resolver_dic={}#不同解析器
Dic_fail_pubres_dic={}  #不同公共解析器

#Status
Dic_status_type_dic={}
Dic_status_domain_dic={}
Dic_status_pubsuf_dic={}
Dic_status_resolver_dic={}
Dic_status_pubres_dic={}

#func用的
List_country=[]         #country列表
Dic_resolver_asnum={}
Dic_asnum_asname={}
Dic_ip_pubres={}
List_pubsuf=[]#公共后缀