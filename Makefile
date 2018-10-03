PORT=9084
ADMIN_PORT=8003

.PHONY: build symlinks run

symlinks:
	cd lib && python _symlinks.py

build: symlinks

run:
	python /usr/local/bin/dev_appserver.py --host=0.0.0.0 --port=$(PORT) --admin_port=$(ADMIN_PORT) geoscixyz
