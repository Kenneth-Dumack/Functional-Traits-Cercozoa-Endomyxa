#!/usr/bin/env python

# Script that connects PR2 Taxonomy output to functional trait data from Dumack et al. 2019
with open("output_filename.txt", "w") as out: #### this just defines the output file name; "w" means there is no headline
	with open("pr2_output_filename.txt", "r") as Taxonomy: #### this is the taxonomy file / database and gives it a name; "r" means there is a headline
		with open("FunctionalTraitsTable.txt", "r") as Function: ### this is the functional table and gives it a name; "r" means there is a headline
			GenusNutrition = {} ### define variables
			GenusMorphology = {} ### define variables
			GenusLocomotion = {} ### define variables
			GenusHabitat = {} ### define variables
			for line in Function:
				line = line.rstrip() #### Processes file by line. Note that if we call .rstrip() with no arguments, all white-space characters (including the newline character(s), spaces, and tabs) are stripped.
				line = line.split("\t") ### separator in file is "/t" (tabstops)
				GenusNutrition[line[6]] = line[7] ### binds value for genus and nutrition in one variable
				GenusMorphology[line[6]] = line[8] ### binds value for genus and morphology in one variable
				GenusLocomotion[line[6]] = line[9] ### binds value for genus and locomotion in one variable
				GenusHabitat[line[6]] = line[10] ### binds value for genus and habitat in one variable
			for row in Taxonomy:
				row = row.rstrip() #### Processes file by line. Note that if we call .rstrip() with no arguments, all white-space characters (including the newline character(s), spaces, and tabs) are stripped.
				row = row.split("\t") ### separator in file is "/t" (tabstops)
				rowConcat = "\t".join(row) ## joins rows
				if row[7] in GenusNutrition: ##### This is important, the number 7 depends on your own database file and must be changed to the number of the row in which your genus level taxonomy is written, python starts counting with 0
					Nutrition = GenusNutrition[row[7]] ## defines variables ##### This is important, the number 7 depends on your own database file and must be changed to the number of the row in which your genus level taxonomy is written
					Morphology = GenusMorphology[row[7]] ## defines variables ##### This is important, the number 7 depends on your own database file and must be changed to the number of the row in which your genus level taxonomy is written
					Locomotion = GenusLocomotion[row[7]] ## defines variables ##### This is important, the number 7 depends on your own database file and must be changed to the number of the row in which your genus level taxonomy is written
					Habitat = GenusHabitat[row[7]] ## defines variables ##### This is important, the number 7 depends on your own database file and must be changed to the number of the row in which your genus level taxonomy is written
					out.write(rowConcat + "\t" + Nutrition + "\t" + Morphology + "\t" + Locomotion + "\t" + Habitat + "\n") ## concatenates each row with the variables lifestyle and substrate and end of line 
				else:
					out.write(rowConcat + "\t" + "NA" + "\t" + "NA" + "\t" + "NA" + "\t" + "NA" + "\n") ## puts NA if there is a missing value 
