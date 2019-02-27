import paramiko


# For below tasks execute commands and verify
#   Read servers from file
#   Poll server
#   Check ssh service response


class Ssh:
    def __init__(self, remote_ip, remote_user, remote_pwd):
        self.remote_ip = remote_ip
        self.remote_user = remote_user
        self.remote_pwd = remote_pwd
        self.ssh_client = None
        self.connect()  # Connect should happen whenever this class is initiated

    # Connect to remote server
    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.get_host_keys()
            self.ssh_client.load_system_host_keys()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_cl ient.connect(self.remote_ip, username=self.remote_user, password=self.remote_pwd)
            ##### FOR PASSWORDLESS AUTHENTICATION #####
            # sshcon.connect(hostname, username=myuser, key_filename=mySSHK) # no passwd needed
            ########################################
        except paramiko.ssh_exception.AuthenticationException:
            print(
                'Authentication failed. Please check the credentials: {}:{}'.format(self.remote_user, self.remote_pwd))
            raise

        # Verify all other settings are correct by checking the exception type
        print('Connection with host established: {}'.format(self.remote_ip))

    # Execute remote command
    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        result = stdout.read().decode("utf-8")
        return result

    def close_connection(self):
        self.ssh_client.close()


if __name__ == '__main__':
    # ssh = Ssh('127.0.0.1', 'swadhi', 'swadhi')
    ssh = Ssh('127.0.0.1', 'swadhi', 'test')
    # ssh.connect()

    ls_result = ssh.execute_command('ls -ltr /')
    print(ls_result)

    ls_result = ssh.execute_command('cat /etc/ssh/sshd_config | head -n 10')
    print(ls_result)

    ls_result = ssh.execute_command('cat /etc/ssh/sshd_config | tail -n 10')
    print(ls_result)

    ssh.close_connection()
