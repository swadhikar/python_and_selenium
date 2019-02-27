from subprocess import Popen, PIPE, call, check_output
from log_util.logger import log


class Command:

    def __init__(self):
        pass

    @staticmethod
    def execute(cmd):
        """
            @brief        Executes a command, displays output and returns status
            @param   cmd  Command to execute
            @return       Command output
        """
        process = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
        status = process.wait()
        output, error = process.communicate()

        if status != 0:
            print("Command execution failed: '{}'".format(cmd))
            output = error

        print("Output: " + output)
        return status

    @staticmethod
    def get_output(cmd):
        """
            @brief        Executes a command and returns output
            @param   cmd  Command to execute
            @return       Command output
        """
        if not cmd:
            raise Exception("Please enter a valid command to run. You entered '{}'".format(cmd))

        log.info("[Command.get_output()] Executing command: '{}'".format(cmd))
        list_cmd = str(cmd).split(" ")

        return check_output(list_cmd)

    @staticmethod
    def run(cmd):
        """
            @brief        Executes a command
            @param   cmd  Command to execute
            @return  1    Success
        """
        if not cmd:
            raise Exception("Please enter a valid command to run. You entered '{}'".format(cmd))

        log.info("[Command.run()] Executing command: '{}'".format(cmd))

        list_cmd = str(cmd).split(" ")
        call(list_cmd)

        log.info("[Command.run()] Command executed successfully!")
        return 1


if __name__ == '__main__':
    pass
    # print Command.execute('ls -l2344tr')
    print Command.execute('hostname') # Get machine name
    print Command.execute('thiscommandshouldnotbefound') # Get machine name
    # print Command.get_output(cmd='sudo pip install cryptography')
    # print Command.get_output(cmd='sudo pip install python-dateutil')
    # print Command.get_output("ls -ltr /dev/null")
    # print Command.get_output("ls -ltr /")
    # Command.run("sudo scutil --set ComputerName swadhi-macbook-pro")
    # Command.run("sudo scutil --set HostName swadhi-macbook-pro")
    # Command.run("sudo scutil --set LocalHostName swadhi-macbook-pro")
    # print "\nHostname: " + Command.get_output('hostname')
