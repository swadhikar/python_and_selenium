from io import StringIO
from contextlib import redirect_stdout
from contextlib import suppress
from python.log_util.logger import log


class CaptureIO:

    @staticmethod
    def get_help(module_name):
        io_obj = StringIO()
        with redirect_stdout(io_obj):
            with suppress(Exception):
                exec('import ' + module_name)
            exec(f'help({module_name})')
        return io_obj.getvalue()


if __name__ == '__main__':
    help_txt = CaptureIO.get_help('python.log_util.logger')
    log.info('Help result: \n\n' + help_txt)
