install:
	sudo pip3 install requests

run: install
	python3 app.py

clean:
	rm *~
