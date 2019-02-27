import os
import time
import shutil
import urllib2
from log_util.logger import log


class FileUtil:

    def __init__(self):
        pass

    @classmethod
    def clear_file(cls, path):
        """
            @brief          empties the content of a file
            @param   path    file path
        """
        if not os.path.isfile(path=path):
            cls.create_file(path=path)
            return

        cls.remove(path=path)
        cls.create_file(path=path)

    @classmethod
    def is_exists(cls, path):
        """
            @brief          check if the path exists
            @param  path    file path
        """
        if os.path.exists(path):
            return 1

        log.info('[FileUtil] File does not exist: {}'.format(path))
        return 0

    @classmethod
    def get_file_type(cls, path):
        """
            @brief          return the file type
            @param   path    file path
            @return         'file' - file,
                            'dir' - directory,
                            None - path does not exist
        """
        if not cls.is_exists(path):
            return None

        if os.path.isfile(path):
            return 'file'

        return 'dir'

    @classmethod
    def remove(cls, path):
        """
            @brief          removes a file or directory
            @param  path    path to be removed
        """
        file_type = cls.get_file_type(path)

        if not file_type:
            return

        if file_type is 'file':
            os.remove(path)
        else:
            shutil.rmtree(path)

        log.info("[FileUtil] File removed successfully: {}".format(path))

    @classmethod
    def create_file(cls, path):
        """
            @brief          creates a file
            @param  path    path of the file to be created
        """
        open(path, 'a').close()

    @classmethod
    def create_directory(cls, path, mode=0777, override=False):
        """
            @brief            creates a directory in the given path
            @param  path      path of the file to be created
            @param  mode      directory mode
            @param  override  should the directory be removed if already exists?
        """
        if os.path.isdir(path) and override:
            log.info('[FileUtil] Directory already exists and override value is set to true. Deleting...')
            cls.remove(path)
            time.sleep(0.5)

        try:
            os.makedirs(path, mode)
        except OSError:
            if not os.path.isdir(path):
                raise

        log.info('[FileUtil] Directory created successfully: {}'.format(path.split('/')[-1]))

    @classmethod
    def download_file(cls, url, file):
        """
            @brief              Downloads a file from the given url
            @param   url        Download link
            @param   file       Name of the file to be downloaded
            @return  1          Successful download
            @raise   Exception  Download failure
        """
        if not url or not file:
            raise Exception("Need to specify a valid url and file name to download file")

        log.info("[FileUtil] Downloading file: " + str(file))

        try:
            f = urllib2.urlopen(url)
            data = f.read()

            if os.path.isfile(file):
                cls.clear_file(file)

            with open(file, 'wb') as fileObj:
                fileObj.write(data)

        except Exception as e:
            log.info("[FileUtil] Failed to download file: " + file)
            log.write("Caused by: \n", e)
            raise

        log.info("[FileUtil] Download Successful!")
        return 1

    @classmethod
    def list_directory_contents(cls, path, list_dir=True):
        """
            @brief               Lists contents of directory
            @param   path        Target directory
            @param   list_dir    Flag to exclude listing directory
            @return  list_files  List of files
            @return  None        Directory not present
        """
        list_files = list()

        if not cls.is_exists(path):
            return None

        for filename in os.listdir(path):
            if os.path.isdir(os.path.join(path, filename)):
                if not list_dir:
                    continue
            list_files.append(filename)

        return list_files


if __name__ == '__main__':
    FileUtil.create_directory('../log/test_dir', mode=0755, override=False)
    print FileUtil.list_directory_contents('../log/test_dir', list_dir=False)
    FileUtil.remove('../log/test_dir')
