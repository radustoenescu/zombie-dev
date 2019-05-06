COMPILER=rst2html5
OPTIONS=--stylesheet css/docutils_solarized_light.css
SOURCE=log.rst
TARGET=index.html
BROWSER=google-chrome

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(COMPILER) $(OPTIONS) $(SOURCE) > $(TARGET)
	./add-tracking-js.sh $(TARGET)

run: $(TARGET)
	$(BROWSER) $(TARGET) &> /dev/null &

.PHONY:
clean:
	rm $(TARGET)
