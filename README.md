# Utsushi's Charm

> Whenever I look at Utsushi I feel like I can do anything. Unfortunately, when I need to register my charms, I can't lose myself in Utsushi's charm.
> Fortunately, now, with Utsushi's charm, I can lose myself in Utsushi's charm for longer.
> 
> \- Utsushi Fan Girl, probably


This repo contains code that will allow you to extract all of your charms in Monster Hunter Rise from recordings taking with the switch's "save clip" feature.

It's called Utsushi's charm because I thought it would be funny to make a complementary "Utsushi's Armor Search System", but ["this armor set searcher exists"](https://mhrise.wiki-db.com/sim/?hl=en). I might still try to port Athena's ASS for MHW to MHR, but for now this works for me.

# Usage

## Requirements
- A computer (Windows) 
  - Linux and Mac might work too, you wont be able to run the EXE and will have to run from source in a terminal window.
- A USB cable to connect your switch to transfer files
- This latest version of this downloaded to your computer (Utsushis-Charm_**vx_x**.zip)
  - You can find it [here](https://github.com/chpoit/utsushis-charm/releases/latest)
- Some knowledge of how to type things in the terminal
  - AKA: Knowing how to type in a hacker box
- Being able to read


## Steps

0. Unequip all jewels. You will create "fake" charms otherwise.
   - Item Box -> Manage Equipment -> Set Decorations -> Equipment Box -> Remove all (Press '-' on controller)
   - Don't ask, this is way out of scope for something that takes you 30 seconds to do.
1. Download the release bundle and follow the Requirements section  (Utsushis-Charm_**vx_x**.zip)
   - Make sure you unzip everythin and you leave the files where they are.
   - You can delete the `tesseract-installer.exe` once it's installed  
2. Record clips similar to the following of you going through your charms. Try placing the UI in front of something that is very "flat" in color and doesn't have NPCs walking in front. 
   - I can easily go through 2-3 pages of charms in 30 seconds. 
   - Use a stopwatch on your phone if you have trouble timing the 30 seconds. I saved a clip every ~25 seconds.
   - Don't worry about passing over a charm multiple times. Duplicates will be removed at the end.

![Example Clip](./media/example_clip.gif)

3. Transfer the clips to your computer.
4. Put the files in the "inputs" directory. If it does not exist, create it at the same place you can find `utsushis-charm.exe` and `tesseract-installer.exe`
   - It does not matter how many you have 
   - I haven't tried to see what would happen if there are clips that are not of the charm UI
5. Run the `utsushis-charm.exe` (Double-click)
6. A Terminal should pop up
   - Wait a little bit, it need to some stuff (~5-15s) 
7. The first step of the program should take roughly 1 minute per clip you have in the inputs folder
8. Once that step is done, the second phase starts, normally, it should be done without needing your attention
   - Follow the instructions on screen and correct any invalid skill names.
   - If a skill has to be corrected, a window with the skill should open, you might have to alt-tab to it, Windows likes to hide it.
9. The program is done running. Press Enter and exit.
   - Sometimes tesseract is absolutely unable to read text, those charms will be logged in `app.log` and you can add them manually.
10. If no charm errored, or you don't care about those charms, you should be able to open the `charms.encoded.txt` file and copy the contents into the import box of [MHR-Wiki](https://mhrise.wiki-db.com/sim/?hl=en)




# Troubleshooting

If the program starts and closes without anything happening, open the `app.log` file and use this section to try and fix your issues

## Simple issues:
- 0 charms found
  - Make sure your clips are in the inputs folder
- I had to enter skill by hand but it wont accept it
  - You need to enter them one word at a time, it might only not know what one of the words is.
  - Make sure you are writing it exactly how it is shown on the picture that pops up
- I get through the First phase, but it stops when checking the first frame of
  - This is an issue with Tesseract not being installed. Check the next bullet point.
- Google Tesseract is not installed/not found
  - Make sure you installed it. You might have to reboot
  - Try adding it manually to the path
    - Potential Locations:
      -  `C:\Program Files\Tesseract-OCR` (Most likely, if you chose "Install for anyone")
      -  `C:\Users\<USERNAME>\AppData\Local\Tesseract-OCR` (If you chose "Install only for me")
      -  `C:\Program Files (x86)\Tesseract-OCR` (Version 4, less likely, would happen if you manually downloaded a 32bit installer)
  -  It seems really random wether it'll add it to path. If there is a request for it, I might add a "bruteforce" method to find the exe so people don't have to worry about this.
- Any other issue:
  - Consider creating a bug report [here](https://github.com/chpoit/utsushis-charm/issues/new)

## Adding something to the path (Windows)

1. Copy the path to the executable (Where the program was installed)
   - Don't put the executable file in the path, only where it is located
2. type `env` in the Windows search bar
   - Alternatively type `Edit environment variables for your account`
3. Press Enter
4. Click on `Environment Variables`
5. In `User Variables`, select `Path`
6. Click `Edit`
7. Click `New`
8. Paste the path you copied previously in the new spot.
9. Click `Ok/Apply` for every window you opened.
10. Restart every terminal/command line, or reboot to make sure you'll have access to the new commands

# Contribute

- If you feel like contributing anything, go ahead and submit a pull request I'll be happy to take a look and decide if it's something worth adding. 

# TODOS: 
- [ ] Throw out Google Tesseract/Try newer version
  - Version 4 works great, this is going on the back burner for a while
  - Version 3 has trouble with quite a few words (Slugger, Recovery, Earplugs, Counterstrike, Maestro, etc.)
  - I'm considering going full monkey brain and having one "mask" per skill like I'm doing for the slots and skill levels.
  - The monkey brain approach would probably make it so this can be run completely unattended, at the cost of some extra storage space.
  - Monkey brain results:
    - Monkey brain is less accurate
    - Tesseract 4 works great
    - Need to do some "pixel poking" to make sure everything is lined up the same
- [ ] Solution for people that don't want to bother with the hassle
- [ ] Make the code not a mess
- [x] Use the page number in the "Is the last frame the same" check. (Low priority, charms still seem to get detected on page swap)
- [ ] Docker image for deployment?
- [ ] UI
- [ ] Multithreading for some of that SPEEEEED
- Get images for the following skills:
  - Likely Possible
    - Ammo Up
    - Attack Boost
    - Blast Resistance
    - Bow Charge Plus
    - Capture Master
    - Critical Draw
    - Guard
    - Guard Up
    - Handicraft
    - Load Shells
    - Marathon Runner
    - Maximum Might
    - Mushroomancer
    - Normal/Rapid Up
    - Offensive Guard
    - Pierce Up
    - Rapid Fire Up
    - Stamina Surge
    - Wall Runner ---
  - Likely not Possible
    - Good Luck
    - Carving Master -> Arena headpiece
    - Chameleos Blessing
    - Kushala Blessing
    - Thunder Alignment
    - Teostra Blessing
    - Wind Alignment

# Extra maintenance (Dev)

To rebuild the js2py file with the extracted encoder from mhr-wiki:
- babel .\js_encoder.js -o converted.js
- python -c "import js2py; js2py.translate_file('converted.js', 'py_encoder.py')"
- babel .\js_encoder.js -o converted.js && python -c "import js2py; js2py.translate_file('converted.js', 'py_encoder.py')"

# Building the executable
Run the `scripts\build_release.bat` file. You will need to have 7zip in path.

# Extra command line options
If you run from source, or call the executable from the terminal you can make use of the following flags/arguments to achieve different functionality

- `-h` or ` --help`: Shows arguments
- `--thirdparty `: Shows 3rd party licenses
- `--skip-frames`: Skips the first frame extraction step. Useful if the second step crashed.
- ` --skip-charms`:`Skips the Tesseract-OCR step. Not sure why you would want that.
- `-i <INPUT_DIR>` or `--input <INPUT_DIR>`: Changes the Input directory for videos
- `-f <FRAME_DIR>` or `--frames <FRAME_DIR>`: Changes the Directory used to store temporary frames