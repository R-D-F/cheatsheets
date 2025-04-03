# Linux Terminal Cheat Sheet

## Basic Commands
- **List files and directories** – `ls`
- **List all files (including hidden)** – `ls -a`
- **List with details (permissions, size, etc.)** – `ls -l`
- **Change directory** – `cd [directory]`
- **Go up one level** – `cd ..`
- **Print current directory** – `pwd`
- **Create a new directory** – `mkdir [directory]`
- **Remove a directory** – `rmdir [directory]`
- **Remove a file** – `rm [file]`
- **Remove a directory and its contents** – `rm -r [directory]`
- **Copy a file** – `cp [source] [destination]`
- **Move (or rename) a file** – `mv [source] [destination]`
- **Display file contents** – `cat [file]`
- **View file content one page at a time** – `less [file]`
- **Edit a file (nano editor)** – `nano [file]`

## File Permissions
- **View file permissions** – `ls -l`
- **Change file permissions** – `chmod [mode] [file]`
  - Example: `chmod 755 script.sh`
- **Change file ownership** – `chown [user]:[group] [file]`
  - Example: `chown user:group file.txt`

## Searching
- **Find files by name** – `find /path -name "filename"`
- **Find files by type** – `find /path -type f -name "*.txt"`
- **Search inside files** – `grep "text" [file]`
- **Search recursively in directories** – `grep -r "text" [directory]`

## Process Management
- **List running processes** – `ps aux`
- **Find a process by name** – `ps aux | grep [name]`
- **Kill a process by PID** – `kill [PID]`
- **Kill a process by name** – `pkill [name]`
- **Monitor system processes interactively** – `top` or `htop`

## Networking
- **Check your IP address** – `ip a`
- **Ping a host** – `ping [host]`
- **Check open ports** – `netstat -tulnp`
- **Download a file** – `wget [URL]`
- **Download a file (alternative)** – `curl -O [URL]`

## User Management
- **Show current user** – `whoami`
- **Switch user** – `su [username]`
- **Add a new user** – `sudo adduser [username]`
- **Delete a user** – `sudo deluser [username]`
- **Show system users** – `cat /etc/passwd`

## System Monitoring
- **Show disk usage** – `df -h`
- **Show directory size** – `du -sh [directory]`
- **Show memory usage** – `free -h`
- **Show system uptime** – `uptime`

## Package Management
### Debian-based (Ubuntu, Debian)
- **Update package list** – `sudo apt update`
- **Upgrade installed packages** – `sudo apt upgrade`
- **Install a package** – `sudo apt install [package]`
- **Remove a package** – `sudo apt remove [package]`

### RedHat-based (Fedora, CentOS)
- **Update system** – `sudo dnf update`
- **Install a package** – `sudo dnf install [package]`
- **Remove a package** – `sudo dnf remove [package]`

## File Compression
- **Compress files into a .tar.gz archive** – `tar -czvf archive.tar.gz [files]`
- **Extract a .tar.gz archive** – `tar -xzvf archive.tar.gz`
- **Compress files into a .zip archive** – `zip archive.zip [files]`
- **Extract a .zip archive** – `unzip archive.zip`

---

### Notes:
- `[text]` indicates a placeholder, replace it with actual values.
- `sudo` may be required for administrative commands.
- Use `man [command]` for detailed help on any command.
