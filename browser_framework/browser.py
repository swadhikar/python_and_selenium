from time import sleep

import atomac

from lib.lib_command import Command
from lib.lib_file_util import FileUtil as file
from lib.variables import BID_FIREFOX, FIREFOX_FILE, FIREFOX_V51
from lib.lib_os_util import capture_screen

from log_util.logger import log


class FireFox:
    def __init__(self):
        pass

    @classmethod
    def is_installed(cls):
        cmd = "ls /Applications/ | grep -i firefox"

        if not Command.execute(cmd):
            log.info("[FireFox] Firefox not installed in this machine")
            return 0

        log.info("[FireFox] Firefox already installed!")
        return 1

    @classmethod
    def uninstall(cls):
        cmd = 'sudo rm -rf /Applications/Firefox.app/'

        if not Command.execute(cmd):
            log.info("[FireFox] Unable to uninstall firefox!")
            return 0

        log.info("[FireFox] Firefox uninstalled successfully!")
        return 1

    @classmethod
    def run(cls, command):
        if not Command(command).execute():
            return 0
        return 1

    @classmethod
    def mount(cls, installer):
        cmd = 'sudo hdiutil attach {}'.format(installer)

        if not cls.run(cmd):
            log.error("[FireFox] Failed to mount volume")
            return 0

        log.info("[Firefox] Firefox volume mounted successfully!")
        return 1

    @classmethod
    def un_mount(cls):
        cmd = 'sudo hdiutil detach /Volumes/Firefox'

        if not cls.run(cmd):
            log.warn("[FireFox] Failed to unmount volume")
        else:
            log.info("[Firefox] Firefox volume unmounted successfully!")
        return 1

    @classmethod
    def install(cls):
        cmd = 'sudo cp -R /Volumes/Firefox/Firefox.app/ /Applications/Firefox.app'

        if not cls.run(cmd):
            log.error("[FireFox] Failed to copy Firefox.app to Applications folder")
            return 0

        log.info("[Firefox] Firefox installed successfully!")
        return 1

    @classmethod
    def install_firefox(cls, installer=None, remove=False):
        if not installer:
            log.error("Need to specify the installer file to proceed with installation")
            return 0

        if remove and cls.is_installed():
            if not cls.uninstall():
                return 0

        if not cls.mount(installer=installer):
            return 0
        sleep(2)

        if not cls.install():
            return 0
        sleep(2)

        if not cls.un_mount():
            return 0
        sleep(2)

        return cls.check_installation()

    @classmethod
    def check_installation(cls):
        found = 0
        cmd = 'open -a Firefox'

        log.info("[Firefox] Starting firefox...")

        if not cls.run(cmd):
            log.info("[Firefox] Failed to open firefox")
            return 0

        try:
            firefox = atomac.getAppRefByBundleId(BID_FIREFOX)
            found = 1
            firefox.activate()
            sleep(5)
            capture_screen('firefox_install_success')
            sleep(2)
            atomac.terminateAppByBundleId(BID_FIREFOX)
            log.info ("[Firefox] Firefox launched successfully!")
        except ValueError:
            log.error("[Firefox] Firefox not running!")

        return found

    @classmethod
    def download_firefox(cls, url, installer):
        if not file.download_file(url=url, file=installer):
            log.error('[Firefox] Failed to download firefox installer from website')
            return 0

        log.info("[Firefox] Downloaded firefox from website successfully!")
        return 1

    @classmethod
    def download_and_install_firefox(cls, url, installer):
        if not cls.download_firefox(url=url, installer=installer):
            return 0

        if not cls.install_firefox(installer=installer, remove=True):
            return 0

        log.info("[Firefox] Firefox installation successful!")

        return 1


if __name__ == '__main__':
    pass
    # print FireFox.download_and_install_firefox(url=FIREFOX_V51, installer=FIREFOX_FILE)
