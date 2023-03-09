__author__ = "Mohamed Morsy"
__credits__ = ["Mohamed Morsy"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Mohamed Morsy"
__email__ = "mohamedmorsyanwar@cu.edu.eg"
__status__ = "Production"

import arcpy
import glob, os

# working folder
working_folder = "C:/Users/Morsy/Desktop/In Progress/production"

# Set the input GA layer.
inputGALayer = "base_Kriging.lyr"

# beginning of the output file
b_o_f = "kriging_ord_sph_"

# type od data: MAXIMUM or TOTAL
d_type = "MAXIMUM"

# get all shapefiles in the working folder and print their length
l_shp = []
os.chdir(working_folder)
for file in glob.glob("*.shp"):
    l_shp.append(file)

len(l_shp)

# set working env for arcpy
arcpy.env.workspace = working_folder

# Check out Geostatistical Analyst extension license
arcpy.CheckExtension("GeoStats")

# run main program to loop through the shapefile and generate new interpolated layers and cross-validation shapeiles
for file in l_shp:
    # Set the new input dataset
    inputDset = file

    # output files name
    out_nam = b_o_f + file.split(".")[0] + "_" + d_type

    print(" Generating: ", out_nam)

    # Set output layer name
    outLayer = out_nam +".lyr"

    # Set the field name: There are two fields, MAXIMUM and TOTAL
    inputDset1 = inputDset + " " + d_type

    # create new Geostatisical layer from the base layer
    arcpy.GACreateGeostatisticalLayer_ga(inputGALayer,inputDset1, outLayer)
    arcpy.management.SaveToLayerFile(outLayer, "./output/" + out_nam + ".lyr")

    # print execution message
    print(arcpy.GetMessages())

    # generate cross validation
    arcpy.CrossValidation_ga(outLayer, "./output/" + out_nam + ".shp")

    print(" Done: ", out_nam)

