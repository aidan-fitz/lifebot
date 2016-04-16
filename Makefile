install:
	sudo pip3 install requests
	sudo pip3 install tinydb

run: install
	python3 app.py

clean:
	rm *~
