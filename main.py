from process import *
import idna


def init():
    #读country
    fin=open('other_data/country.txt')
    for line in fin:
        country=line.strip()
        data.List_country.append(country)
    #读asnum2asname
    fin=open('./other_data/asnum2asname.txt',encoding='utf-8')
    for line in fin:
        list_tp=line.split(None,1)
        data.Dic_asnum_asname[list_tp[0]]=list_tp[1].strip()
    fin.close()
    #读public resolver
    fin=open('other_data/public_resolver_ip.txt')
    for line in fin:#对于每个公共解析器
        [pubres,ips]=line.split(',',1)
        ips_list=ips.strip().split(',')#是个list
        for ip in ips_list:
            data.Dic_ip_pubres[ip]=pubres
    #读public suffix
    fin=open('./other_data/public_suffix.txt',encoding='utf-8')
    for line in fin:
        tp=''
        pubsuf=''
        if line.isspace():
            continue
        if line[0]=='/' and line[1]=='/':
            continue
        if line[0]=='*' and line[1]=='.':
            tp=line[2:]
        elif line[0]=='!':
            tp=line[1:]
        else:
            tp=line
        pubsuf=tp.strip()
        data.List_pubsuf.append(idna.encode(pubsuf).decode())

if __name__=='__main__':
    init()
    process_all()
    process_merge_nxdomain_byday()
    output()