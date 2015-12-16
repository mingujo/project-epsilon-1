.PHONY: all clean coverage test verbose

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests code/utils/tests data/tests/ --with-coverage --cover-package=code/utils/functions,data/data_hashes.py

test:
	nosetests code/utils/tests data/tests/

verbose:
	nosetests data/tests code/utils/tests -v

data:
	cd data && make download_all

validate_data:
	cd data && make validate_data

eda:
	cd code/utils/scripts && python eda.py
	cd code/utils/scripts && python hist-outliers_script.py

linear:
	cd code/utils/scripts && python linear_regression_script.py

lostic:
	cd code/utils/scripts && python log_regression_script.py

t-test:
	cd code/utils/scripts && python t_test_plot_script.py

convolution-high:
	cd code/utils/scripts && python convolution_high_res_script.py

convolution-normal:
	cd code/utils/scripts && python convolution_normal_script.py

correlation:
	cd code/utils/scripts && python correlation_script.py

noise-pca:
	cd code/utils/scripts && python noise-pca_script.py
	cd code/utils/scripts && python noise-pca_filtered_script.py

multi-comparison:
	code code/utils/scripts && python multi_comparison_script.py

all-analysis:
	make eda 
	make linear
	make logistic
	make t-test
	make convolution-high
	make convolution-normal
	make correlation
	make noise-pca 
	make multi-comparison
