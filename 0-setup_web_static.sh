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
sudo touch /data/web_static/releases/test/index.html
sudo chmod -R 755 /data/web_static/releases/test/  # Ensure only admin has write privileges
echo "Hello World! I'm Web Static!" | sudo tee -a /data/web_static/releases/test/index.html  # Write something to file for testing sake. P.S: The no of Hello World strings in the pseudo webpage is the amount of tines this script was ran.
sudo ln -sf -t /data/web_static/releases/test/ /data/web_static/current  # -f to remove existing sym link. /current is the sym link referencing /test/ folder. Check ln -t [DIR] [DEST] in "man ls"
sudo chown -R "ubuntu:ubuntu" /data/  # Give file and group ownership to user ubuntu


# Edit server block to serve static web content in location /hbnb_static
config_file="/etc/nginx/sites-available/default.conf"
sudo sed -i "s/location \/ {/\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html;\n\t}\n\n\tlocation \/ {/g"  "$config_file"
# single quotes can be used to prevent any unforseen shell interference on sed. Always ensure the root and alis direcrives and with a / followed by a semicolon.
# an alias was used here mainly for security purposes inorder to obsure the underlying architecture of this page/resource, rather than usingg a root directive which is more revealing of the specific location where the resource is stored.



# Reload/Start Nginx to apply changes
sudo nginx -s reload
