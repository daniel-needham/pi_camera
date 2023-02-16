import os
import paramiko
import config


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="raspberry", username="pi", password=config.pw)
sftp_client = ssh.open_sftp()
sftp_client.put("/home/dan/Projects/pi_camera/pi_camera.py", "/home/pi/Desktop/pi_camera.py")
print("starting..")
stdin, stdout, stderr = ssh.exec_command("cd Desktop; python pi_camera.py", get_pty=True)
for line in iter(stdout.readline, ""):
    print(line, end="")

sftp_client.get("Desktop/test.jpg", "/home/dan/Projects/pi_camera/test.jpg")

sftp_client.close()
ssh.close()
