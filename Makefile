default: results

cases: template.m generate_cases.py
	python generate_cases.py

results: cases cases/*.m
	python launch_results.py
