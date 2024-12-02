# Purpose
- If you are using an AMP/DAC (I'm not sure what causes it), windows wont let you use master volume, only individual app volumes
- This program just checks the main volume, and sets every app volume equal to the master volume, Essentially emulating as if master volume worked

# Installation + Usage
- Download the .exe, or .py if thats your way to go
- Run the exe, it should run as a background process
- - You can test it by changing the volume and seeing if it changes properly
- And thats it, you're all setup!

# Known problems
- As of right now, the mute button wont work, since it doesnt listen for that
- - If you want the mute, you can download the py and uncomment line 17 and 18
- The volume can be quite jumpy, this is because of the 0.5 second timer to prevent heavy resource usage
- - if you want a more responsive program, you can download the py and edit the timings to your desire
- This program can be quite resource heavy while changing volume, be wary of that, little cost while idle though


#
- Made by me, @hermivore on discord ;3
- DM me for support (Discord), or just figure it out yourself, running the py will show the console
