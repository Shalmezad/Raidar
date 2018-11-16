# Raidar

An attempt to automate Pokemon Go raid information without violating Niantic's TOS

## Sub projects at a glance:

* *android* - The android app. This sits as a bubble that when pressed, grabs a screenshot and prompts to upload
* *api* - The api. This handles calls to fetch data (for the front end), or process data (from the android app)
* *discordbot* - Interacts with discord, reporting raids uploaded from the android app, and gathering raid information submitted manually via commands
* *frontend* - Front end for an interactive map website
* *imageprocessor* - Dedicated app for processing images for raid data

