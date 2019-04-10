COMPILER=rst2html5
OPTIONS=--stylesheet css/docutils_solarized_light.css
SOURCE=log.rst
TARGET=index.html

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(COMPILER) $(OPTIONS) $(SOURCE) > $(TARGET)

.PHONY:
clean:
	rm $(TARGET)
