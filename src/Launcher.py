from subprocess import Popen, call
from sys import argv
from threading import Thread
from time import sleep


class Launcher (object):
    def __init__ (self) -> None:
        self.path: str  = ""
        self.args: list = []
        self.proc: Popen = None
        self.thread: Thread = None


    def run_program (self) -> None:
        self.thread = Thread (target = self.branch_proc)
        self.thread.start()

    def branch_proc (self) -> None:
        self.proc = Popen([self.path] + self.args)


    def proc_is_running (self) -> bool:
        self.proc.poll()
        if (self.proc.returncode is None):
            return True
        else:
            return False

    def set_path (self, filepath: str) -> None:
        self.path = filepath

    def set_args (self, arg_list: str) -> None:
        self.args = arg_list



if __name__ == "__main__":
    my_prog = Launcher ()
    my_prog.set_path(argv[1])
    if len(argv) > 2:
        my_prog.set_args(argv[2:])
    my_prog.branch_proc()

    while (my_prog.proc_is_running() is True):
        pass
    print ("Process Terminated")
