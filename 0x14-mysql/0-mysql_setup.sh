#!/usr/bin/env bash
# Install MySQL on web-01 and web-02 servers

# Update the package list
sudo apt-get update

# Install MySQL server (5.7.x)
sudo apt-get install -y mysql-server-5.7

# Run the MySQL secure installation script
sudo mysql_secure_installation

# Allow MySQL to listen on all addresses (for remote connections)
sudo sed -i 's/bind-address.*/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Restart MySQL service to apply changes
sudo service mysql restart
