import asyncore, socket

class PageRequestHandler(asyncore.dispatcher_with_send):
    def __init__(self, sock, filename):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.__filename = filename

    def handle_read(self):
        _ = self.recv(1048576)
        
        header = """HTTP/1.x 200 OK
Content-Type: text/html; charset=UTF-8
Server: Single Page Web Server


"""
        self.send(header.encode('utf-8')
        with open(self.__filename, 'r') as index_file:
            content = index_file.read()
            self.send(content.encode('utf-8'))
        self.close()

class Server(asyncore.dispatcher):
    def __init__(self, host, port, filename):
        asyncore.dispatcher.__init__(self)
        self.__filename = filename
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
    
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            handler = PageRequestHandler(sock, self.__filename)
