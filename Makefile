PREFIX?= /usr/local
BINDIR?= ${PREFIX}/bin
INSTALL?= install
INSTALLDIR= ${INSTALL} -d
INSTALLBIN= ${INSTALL} -m 755

uninstall:
	rm -f ${DESTDIR}${BINDIR}/pymuxinator

install:
	python setup.py install
	${INSTALLDIR} ${DESTDIR}${BINDIR}
	${INSTALLBIN} ./bin/pymuxinator ${DESTDIR}${BINDIR}

.PHONY: install uninstall
