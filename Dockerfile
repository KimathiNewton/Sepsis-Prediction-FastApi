# Specifying the base image
FROM python:3.11

# Set the working directory to /Sepsis
WORKDIR /Sepsis
 
# Copy the current directory contents into the container at /Sepsis
COPY ./requirements.txt /Sepsis/requirements.txt
 
# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /Sepsis/requirements.txt
 
# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
 
# Set the working directory to the user's home directory
WORKDIR $HOME/app
 
# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app
 
# Start the FastAPI app on port 7860, the default port expected by Spaces
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"] 