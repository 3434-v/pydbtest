/*第一个py存储过程
  declare 声明变量
  */
/*
delimiter  $$
CREATE PROCEDURE test1()
BEGIN
    declare  usernames varchar(30) default '';
    declare  userids varchar(30) default '001';
    set usernames='389863294@qq.com';
    select userid into userids from usermessage where username=usernames;
    select userids;

end $$
delimiter ;
*/

/*
delimiter $$
create procedure testcount()
begin
    declare username_count int default 0;
    declare env_count int default  0;
    declare userid_count int default 0;
        begin
            select count(username) into username_count from usermessage;
            select count(environment) into env_count from usermessage where environment='预发布环境';
        end;
        begin
            select count(username) into userid_count from user where  environment='预发布环境';
        end;
    select username_count, env_count,userid_count;
end $$
delimiter ;
*/

/*
delimiter $$
create procedure  pytest1(
    in usernames varchar(20)
)
begin
    declare  result varchar(20) default '';
    begin
        select userid into result from usermessage where username=usernames;

    end;
    select result;
end $$
delimiter ;
*/


/*
delimiter $$
create procedure pytest2(
    in userids varchar(30)
)
BEGIN
    declare result varchar(30) default '';
    begin
        declare phones varchar(30) default '';
        declare usernames varchar(30) default  '';
        select username into usernames from usermessage where userid=userids;
        select phone into phones from usermessage where username=usernames;
        if (phones="8618770185021") then
            set result=phones;
        else
            set result='666666';
        end if;
    end;
select result;
end $$
delimiter ;
*/

# 正则匹配
# delimiter $$
# create procedure relation(
#     in usernames varchar(30)
# )
# BEGIN
#     declare  userids varchar(30) default '';
#     declare  userid_msg varchar(200) default '';
#     declare  result varchar(50) default '';
#     begin
#         declare strindex1 int default 0;
#         declare strindex2 int default 0;
#         declare strindex int default 0;
#         select userid into userids from usermessage where username=usernames;
#         select channel into userid_msg from registermsg where username=usernames;
#         select locate('", "activityid"', userid_msg) into strindex1;
#         select locate('"share_id": "', userid_msg) into strindex2;
#         set strindex2 = strindex2 + 13;
#         set strindex = strindex1 - strindex2;
#         select substring(userid_msg, 30, strindex) into result;
#     end;
#     select result;
# end $$
# delimiter ;

delimiter $$
create procedure select_lever(
    in uname varchar(30)
)
BEGIN
    declare  uid varchar(30) default '';
    declare  umsg varchar(30) default '';
    begin
        select userid into uid from usermessage where username=uname;
        select username into umsg from registermsg where substring(channel,30,11)=uid;
    end;
    select uid,umsg;
end $$
delimiter ;