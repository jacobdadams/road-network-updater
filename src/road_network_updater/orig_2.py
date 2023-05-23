'''
Notes on running this script:
1. Change the directory variable ('new_network_location') to point to the newest RecentsBuilds folder (variable >> new_network_location).
2. Make sure to use python-3 (or Desktop 10.6)
'''

# Name: NetworkDatasetTemplate_workflow.py
# Description: Create a new network dataset with the same schema as an existing
#               network dataset
# Requirements: Network Analysst Extension


import os

#Import system modules
import arcpy

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")

    #Set local variables
    ##original_network = "C:/data/Region1.gdb/Transportation/Streets_ND"
    new_network_location = "C:\\Users\\gbunce\\Documents\\projects\\NetworkDataset\\RecentBuilds\\2022_8_4\\UtahRoadsNetworkAnalysis.gdb\\NetworkDataset"
    xml_template = "C:\\Users\\gbunce\\Documents\\projects\\NetworkDataset\\agrc_network_template.xml"

    #Create an XML template from the original network dataset
    ##arcpy.na.CreateTemplateFromNetworkDataset(original_network, xml_template)

    #Create the new network dataset in the output location using the template.
    #The output location must already contain feature classes and tables with
    #the same names and schema as the original network.
    arcpy.na.CreateNetworkDatasetFromTemplate(xml_template, new_network_location)

    print(("done creating network, now building it"))

    #Build the new network dataset
    arcpy.na.BuildNetwork(os.path.join(new_network_location, "UtahRoadsNetwork"))

    print(("done building the network"))
    print(("done!"))

except Exception as e:
    # If an error occurred, print line number and error message
    import sys
    import traceback
    tb = sys.exc_info()[2]
    print(("An error occurred on line %i" % tb.tb_lineno))
    print((str(e)))
