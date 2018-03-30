import glob

files_dir="C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/PianoRolls/"
read_files =  glob.glob("%s*.csv" %(files_dir))  
with open("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/PianoRolls/Result.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            print(f)
            outfile.write(infile.read())