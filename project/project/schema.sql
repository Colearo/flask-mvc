drop table if exists Tasks;
create table Tasks (
  task_id integer primary key autoincrement,
  task text not null,
  status INT not null
);
