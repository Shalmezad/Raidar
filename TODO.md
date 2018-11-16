# Raidar
Raidar TODO list (until Github repo is up)

## Misc
  - [ ] Set up docker/docker-compose to spin up redis
  - [ ] Set up docker/docker-compose to spin up api
  - [ ] Set up docker/docker-compose to spin up web frontend
  - [ ] Set up docker/docker-compose to spin up image processor
  - [ ] Set up docker/docker-compose to spin up discord
  - [ ] Get a bunch of screenshots from discord for testing image processing
  - [ ] Get a bunch of screenshots from android for testing image processing

## Android
  - [X] Set up project
  - [ ] Add floating button
  - [ ] Take screenshot on floating button press
  - [ ] Present prompt to submit screenshot
  - [ ] Base64 encode screenshot
  - [ ] Post screenshot as json
  - [ ] Add screen info to json (resolution, dp scale)
  - [ ] Add GPS info to json

## API
  - [ ] Retrieve gym locations for area
  - [ ] Submit raid locations (admin only)
  - [ ] Submit raid images (post to redis)
  - [ ] Retrieve raids list for area
  - [ ] Add ongoing raids to gym list

## Web
  - [ ] Show map of area
  - [ ] Show gyms in area (call API)
  - [ ] Show raids in area (call API)

## Discord
  - [ ] Allow reporting of raids via !raid commands
  - [ ] Listen on redis for raid information (pubsub)
  - [ ] Gather raid images from dedicated channel (post to redis)

## Image processor
  - [ ] Poll redis for images
  - [ ] Get image
  - [ ] Identify image screen (egg, raid, gym, nearby-raid-tab, overview, etc)
  - [ ] Parse info from nearby-raid-tab (tensorflow? something else?)
