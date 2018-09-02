
/*

当日日程安排 -- 2018.09.02  
*/

修改mysql的登录密码:

mysql> set password for 用户名@localhost = password('新密码');


01.写上周的周报 (11点之前完成)
	
	1)完成了对parse解析失败任务的T_HISI_WORK_ORDER工单数据配置,对原有的STATUS为GetParseLotNo状态的数据重新进行了解析;
	
	(任务量为882--> 200w,841-->113w,840-->43w,844-->120w)
	
	2)对无线终端业务进展表进行更新,确定当前的任务进展情况,哪些是缺少LotId或WaferId的项并无法解析的任务,进行相应的标注;
	
	3)周良率数据表导出,根据宋雪兵的要求来进行导出,相应的需求按FAE的要求来;
	
	4)对Log解析的结果数据进行导出,未来根据计划以一定的时间间隔进行导出
	
	(三张表做联合查询T_SLT_TEST_INFO 原log中的BEGIN部分,包含很多测试的信息,
	
	 T_SLT_ONE_TEST 原log中的ONETEST部分,所有当天的数据会追加在一个表T_SLT_ONE_TEST_2018中,
	 
	 查询时以T_SLT_ONE_TEST_2018表的CHIP_ID字段为关联进行查询,其中的BIN_NAME对应的是测试项的名称,BIN_NAME与PATTERN一一对应每行进行单独存储;
	 
	 T_SLT_DIE_ID 表存储的是DieID字符串提取出的寄存器,后面对应的是相应的LotId和WaferId,以及批次信息);
	
	
02.对MySQL的查询语句再熟悉一遍,inner join和group by 及order by 及desc asc的用法(11-12点);

    mysql中的索引类型,主键索引,唯一索引,常规索引,全文索引四种类型

03.使用sql查询语句对数据库进行操作,读取相应的数据后进行文件的导出并且以Excel和csv文件格式进行存储,每次执行

	数据写入时,如何追加在原有的基础之上不用再重新建sheet表(14-16点之间);

04.对定时任务Celery进行服务器部署,实现简单的定时任务拉取,学习如何部署master 和 worker(16-18点);

05.




 




















