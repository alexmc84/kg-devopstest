package 'httpd' do
    action :install
end

file '/etc/motd' do
    owner 'root'
    group 'root'
    mode '0644'
    content 'Hello world'
end


service 'httpd' do
  action :start
end


user 'alejandro.merino' do
  shell '/bin/bash'
  password '1234'
end


cron 'test_cron' do
  action :create
  minute '45'
  hour '5'
  command 'ls -lrt'
end


timezone 'London' do
  timezone 'Europe/London'
end