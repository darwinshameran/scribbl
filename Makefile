.PHONY: init reqs

HELP_FUNC = \
    %help; \
    while(<>) { \
        if(/^([a-z0-9_-]+):.*\#\#(?:@(\w+))?\s(.*)$$/) { \
            push(@{$$help{$$2}}, [$$1, $$3]); \
        } \
    }; \
    print "usage: make [target]\n\n"; \
    for (sort keys %help) { \
        printf("  %-20s %s\n", $$_->[0], $$_->[1]) for @{$$help{$$_}}; \
        print "\n"; \
    }

help:
	@perl -e '$(HELP_FUNC)' $(MAKEFILE_LIST)

init:		## Install all dependencies from requirements.txt using pip
	sudo pip3 install -r requirements.txt

reqs:		## Generate a requirements.txt using `pipreqs'
	pipreqs $(shell pwd)

#  vim: set ts=4 sw=4 tw=80 et :
