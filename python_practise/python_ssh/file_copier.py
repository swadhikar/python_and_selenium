from os.path import basename, expanduser, join
from paramiko import SSHException
import paramiko

__author__ = 'Swadhikar C'


class RemoteManager(object):
    """Manages remote files and directory"""

    def __init__(self, hostname, username, password):
        self.username = username
        self.hostname = hostname
        self.password = password
        self.ssh_conn = None
        self.sftp_con = None

    def __connect(self):
        """Connects to remote host"""
        try:
            self.ssh_conn = paramiko.SSHClient()
            self.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_conn.load_system_host_keys()
            self.ssh_conn.load_host_keys(expanduser('~/.ssh/known_hosts'))
            self.ssh_conn.connect(hostname=self.hostname, username=self.username, password=self.password)
        except Exception as e:
            print 'Failed to connect to remote host: {}.\nCaused by: {}'.format(self.hostname, e)
            raise

        return 1

    def __close(self):
        """Close connection"""
        if self.ssh_conn:
            self.ssh_conn.close()

    def execute(self, command, get_output=True):
        """
            Executes a given remote command and returns output by default.

        @param      command         Command
        @param      get_output      Flag to suppress output return
        @return                     result(success, flag on), 1 (success, flag off), 0 (error)
        """
        self.__connect()
        print 'Executing ssh command: ' + command

        try:
            _, stdout, _ = self.ssh_conn.exec_command(command)
            result = stdout.read().strip()
        except SSHException as e:
            print 'Failed to execute ssh command: ' + command + '. Caused by:\n' + str(e)
            return 0
        finally:
            self.__close()

        result = result if get_output else 1
        return result

    def file_exists(self, filename):
        """
            Checks if a given remote file exists

        @param      filename    File name
        @return                 1 (exists), 0 (not exists)
        """
        ls_cmd = 'ls {} | wc -l'.format(filename)
        result = self.execute(ls_cmd)

        if not int(result):
            print 'File not found: ' + filename
            return False

        print 'File found: ' + filename
        return True

    def copy_ssh(self, file_list, remote_path, force_remove=False):
        """
            Copy given files to remote machine

        @param      file_list       File(s) to copy
        @param      remote_path     Target remote path
        @param      force_remove    Flag to remove if file already exists
        @return                     1 (success), Exception (fail)
        """
        if type(file_list) != list:
            file_list = [file_list]

        copy_files = [join(remote_path, basename(local_file)) for local_file in file_list]
        self.__connect()

        try:
            self.sftp_con = self.ssh_conn.open_sftp()

            if force_remove:
                self.remove_files(copy_files)

            for local_file, copy_file in zip(file_list, copy_files):
                self.sftp_con.put(local_file, copy_file)
                print 'Copied file to remote host: ' + basename(local_file)

        except Exception:
            print 'Remote copy failed!'
            raise

        finally:
            if self.sftp_con:
                self.sftp_con.close()
            self.__close()

        return 1

    def remove_files(self, file_list):
        """
            Remove given files in remote machine

        @param      file_list       File(s) to remove
        @return                     1 (success), Exception (fail)
        """
        if type(file_list) != list:
            file_list = [file_list]

        self.__connect()

        try:
            for remote_file in file_list:
                self.execute('rm -f ' + remote_file, get_output=False)
        except Exception:
            print 'Remote remove failed!'
            raise
        finally:
            self.__close()

        print 'Removed remote files!'
        return 1

    def copy_files(self, files, remote_path, force_remove=False, raise_exception=False):
        """
            Copies a given list of files to remote machine
        
        @param      files               File(s) to copy
        @param      remote_path         Target remote path
        @param      force_remove        Flag to remove if file already exists
        @param      raise_exception     Flag to raise if copy fails
        @return                         1 (success)
                                        0 (fail - flag off)
                                        Exception (fail- flag on)
        """
        if self.copy_ssh(files, remote_path, force_remove):
            print 'Files copied to remote machine successfully!'
            return 1

        fail = 'Failed to copy file to remote machine!'
        if raise_exception:
            raise Exception(fail)

        print fail
        return 0


if __name__ == '__main__':
    from glob import glob

    txt_files = glob('/tmp/*.txt')
    txt_files = sorted(txt_files)

    remote = RemoteManager('127.0.0.1', 'swadhi', 'swadhi')
    remote.copy_files(txt_files, '/tmp/tmp/', force_remove=True)


"""
Output:

/usr/bin/python2.7 /home/swadhi/PycharmProjects/pyselenium/python/python_practise/python_ssh/file_copier.py

copy_files : ['/tmp/tmp/test.txt', '/tmp/tmp/test_copy.txt']
Executing ssh command: rm -f /tmp/tmp/test.txt
Executing ssh command: rm -f /tmp/tmp/test_copy.txt
Removed remote files!
Copied file to remote host: test.txt
Copied file to remote host: test_copy.txt
Files copied to remote machine successfully!

"""