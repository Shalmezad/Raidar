FROM python:3.6
WORKDIR /usr/src/app

# Install dependencies:
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# -u for unbuffered stdout
# See: https://stackoverflow.com/a/29745541
CMD [ "python", "-u" , "./raidar_discord/raidar_discord.py" ]
