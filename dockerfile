FROM python:3.11.7

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /aqs_db_snapshot-2023-10-23/aqsproject

# Copy the current directory contents into the container
COPY . /aqs_db_snapshot-2023-10-23/aqsproject

# Copy the wait-for-it.sh script into the container
# COPY wait-for-it.sh /aqs_db_snapshot-2023-10-23/aqsproject/wait-for-it.sh

# Make the script executable
RUN chmod +x /aqs_db_snapshot-2023-10-23/aqsproject/wait-for-it.sh

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["timescaledb:5432", "--timeout=90", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

