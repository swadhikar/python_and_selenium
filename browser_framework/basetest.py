# Base test case for all the test cases to implement
from lib.variables import SCREENSHOT_PATH as screen_shot_path
from lib.lib_os_util import capture_screen
from log_util.logger import log


class BaseTestCase(object):
    def __init__(self):
        pass

    @staticmethod
    def take_screen_shot(filename='screenshot'):
        if not capture_screen(screen_shot_path, filename):
            return 0
        return 1

    @staticmethod
    def execute_step(func, summary, *args, **kwargs):
        """
            @brief            Executes the given function
            @param  func      Method to be executed
            @param  summary   Step summary
            @param  args      List of arguments
            @param  kwargs    Keyword arguments
        """
        stars = (len(summary) + 25) * "*"

        log.info(stars)
        log.info("Method       : " + func.__name__)
        log.info("Summary      : " + summary)
        log.info("Arguments    : " + str(args))
        log.info("Keyword args : " + str(kwargs))
        log.info(stars)

        try:
            func(*args, **kwargs)
        finally:
            log.info("Completed step: '{}'".format(summary))

    @staticmethod
    def execute_step_validate(func, summary, expected_output=(1,), exception=Exception, exception_msg='', *args,
                              **kwargs):
        """
            @brief                   Executes the given function and validates result
            @param  func             Method to be executed
            @param  summary          Step summary
            @param  expected_output  Tuple of elements to be validated against result
            @param  exception        Name of the exception to be thrown
            @param  exception_msg    Exception message while throwing
            @param  args             List of arguments
            @param  kwargs           Keyword arguments
        """
        stars = (len(summary) + 25) * "*"

        log.info(stars)
        log.info("Method       : " + func.__name__)
        log.info("Summary      : " + summary)
        log.info("Arguments    : " + str(args))
        log.info("Keyword args : " + str(kwargs))
        log.info(stars)

        # Force tuple the expected output if not in type tuple or list
        if not isinstance(expected_output, tuple) or not isinstance(expected_output, list):
            expected_output = (expected_output,)

        try:
            result = func(*args, **kwargs)

            if result not in expected_output:
                log.error("Result '{}' not in expected output '{}'".format(result, expected_output))

                if not exception_msg:
                    exception_msg = "Result '{}' not in expected output '{}'".format(result, expected_output)

                raise exception(exception_msg)

            log.info(log.error("Result '{}' is present in expected output '{}'".format(result, expected_output)))
        finally:
            log.info("Completed step: '{}'".format(summary))


if __name__ == "__main__":
    pass

    # from time import sleep
    # from lib.lib_os_util import capture_screen
    # from lib.lib_command import Command
    # BaseTestCase.execute_step(sleep, "Sleeps for 2 seconds", 2)
    # BaseTestCase.execute_step(capture_screen, "Captures current screen", "SampleScreenDev")
    # BaseTestCase.execute_step_validate(func=Command.get_output,
    #                                    summary="Runs ls command and verifies if Drop Box is present",
    #                                    expected_output="Drop Box\n",
    #                                    exception_msg="Unable to find 'Drop Box' in public directory",
    #                                    cmd="ls /Users/swadhikar_c/Public")
    # BaseTestCase.execute_step_validate(BaseTestCase.return_num, "Checks if 1 is returned", expected_output=1,
    #                                    exception=Exception, exception_msg="1 is not returned", num=1)
    # BaseTestCase.execute_step_validate(BaseTestCase.return_num, "Checks if 1 is returned", expected_output=1,
    #                                    exception=Exception, exception_msg="1 is not returned", num=0)
