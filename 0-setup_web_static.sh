#!/usr/bin/env bash
# Sets up a web server for static page deployment/upload

# Install any ubuntu updates
sudo apt -y update
sudo apt -y upgrade

# Server software installations
sudo apt -y --fix-missing install nginx  # add --allow-downgrades flag when reverting upgrade
sudo apt-get -y --fix-missing install ufw  # add --allow-downgrades flag when reverting upgrade

# Allow nginx to pass through firewall
sudo ufw allow 'Nginx HTTP'

# Create neccessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch -c  /data/web_static/releases/test/index.html
sudo chmod -R 755 /data/web_static/releases/test/  # Ensure only admin has write privileges
sudo echo "Hello World! I'm Web Static!" >> /data/web_static/releases/test/index.html  # Write something to file for testing
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current  # -f to remove existing sym link. /current is the sym link referencing /test/ folder
sudo chown -R "ubuntu":"ubuntu" /data/  # Give file and group ownership to user ubuntu


# Edit server block to serve static web content in /current
sudo tee -a "$config_file" > /dev/null <<EOF  # write into the nginx default config file
server {
	listen 80;
	server_name "$domain";

	location / {
		root "$webroot";
		index index.html;
		add_header X-Served-By "$HOSTNAME";
       }
}

EOF

# Reload/Start Nginx to apply changes
sudo nginx -s reload
