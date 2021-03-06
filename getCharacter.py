'''Clase para obtener un simple caracter desde la consola sin pulsar la
	tecla enter'''

class _Getch:
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()

	def __call__(self):
		''' al finalizar la clase devuelve el apuntador de la clase a utilizar '''
		return self.impl()


class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


class _GetchWindows:
	def __init__(self):
		import msvcrt

	def __call__(self):
		import msvcrt
		return msvcrt.getch()
'''
a = True
while(a==True):
    getch = _Getch()

    teclaPulsada=getch.__call__()

    if(teclaPulsada!='*'):
        print "La tecla pulsada ha sido",teclaPulsada
    else:
        a=False
'''
