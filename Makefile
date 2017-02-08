
SUBDIR := $(wildcard *.lv2/)
#SUBDIR := $(filter-out  debian/, $(SUBDIR))

.PHONY: $(SUBDIR) recurse

$(MAKECMDGOALS) recurse: $(SUBDIR)

$(SUBDIR):
	@exec $(MAKE) -C $@ $(MAKECMDGOALS)
