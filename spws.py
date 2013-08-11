from Server import Server
import asyncore        

def runserver():
    s = Server('0.0.0.0', 8080, 'index.html')
    print 'Server created on port 8080.'
    asyncore.loop()

if __name__ == '__main__':
    try:
        runserver()
    except KeyboardInterrupt:
        print '\nGoodbye.'
