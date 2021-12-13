#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# NWoodward, 2021-Dec-12, Added code under strChoice 'c' to handle tracks on an individual CD
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x': #Exit
        break
    if strChoice == 'l': #Load Inventory
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a': #Add CD
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd': #Display CD Inventory
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c': # Choose CD
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ').strip()
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            IO.ScreenIO.print_CD_menu()
            strchoice = IO.ScreenIO.menu_CD_choice()
            
            if strchoice == 'x': #Exit to main menu
                break
            if strchoice == 'a': #Add a track
                track = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(track, cd)
                IO.ScreenIO.show_tracks(cd)
            elif strchoice == 'd': #Display CD details
                IO.ScreenIO.show_tracks(cd)
            elif strchoice == 'r': #Remove a track
                IO.ScreenIO.show_tracks(cd)
                badtrack = input('Enter the track number you want to remove: ')
                cd.rmv_track(badtrack)
            else:
                print('General Error in CD sub menu.')
    elif strChoice == 's':  # Save CD Inventory to text file
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')