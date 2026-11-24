FROM python:3.14
WORKDIR /emp_recruit 
COPY employee.py .
CMD ["python", "employee.py"]
