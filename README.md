# Secondary development templates based on django
#    Development and using need to know：
*        1.conf/
            All variable configuration directory: including the log configuration, celery configuration, database configuration, the routing configuration

*        2.controller/
            django native configuration directory

*        3.resource/
            common/
                Includes common tooling packages, such as defining standard output and catching arbitrary exceptions

            extension/
                This directory mainly solves the user needs the custom module to carry on the encapsulation

*        4.views/
            This directory is primarily where developers define API interfaces
            This directory provides test views for developers to refer to


# centos introduction:
*    step1. Modify uwsgi.ini
*         Please modify the port number.

*    step2.Installing CentOS environment dependencies
*        sudo yum install -y pcre pcre-devel pcre-static
*        sudo yum install -y gcc
*        sudo yum install -y python-devel


*    step3. Note
*        1.There may be a system error, and you will get the following error: "\r"
*            sudo yum install -y dos2unix
*            dos2unix *
*            dos2unix */*
*            dos2unix */*/*

#    1. start
        sh bin/start.sh
#    2. stop
        sh bin/stop.sh
        
# Docker:
    * step1: build image
        docker build -t pand-python-3.6-django:base .

    * step2: start container
        docker run -itd --name {container_name} -v {project_dir}:/opt/app-root/src/ -p 8000:7999 pand-python-3.6-django:base bash
