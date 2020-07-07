create view teacher2course as
select * from teacher inner join course on teacher.tid = course.teacher_id;