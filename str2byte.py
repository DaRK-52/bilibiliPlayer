class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj

    def read(self, size):
        return self.fileobj.read(size).encode()

    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

    def write(self, size):
        return self.fileobj.write(size)

    def writeline(self, size=-1):
        return self.fileobj.writeline(size)
