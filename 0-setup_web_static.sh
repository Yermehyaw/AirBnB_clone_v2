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


# Edit server block to serve static web content in location /hbnb_static
config_file="/etc/nginx/sites-enabled/$HOSTMANE.conf"
# sudo -c "$config_file"  # In case config file hadnt bern created
sudo sed -i "s/location \/ {/\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n\n\tlocation \/ {/g"  "$config_file"
# single quotes can be used to prevent any unforseen shell interference on sed. Always ensure the root and alis direcrives ebd with a / followed by a semicolon.
# an alias was used here mainly for security purposes inorder to obsure the underlying architecture of this page/resource, rather than usubg a root directive which is more revealing of the specific location where the resource is stored.


# Activate server block if not already previously activated
if [ -L "/etc/nginx/sites-enabled" ]  # Does sym link exists here
then
    sudo ln -s "$config" /etc/nginx/sites-enabled/
fi

# Reload/Start Nginx to apply changes
sudo nginx -s reload
