import pandas as pd
#import arcpy
import os
#input_excel = arcpy.GetParameterAsText(0)
input_excel = "D:\\Shaheryar\\KeyCodeandSummary\\AUGUST\\23-8-2021\\LIWA 3 Sectors (New)\\forms"
input_excel.replace(" ", "")
#SurveyID = arcpy.GetParameterAsText(1)
#Enviroment = arcpy.GetParameterAsText(2)
#path = "D:\\Shaheryar\\KeyCodeandSummary\\E90\\REV_01\\PCI_FORMS"
#path.replace(" ","")
dirs = os.listdir(input_excel)
#Enviroment.replace(" ", "")

sub = pd.DataFrame(columns=['OBJECTID','SURVEY_ID','PMS_CHAINAGE_START','PMS_CHAINAGE_END','SURVEY_CHAINAGE_START','SURVEY_CHAINAGE_END','PCI_VALUE','PCI_RATING','LANE_WIDTH','ALLIGATOR_L','ALLIGATOR_L_DV','ALLIGATOR_M','ALLIGATOR_M_DV','ALLIGATOR_H','ALLIGATOR_H_DV','BLEED_L','BLEED_L_DV','BLEED_M','BLEED_M_DV','BLEED_H','BLEED_H_DV','BLOCK_L','BLOCK_L_DV','BLOCK_M','BLOCK_M_DV','BLOCK_H','BLOCK_H_DV','BUMP_L','BUMP_L_DV','BUMP_M','BUMP_M_DV','BUMP_H','BUMP_H_DV','CORRUGATION_L','CORRUGATION_L_DV','CORRUGATION_M','CORRUGATION_M_DV','CORRUGATION_H','CORRUGATION_H_DV','DEPRESSION_L','DEPRESSION_L_DV','DEPRESSION_M','DEPRESSION_M_DV','DEPRESSION_H','DEPRESSION_H_DV','EDGE_L','EDGE_L_DV','EDGE_M','EDGE_M_DV','EDGE_H','EDGE_H_DV','REFLECTION_L','REFLECTION_L_DV','REFLECTION_M','REFLECTION_M_DV','REFLECTION_H','REFLECTION_H_DV','LANEDROP_L','LANEDROP_L_DV','LANEDROP_M','LANEDROP_M_DV','LANEDROP_H','LANEDROP_H_DV','LONG_L','LONG_L_DV','LONG_M','LONG_M_DV','LONG_H','LONG_H_DV','PATCH_L','PATCH_L_DV','PATCH_M','PATCH_M_DV','PATCH_H','PATCH_H_DV','POLAG_L','POLAG_L_DV','POLAG_M','POLAG_M_DV','POLAG_H','POLAG_H_DV','POTHOL_L','POTHOL_L_DV','POTHOL_M','POTHOL_M_DV','POTHOL_H','POTHOL_H_DV','RAIL_L','RAIL_L_DV','RAIL_M','RAIL_M_DV','RAIL_H','RAIL_H_DV','RUTTING_L','RUTTING_L_DV','RUTTING_M','RUTTING_M_DV','RUTTING_H','RUTTING_H_DV','SHOVING_L','SHOVING_L_DV','SHOVING_M','SHOVING_M_DV','SHOVING_H','SHOVING_H_DV','SLIPCRACK_L','SLIPCRACK_L_DV','SLIPCRACK_M','SLIPCRACK_M_DV','SLIPCRACK_H','SLIPCRACK_H_DV','SWELL_L','SWELL_L_DV','SWELL_M','SWELL_M_DV','SWELL_H','SWELL_H_DV','RAVEL_L','RAVEL_L_DV','RAVEL_M','RAVEL_M_DV','RAVEL_H','RAVEL_H_DV','WEATHERING_L','WEATHERING_L_DV','WEATHERING_M','WEATHERING_M_DV','WEATHERING_H','WEATHERING_H_DV','REMARKS','LINK'])
sub1 = pd.DataFrame(columns=['OBJECTID','SURVEY_ID','PMS_CHAINAGE_START','PMS_CHAINAGE_END','SURVEY_CHAINAGE_START','SURVEY_CHAINAGE_END','PCI_VALUE','PCI_RATING','LANE_WIDTH','ALLIGATOR_L','ALLIGATOR_L_DV','ALLIGATOR_M','ALLIGATOR_M_DV','ALLIGATOR_H','ALLIGATOR_H_DV','BLEED_L','BLEED_L_DV','BLEED_M','BLEED_M_DV','BLEED_H','BLEED_H_DV','BLOCK_L','BLOCK_L_DV','BLOCK_M','BLOCK_M_DV','BLOCK_H','BLOCK_H_DV','BUMP_L','BUMP_L_DV','BUMP_M','BUMP_M_DV','BUMP_H','BUMP_H_DV','CORRUGATION_L','CORRUGATION_L_DV','CORRUGATION_M','CORRUGATION_M_DV','CORRUGATION_H','CORRUGATION_H_DV','DEPRESSION_L','DEPRESSION_L_DV','DEPRESSION_M','DEPRESSION_M_DV','DEPRESSION_H','DEPRESSION_H_DV','EDGE_L','EDGE_L_DV','EDGE_M','EDGE_M_DV','EDGE_H','EDGE_H_DV','REFLECTION_L','REFLECTION_L_DV','REFLECTION_M','REFLECTION_M_DV','REFLECTION_H','REFLECTION_H_DV','LANEDROP_L','LANEDROP_L_DV','LANEDROP_M','LANEDROP_M_DV','LANEDROP_H','LANEDROP_H_DV','LONG_L','LONG_L_DV','LONG_M','LONG_M_DV','LONG_H','LONG_H_DV','PATCH_L','PATCH_L_DV','PATCH_M','PATCH_M_DV','PATCH_H','PATCH_H_DV','POLAG_L','POLAG_L_DV','POLAG_M','POLAG_M_DV','POLAG_H','POLAG_H_DV','POTHOL_L','POTHOL_L_DV','POTHOL_M','POTHOL_M_DV','POTHOL_H','POTHOL_H_DV','RAIL_L','RAIL_L_DV','RAIL_M','RAIL_M_DV','RAIL_H','RAIL_H_DV','RUTTING_L','RUTTING_L_DV','RUTTING_M','RUTTING_M_DV','RUTTING_H','RUTTING_H_DV','SHOVING_L','SHOVING_L_DV','SHOVING_M','SHOVING_M_DV','SHOVING_H','SHOVING_H_DV','SLIPCRACK_L','SLIPCRACK_L_DV','SLIPCRACK_M','SLIPCRACK_M_DV','SLIPCRACK_H','SLIPCRACK_H_DV','SWELL_L','SWELL_L_DV','SWELL_M','SWELL_M_DV','SWELL_H','SWELL_H_DV','RAVEL_L','RAVEL_L_DV','RAVEL_M','RAVEL_M_DV','RAVEL_H','RAVEL_H_DV','WEATHERING_L','WEATHERING_L_DV','WEATHERING_M','WEATHERING_M_DV','WEATHERING_H','WEATHERING_H_DV','REMARKS','LINK'])
sub2 = pd.DataFrame(columns=['OBJECTID','SURVEY_ID','PMS_CHAINAGE_START','PMS_CHAINAGE_END','SURVEY_CHAINAGE_START','SURVEY_CHAINAGE_END','PCI_VALUE','PCI_RATING','LANE_WIDTH','ALLIGATOR_L','ALLIGATOR_L_DV','ALLIGATOR_M','ALLIGATOR_M_DV','ALLIGATOR_H','ALLIGATOR_H_DV','BLEED_L','BLEED_L_DV','BLEED_M','BLEED_M_DV','BLEED_H','BLEED_H_DV','BLOCK_L','BLOCK_L_DV','BLOCK_M','BLOCK_M_DV','BLOCK_H','BLOCK_H_DV','BUMP_L','BUMP_L_DV','BUMP_M','BUMP_M_DV','BUMP_H','BUMP_H_DV','CORRUGATION_L','CORRUGATION_L_DV','CORRUGATION_M','CORRUGATION_M_DV','CORRUGATION_H','CORRUGATION_H_DV','DEPRESSION_L','DEPRESSION_L_DV','DEPRESSION_M','DEPRESSION_M_DV','DEPRESSION_H','DEPRESSION_H_DV','EDGE_L','EDGE_L_DV','EDGE_M','EDGE_M_DV','EDGE_H','EDGE_H_DV','REFLECTION_L','REFLECTION_L_DV','REFLECTION_M','REFLECTION_M_DV','REFLECTION_H','REFLECTION_H_DV','LANEDROP_L','LANEDROP_L_DV','LANEDROP_M','LANEDROP_M_DV','LANEDROP_H','LANEDROP_H_DV','LONG_L','LONG_L_DV','LONG_M','LONG_M_DV','LONG_H','LONG_H_DV','PATCH_L','PATCH_L_DV','PATCH_M','PATCH_M_DV','PATCH_H','PATCH_H_DV','POLAG_L','POLAG_L_DV','POLAG_M','POLAG_M_DV','POLAG_H','POLAG_H_DV','POTHOL_L','POTHOL_L_DV','POTHOL_M','POTHOL_M_DV','POTHOL_H','POTHOL_H_DV','RAIL_L','RAIL_L_DV','RAIL_M','RAIL_M_DV','RAIL_H','RAIL_H_DV','RUTTING_L','RUTTING_L_DV','RUTTING_M','RUTTING_M_DV','RUTTING_H','RUTTING_H_DV','SHOVING_L','SHOVING_L_DV','SHOVING_M','SHOVING_M_DV','SHOVING_H','SHOVING_H_DV','SLIPCRACK_L','SLIPCRACK_L_DV','SLIPCRACK_M','SLIPCRACK_M_DV','SLIPCRACK_H','SLIPCRACK_H_DV','SWELL_L','SWELL_L_DV','SWELL_M','SWELL_M_DV','SWELL_H','SWELL_H_DV','RAVEL_L','RAVEL_L_DV','RAVEL_M','RAVEL_M_DV','RAVEL_H','RAVEL_H_DV','WEATHERING_L','WEATHERING_L_DV','WEATHERING_M','WEATHERING_M_DV','WEATHERING_H','WEATHERING_H_DV','REMARKS','LINK'])
sub3 = pd.DataFrame(columns=['OBJECTID','SURVEY_ID','PMS_CHAINAGE_START','PMS_CHAINAGE_END','SURVEY_CHAINAGE_START','SURVEY_CHAINAGE_END','PCI_VALUE','PCI_RATING','LANE_WIDTH','ALLIGATOR_L','ALLIGATOR_L_DV','ALLIGATOR_M','ALLIGATOR_M_DV','ALLIGATOR_H','ALLIGATOR_H_DV','BLEED_L','BLEED_L_DV','BLEED_M','BLEED_M_DV','BLEED_H','BLEED_H_DV','BLOCK_L','BLOCK_L_DV','BLOCK_M','BLOCK_M_DV','BLOCK_H','BLOCK_H_DV','BUMP_L','BUMP_L_DV','BUMP_M','BUMP_M_DV','BUMP_H','BUMP_H_DV','CORRUGATION_L','CORRUGATION_L_DV','CORRUGATION_M','CORRUGATION_M_DV','CORRUGATION_H','CORRUGATION_H_DV','DEPRESSION_L','DEPRESSION_L_DV','DEPRESSION_M','DEPRESSION_M_DV','DEPRESSION_H','DEPRESSION_H_DV','EDGE_L','EDGE_L_DV','EDGE_M','EDGE_M_DV','EDGE_H','EDGE_H_DV','REFLECTION_L','REFLECTION_L_DV','REFLECTION_M','REFLECTION_M_DV','REFLECTION_H','REFLECTION_H_DV','LANEDROP_L','LANEDROP_L_DV','LANEDROP_M','LANEDROP_M_DV','LANEDROP_H','LANEDROP_H_DV','LONG_L','LONG_L_DV','LONG_M','LONG_M_DV','LONG_H','LONG_H_DV','PATCH_L','PATCH_L_DV','PATCH_M','PATCH_M_DV','PATCH_H','PATCH_H_DV','POLAG_L','POLAG_L_DV','POLAG_M','POLAG_M_DV','POLAG_H','POLAG_H_DV','POTHOL_L','POTHOL_L_DV','POTHOL_M','POTHOL_M_DV','POTHOL_H','POTHOL_H_DV','RAIL_L','RAIL_L_DV','RAIL_M','RAIL_M_DV','RAIL_H','RAIL_H_DV','RUTTING_L','RUTTING_L_DV','RUTTING_M','RUTTING_M_DV','RUTTING_H','RUTTING_H_DV','SHOVING_L','SHOVING_L_DV','SHOVING_M','SHOVING_M_DV','SHOVING_H','SHOVING_H_DV','SLIPCRACK_L','SLIPCRACK_L_DV','SLIPCRACK_M','SLIPCRACK_M_DV','SLIPCRACK_H','SLIPCRACK_H_DV','SWELL_L','SWELL_L_DV','SWELL_M','SWELL_M_DV','SWELL_H','SWELL_H_DV','RAVEL_L','RAVEL_L_DV','RAVEL_M','RAVEL_M_DV','RAVEL_H','RAVEL_H_DV','WEATHERING_L','WEATHERING_L_DV','WEATHERING_M','WEATHERING_M_DV','WEATHERING_H','WEATHERING_H_DV','REMARKS','LINK'])
iter = 1
itera = 1
try:
    
    for file in dirs:
        print(file)
        #arcpy.AddMessage(file)
        fx= pd.ExcelFile(input_excel+"\\"+file)
        for a in range(9,len(fx.sheet_names)):



            f1= pd.read_excel(input_excel+"\\"+file,index_col = None, header= None,sheet_name = a)

            PMS_start = f1.iloc[24,3]
            PMS_CHAINAGE = sub.at[iter,'PMS_CHAINAGE_START']= PMS_start
            PMS_CHAINAGE = str(PMS_CHAINAGE)
            PMS_CHAINAGE = PMS_CHAINAGE.replace('.0','')

            PMS_end = f1.iloc[24,6]          
            PMS_CHAINAGE_END = sub.at[iter,'PMS_CHAINAGE_END']= PMS_end
            PMS_CHAINAGE_END = str(PMS_CHAINAGE_END)
            PMS_CHAINAGE_END = PMS_CHAINAGE_END.replace('.0','')

            Survey_start = f1.iloc[25,3]
            SURVEY_CHAINAGE = sub.at[iter,'SURVEY_CHAINAGE_START']=  Survey_start
            SURVEY_CHAINAGE = str(SURVEY_CHAINAGE)
            SURVEY_CHAINAGE = SURVEY_CHAINAGE.replace('.0','')

            Survey_end = f1.iloc[25,6]          
            SURVEY_CHAINAGE_END = sub.at[iter,'SURVEY_CHAINAGE_END']= Survey_end
            SURVEY_CHAINAGE_END = str(SURVEY_CHAINAGE_END)
            SURVEY_CHAINAGE_END = SURVEY_CHAINAGE_END.replace('.0','')



            Survey = f1.iloc[5,10]
            sub.at[iter,'PCI_RATING']=f1.iloc[42,6]
            sub.at[iter,'LANE_WIDTH']=f1.iloc[12,4]

            sub.at[iter,'SURVEY_ID']= Survey
            link = sub.at[iter,'LINK']= str(Survey)+'_'+str(PMS_CHAINAGE)
            sub.at[iter,'PCI_VALUE']=f1.iloc[42,3]

            Distress_1 = f1.iloc[26,2]
            Distress_1l = f1.iloc[27,2]
            Distress_1m = f1.iloc[28,2]
            Distress_1h = f1.iloc[29,2]
            Distress_1_dvl = f1.iloc[35,2]
            Distress_1_dvm = f1.iloc[36,2]
            Distress_1_dvh = f1.iloc[37,2]

            Distress_2 = f1.iloc[26,3]
            Distress_2l = f1.iloc[27,3]
            Distress_2m = f1.iloc[28,3]
            Distress_2h = f1.iloc[29,3]
            Distress_2_dvl = f1.iloc[35,3]
            Distress_2_dvm = f1.iloc[36,3]
            Distress_2_dvh = f1.iloc[37,3]


            Distress_3 = f1.iloc[26,4]
            Distress_3l = f1.iloc[27,4]
            Distress_3m = f1.iloc[28,4]
            Distress_3h = f1.iloc[29,4]
            Distress_3_dvl = f1.iloc[35,4]
            Distress_3_dvm = f1.iloc[36,4]
            Distress_3_dvh = f1.iloc[37,4]



            Distress_4 = f1.iloc[26,5]
            Distress_4l = f1.iloc[27,5]
            Distress_4m = f1.iloc[28,5]
            Distress_4h = f1.iloc[29,5]
            Distress_4_dvl = f1.iloc[35,5]
            Distress_4_dvm = f1.iloc[36,5]
            Distress_4_dvh = f1.iloc[37,5]



            Distress_5 = f1.iloc[26,6]
            Distress_5l = f1.iloc[27,6]
            Distress_5m = f1.iloc[28,6]
            Distress_5h = f1.iloc[29,6]
            Distress_5_dvl = f1.iloc[35,6]
            Distress_5_dvm = f1.iloc[36,6]
            Distress_5_dvh = f1.iloc[37,6]



            if Distress_1 == 1:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'ALLIGATOR_L']=f1.iloc[27,2]
                    sub.at[iter,'ALLIGATOR_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'ALLIGATOR_M']=f1.iloc[28,2]
                    sub.at[iter,'ALLIGATOR_M_DV']=f1.iloc[36,2]
                if Distress_1_dvh >= 0:
                    sub.at[iter,'ALLIGATOR_H']=f1.iloc[29,2]
                    sub.at[iter,'ALLIGATOR_H_DV']=f1.iloc[37,2] 

            if Distress_1 == 2:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'BLEED_L']=f1.iloc[27,2]
                    sub.at[iter,'BLEED_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'BLEED_M']=f1.iloc[28,2]
                    sub.at[iter,'BLEED_M_DV']=f1.iloc[36,2]   
                if Distress_1_dvh >= 0:
                    sub.at[iter,'BLEED_H']=f1.iloc[29,2]
                    sub.at[iter,'BLEED_H_DV']=f1.iloc[37,2]

            if Distress_1 == 3:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'BLOCK_L']=f1.iloc[27,2]
                    sub.at[iter,'BLOCK_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'BLOCK_M']=f1.iloc[28,2]
                    sub.at[iter,'BLOCK_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'BLOCK_H']=f1.iloc[29,2]
                    sub.at[iter,'BLOCK_H_DV']=f1.iloc[37,2]


            if Distress_1 == 4:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'BUMP_L']=f1.iloc[27,2]
                    sub.at[iter,'BUMP_L']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'BUMP_M']=f1.iloc[28,2]
                    sub.at[iter,'BUMP_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'BUMP_H']=f1.iloc[29,2]
                    sub.at[iter,'BUMP_H_DV']=f1.iloc[37,2]
            if Distress_1 == 5:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'CORRUGATION_L']=f1.iloc[27,2]
                    sub.at[iter,'CORRUGATION_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'CORRUGATION_M']=f1.iloc[28,2]
                    sub.at[iter,'CORRUGATION_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'CORRUGATION_H']=f1.iloc[29,2]
                    sub.at[iter,'CORRUGATION_H_DV']=f1.iloc[37,2]
            if Distress_1 == 6:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'DEPRESSION_L']=f1.iloc[27,2]
                    sub.at[iter,'DEPRESSION_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'DEPRESSION_M']=f1.iloc[28,2]
                    sub.at[iter,'DEPRESSION_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'DEPRESSION_H']=f1.iloc[29,2]
                    sub.at[iter,'DEPRESSION_H_DV']=f1.iloc[37,2]
            if Distress_1 == 7:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'EDGE_L']=f1.iloc[27,2]
                    sub.at[iter,'EDGE_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'EDGE_M']=f1.iloc[28,2]
                    sub.at[iter,'EDGE_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'EDGE_H']=f1.iloc[29,2]
                    sub.at[iter,'EDGE_H_DV']=f1.iloc[37,2]
            if Distress_1 == 8:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'REFLECTION_L']=f1.iloc[27,2]
                    sub.at[iter,'REFLECTION_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'REFLECTION_M']=f1.iloc[28,2]
                    sub.at[iter,'REFLECTION_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'REFLECTION_H']=f1.iloc[29,2]
                    sub.at[iter,'REFLECTION_H_DV']=f1.iloc[37,2]
            if Distress_1 == 9:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'LANEDROP_L']=f1.iloc[27,2]
                    sub.at[iter,'LANEDROP_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'LANEDROP_M']=f1.iloc[28,2]
                    sub.at[iter,'LANEDROP_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'LANEDROP_H']=f1.iloc[29,2]
                    sub.at[iter,'LANEDROP_H_DV']=f1.iloc[37,2]

            if Distress_1 == 10:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'LONG_L']=f1.iloc[27,2]
                    sub.at[iter,'LONG_L_DV']=f1.iloc[35,2]

                if Distress_1_dvm >= 0:
                    sub.at[iter,'LONG_M']=f1.iloc[28,2]
                    sub.at[iter,'LONG_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'LONG_H']=f1.iloc[29,2]
                    sub.at[iter,'LONG_H_DV']=f1.iloc[37,2]


            if Distress_1 == 11:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'PATCH_L']=f1.iloc[27,2]
                    sub.at[iter,'PATCH_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'PATCH_M']=f1.iloc[28,2]
                    sub.at[iter,'PATCH_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'PATCH_H']=f1.iloc[29,2]
                    sub.at[iter,'PATCH_H_DV']=f1.iloc[37,2]
            if Distress_1 == 12:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'POLAG_L']=f1.iloc[27,2]
                    sub.at[iter,'POLAG_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'POLAG_M']=f1.iloc[28,2]
                    sub.at[iter,'POLAG_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'POLAG_H']=f1.iloc[29,2]
                    sub.at[iter,'POLAG_H_DV']=f1.iloc[37,2]
            if Distress_1 == 13:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'POTHOL_L']=f1.iloc[27,2]
                    sub.at[iter,'POTHOL_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'POTHOL_M']=f1.iloc[28,2]
                    sub.at[iter,'POTHOL_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'POTHOL_H']=f1.iloc[29,2]
                    sub.at[iter,'POTHOL_H_DV']=f1.iloc[37,2]

            if Distress_1 == 14:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'RAIL_L']=f1.iloc[27,2]
                    sub.at[iter,'RAIL_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'RAIL_M']=f1.iloc[28,2]
                    sub.at[iter,'RAIL_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'RAIL_H']=f1.iloc[29,2]
                    sub.at[iter,'RAIL_H_DV']=f1.iloc[37,2]
            if Distress_1 == 15:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'RUTTING_L']=f1.iloc[27,2]
                    sub.at[iter,'RUTTING_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'RUTTING_M']=f1.iloc[28,2]
                    sub.at[iter,'RUTTING_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'RUTTING_H']=f1.iloc[29,2]
                    sub.at[iter,'RUTTING_H_DV']=f1.iloc[37,2]
            if Distress_1 == 16:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'SHOVING_L']=f1.iloc[27,2]
                    sub.at[iter,'SHOVING_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'SHOVING_M']=f1.iloc[28,2]
                    sub.at[iter,'SHOVING_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'SHOVING_H']=f1.iloc[29,2]
                    sub.at[iter,'SHOVING_H_DV']=f1.iloc[37,2]
            if Distress_1 == 17:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'SLIPCRACK_L']=f1.iloc[27,2]
                    sub.at[iter,'SLIPCRACK_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'SLIPCRACK_M']=f1.iloc[28,2]
                    sub.at[iter,'SLIPCRACK_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'SLIPCRACK_H']=f1.iloc[29,2]
                    sub.at[iter,'SLIPCRACK_H_DV']=f1.iloc[37,2]
            if Distress_1 == 18:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'SWELL_L']=f1.iloc[27,2]
                    sub.at[iter,'SWELL_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'SWELL_M']=f1.iloc[28,2]
                    sub.at[iter,'SWELL_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'SWELL_H']=f1.iloc[29,2]
                    sub.at[iter,'SWELL_H_DV']=f1.iloc[37,2]
            if Distress_1 == 19:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'RAVEL_L']=f1.iloc[27,2]
                    sub.at[iter,'RAVEL_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'RAVEL_M']=f1.iloc[28,2]
                    sub.at[iter,'RAVEL_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'RAVEL_H']=f1.iloc[29,2]
                    sub.at[iter,'RAVEL_H_DV']=f1.iloc[37,2]
            if Distress_1 == 20:
                if Distress_1_dvl >= 0:
                    sub.at[iter,'WEATHERING_L']=f1.iloc[27,2]
                    sub.at[iter,'WEATHERING_L_DV']=f1.iloc[35,2]
                if Distress_1_dvm >= 0:
                    sub.at[iter,'WEATHERING_M']=f1.iloc[28,2]
                    sub.at[iter,'WEATHERING_M_DV']=f1.iloc[36,2] 
                if Distress_1_dvh >= 0:
                    sub.at[iter,'WEATHERING_H']=f1.iloc[29,2]
                    sub.at[iter,'WEATHERING_H_DV']=f1.iloc[37,2]

            if Distress_2 == 1:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'ALLIGATOR_L']=f1.iloc[27,3]
                    sub.at[iter,'ALLIGATOR_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'ALLIGATOR_M']=f1.iloc[28,3]
                    sub.at[iter,'ALLIGATOR_M_DV']=f1.iloc[36,3]
                if Distress_2_dvh >= 0:
                    sub.at[iter,'ALLIGATOR_H']=f1.iloc[29,3]
                    sub.at[iter,'ALLIGATOR_H_DV']=f1.iloc[37,3] 

            if Distress_2 == 2:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'BLEED_L']=f1.iloc[27,3]
                    sub.at[iter,'BLEED_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'BLEED_M']=f1.iloc[28,3]
                    sub.at[iter,'BLEED_M_DV']=f1.iloc[36,3]   
                if Distress_2_dvh >= 0:
                    sub.at[iter,'BLEED_H']=f1.iloc[29,3]
                    sub.at[iter,'BLEED_H_DV']=f1.iloc[37,3]

            if Distress_2 == 3:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'BLOCK_L']=f1.iloc[27,3]
                    sub.at[iter,'BLOCK_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'BLOCK_M']=f1.iloc[28,3]
                    sub.at[iter,'BLOCK_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'BLOCK_H']=f1.iloc[29,3]
                    sub.at[iter,'BLOCK_H_DV']=f1.iloc[37,3]


            if Distress_2 == 4:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'BUMP_L']=f1.iloc[27,3]
                    sub.at[iter,'BUMP_L']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'BUMP_M']=f1.iloc[28,3]
                    sub.at[iter,'BUMP_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'BUMP_H']=f1.iloc[29,3]
                    sub.at[iter,'BUMP_H_DV']=f1.iloc[37,3]
            if Distress_2 == 5:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'CORRUGATION_L']=f1.iloc[27,3]
                    sub.at[iter,'CORRUGATION_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'CORRUGATION_M']=f1.iloc[28,3]
                    sub.at[iter,'CORRUGATION_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'CORRUGATION_H']=f1.iloc[29,3]
                    sub.at[iter,'CORRUGATION_H_DV']=f1.iloc[37,3]
            if Distress_2 == 6:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'DEPRESSION_L']=f1.iloc[27,3]
                    sub.at[iter,'DEPRESSION_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'DEPRESSION_M']=f1.iloc[28,3]
                    sub.at[iter,'DEPRESSION_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'DEPRESSION_H']=f1.iloc[29,3]
                    sub.at[iter,'DEPRESSION_H_DV']=f1.iloc[37,3]
            if Distress_2 == 7:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'EDGE_L']=f1.iloc[27,3]
                    sub.at[iter,'EDGE_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'EDGE_M']=f1.iloc[28,3]
                    sub.at[iter,'EDGE_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'EDGE_H']=f1.iloc[29,3]
                    sub.at[iter,'EDGE_H_DV']=f1.iloc[37,3]
            if Distress_2 == 8:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'REFLECTION_L']=f1.iloc[27,3]
                    sub.at[iter,'REFLECTION_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'REFLECTION_M']=f1.iloc[28,3]
                    sub.at[iter,'REFLECTION_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'REFLECTION_H']=f1.iloc[29,3]
                    sub.at[iter,'REFLECTION_H_DV']=f1.iloc[37,3]
            if Distress_2 == 9:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'LANEDROP_L']=f1.iloc[27,3]
                    sub.at[iter,'LANEDROP_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'LANEDROP_M']=f1.iloc[28,3]
                    sub.at[iter,'LANEDROP_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'LANEDROP_H']=f1.iloc[29,3]
                    sub.at[iter,'LANEDROP_H_DV']=f1.iloc[37,3]

            if Distress_2 == 10:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'LONG_L']=f1.iloc[27,3]
                    sub.at[iter,'LONG_L_DV']=f1.iloc[35,3]

                if Distress_2_dvm >= 0:
                    sub.at[iter,'LONG_M']=f1.iloc[28,3]
                    sub.at[iter,'LONG_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'LONG_H']=f1.iloc[29,3]
                    sub.at[iter,'LONG_H_DV']=f1.iloc[37,3]


            if Distress_2 == 11:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'PATCH_L']=f1.iloc[27,3]
                    sub.at[iter,'PATCH_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'PATCH_M']=f1.iloc[28,3]
                    sub.at[iter,'PATCH_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'PATCH_H']=f1.iloc[29,3]
                    sub.at[iter,'PATCH_H_DV']=f1.iloc[37,3]
            if Distress_2 == 12:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'POLAG_L']=f1.iloc[27,3]
                    sub.at[iter,'POLAG_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'POLAG_M']=f1.iloc[28,3]
                    sub.at[iter,'POLAG_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'POLAG_H']=f1.iloc[29,3]
                    sub.at[iter,'POLAG_H_DV']=f1.iloc[37,3]
            if Distress_2 == 13:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'POTHOL_L']=f1.iloc[27,3]
                    sub.at[iter,'POTHOL_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'POTHOL_M']=f1.iloc[28,3]
                    sub.at[iter,'POTHOL_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'POTHOL_H']=f1.iloc[29,3]
                    sub.at[iter,'POTHOL_H_DV']=f1.iloc[37,3]

            if Distress_2 == 14:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'RAIL_L']=f1.iloc[27,3]
                    sub.at[iter,'RAIL_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'RAIL_M']=f1.iloc[28,3]
                    sub.at[iter,'RAIL_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'RAIL_H']=f1.iloc[29,3]
                    sub.at[iter,'RAIL_H_DV']=f1.iloc[37,3]
            if Distress_2 == 15:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'RUTTING_L']=f1.iloc[27,3]
                    sub.at[iter,'RUTTING_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'RUTTING_M']=f1.iloc[28,3]
                    sub.at[iter,'RUTTING_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'RUTTING_H']=f1.iloc[29,3]
                    sub.at[iter,'RUTTING_H_DV']=f1.iloc[37,3]
            if Distress_2 == 16:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'SHOVING_L']=f1.iloc[27,3]
                    sub.at[iter,'SHOVING_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'SHOVING_M']=f1.iloc[28,3]
                    sub.at[iter,'SHOVING_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'SHOVING_H']=f1.iloc[29,3]
                    sub.at[iter,'SHOVING_H_DV']=f1.iloc[37,3]
            if Distress_2 == 17:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'SLIPCRACK_L']=f1.iloc[27,3]
                    sub.at[iter,'SLIPCRACK_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'SLIPCRACK_M']=f1.iloc[28,3]
                    sub.at[iter,'SLIPCRACK_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'SLIPCRACK_H']=f1.iloc[29,3]
                    sub.at[iter,'SLIPCRACK_H_DV']=f1.iloc[37,3]
            if Distress_2 == 18:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'SWELL_L']=f1.iloc[27,3]
                    sub.at[iter,'SWELL_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'SWELL_M']=f1.iloc[28,3]
                    sub.at[iter,'SWELL_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'SWELL_H']=f1.iloc[29,3]
                    sub.at[iter,'SWELL_H_DV']=f1.iloc[37,3]
            if Distress_2 == 19:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'RAVEL_L']=f1.iloc[27,3]
                    sub.at[iter,'RAVEL_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'RAVEL_M']=f1.iloc[28,3]
                    sub.at[iter,'RAVEL_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'RAVEL_H']=f1.iloc[29,3]
                    sub.at[iter,'RAVEL_H_DV']=f1.iloc[37,3]
            if Distress_2 == 20:
                if Distress_2_dvl >= 0:
                    sub.at[iter,'WEATHERING_L']=f1.iloc[27,3]
                    sub.at[iter,'WEATHERING_L_DV']=f1.iloc[35,3]
                if Distress_2_dvm >= 0:
                    sub.at[iter,'WEATHERING_M']=f1.iloc[28,3]
                    sub.at[iter,'WEATHERING_M_DV']=f1.iloc[36,3] 
                if Distress_2_dvh >= 0:
                    sub.at[iter,'WEATHERING_H']=f1.iloc[29,3]
                    sub.at[iter,'WEATHERING_H_DV']=f1.iloc[37,3]


            if Distress_3 == 1:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'ALLIGATOR_L']=f1.iloc[27,4]
                    sub.at[iter,'ALLIGATOR_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'ALLIGATOR_M']=f1.iloc[28,4]
                    sub.at[iter,'ALLIGATOR_M_DV']=f1.iloc[36,4]
                if Distress_3_dvh >= 0:
                    sub.at[iter,'ALLIGATOR_H']=f1.iloc[29,4]
                    sub.at[iter,'ALLIGATOR_H_DV']=f1.iloc[37,4] 

            if Distress_3 == 2:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'BLEED_L']=f1.iloc[27,4]
                    sub.at[iter,'BLEED_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'BLEED_M']=f1.iloc[28,4]
                    sub.at[iter,'BLEED_M_DV']=f1.iloc[36,4]   
                if Distress_3_dvh >= 0:
                    sub.at[iter,'BLEED_H']=f1.iloc[29,4]
                    sub.at[iter,'BLEED_H_DV']=f1.iloc[37,4]

            if Distress_3 == 3:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'BLOCK_L']=f1.iloc[27,4]
                    sub.at[iter,'BLOCK_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'BLOCK_M']=f1.iloc[28,4]
                    sub.at[iter,'BLOCK_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'BLOCK_H']=f1.iloc[29,4]
                    sub.at[iter,'BLOCK_H_DV']=f1.iloc[37,4]


            if Distress_3 == 4:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'BUMP_L']=f1.iloc[27,4]
                    sub.at[iter,'BUMP_L']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'BUMP_M']=f1.iloc[28,4]
                    sub.at[iter,'BUMP_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'BUMP_H']=f1.iloc[29,4]
                    sub.at[iter,'BUMP_H_DV']=f1.iloc[37,4]
            if Distress_3 == 5:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'CORRUGATION_L']=f1.iloc[27,4]
                    sub.at[iter,'CORRUGATION_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'CORRUGATION_M']=f1.iloc[28,4]
                    sub.at[iter,'CORRUGATION_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'CORRUGATION_H']=f1.iloc[29,4]
                    sub.at[iter,'CORRUGATION_H_DV']=f1.iloc[37,4]
            if Distress_3 == 6:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'DEPRESSION_L']=f1.iloc[27,4]
                    sub.at[iter,'DEPRESSION_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'DEPRESSION_M']=f1.iloc[28,4]
                    sub.at[iter,'DEPRESSION_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'DEPRESSION_H']=f1.iloc[29,4]
                    sub.at[iter,'DEPRESSION_H_DV']=f1.iloc[37,4]
            if Distress_3 == 7:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'EDGE_L']=f1.iloc[27,4]
                    sub.at[iter,'EDGE_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'EDGE_M']=f1.iloc[28,4]
                    sub.at[iter,'EDGE_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'EDGE_H']=f1.iloc[29,4]
                    sub.at[iter,'EDGE_H_DV']=f1.iloc[37,4]
            if Distress_3 == 8:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'REFLECTION_L']=f1.iloc[27,4]
                    sub.at[iter,'REFLECTION_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'REFLECTION_M']=f1.iloc[28,4]
                    sub.at[iter,'REFLECTION_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'REFLECTION_H']=f1.iloc[29,4]
                    sub.at[iter,'REFLECTION_H_DV']=f1.iloc[37,4]
            if Distress_3 == 9:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'LANEDROP_L']=f1.iloc[27,4]
                    sub.at[iter,'LANEDROP_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'LANEDROP_M']=f1.iloc[28,4]
                    sub.at[iter,'LANEDROP_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'LANEDROP_H']=f1.iloc[29,4]
                    sub.at[iter,'LANEDROP_H_DV']=f1.iloc[37,4]

            if Distress_3 == 10:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'LONG_L']=f1.iloc[27,4]
                    sub.at[iter,'LONG_L_DV']=f1.iloc[35,4]

                if Distress_3_dvm >= 0:
                    sub.at[iter,'LONG_M']=f1.iloc[28,4]
                    sub.at[iter,'LONG_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'LONG_H']=f1.iloc[29,4]
                    sub.at[iter,'LONG_H_DV']=f1.iloc[37,4]


            if Distress_3 == 11:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'PATCH_L']=f1.iloc[27,4]
                    sub.at[iter,'PATCH_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'PATCH_M']=f1.iloc[28,4]
                    sub.at[iter,'PATCH_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'PATCH_H']=f1.iloc[29,4]
                    sub.at[iter,'PATCH_H_DV']=f1.iloc[37,4]
            if Distress_3 == 12:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'POLAG_L']=f1.iloc[27,4]
                    sub.at[iter,'POLAG_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'POLAG_M']=f1.iloc[28,4]
                    sub.at[iter,'POLAG_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'POLAG_H']=f1.iloc[29,4]
                    sub.at[iter,'POLAG_H_DV']=f1.iloc[37,4]
            if Distress_3 == 13:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'POTHOL_L']=f1.iloc[27,4]
                    sub.at[iter,'POTHOL_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'POTHOL_M']=f1.iloc[28,4]
                    sub.at[iter,'POTHOL_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'POTHOL_H']=f1.iloc[29,4]
                    sub.at[iter,'POTHOL_H_DV']=f1.iloc[37,4]

            if Distress_3 == 14:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'RAIL_L']=f1.iloc[27,4]
                    sub.at[iter,'RAIL_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'RAIL_M']=f1.iloc[28,4]
                    sub.at[iter,'RAIL_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'RAIL_H']=f1.iloc[29,4]
                    sub.at[iter,'RAIL_H_DV']=f1.iloc[37,4]
            if Distress_3 == 15:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'RUTTING_L']=f1.iloc[27,4]
                    sub.at[iter,'RUTTING_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'RUTTING_M']=f1.iloc[28,4]
                    sub.at[iter,'RUTTING_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'RUTTING_H']=f1.iloc[29,4]
                    sub.at[iter,'RUTTING_H_DV']=f1.iloc[37,4]
            if Distress_3 == 16:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'SHOVING_L']=f1.iloc[27,4]
                    sub.at[iter,'SHOVING_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'SHOVING_M']=f1.iloc[28,4]
                    sub.at[iter,'SHOVING_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'SHOVING_H']=f1.iloc[29,4]
                    sub.at[iter,'SHOVING_H_DV']=f1.iloc[37,4]
            if Distress_3 == 17:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'SLIPCRACK_L']=f1.iloc[27,4]
                    sub.at[iter,'SLIPCRACK_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'SLIPCRACK_M']=f1.iloc[28,4]
                    sub.at[iter,'SLIPCRACK_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'SLIPCRACK_H']=f1.iloc[29,4]
                    sub.at[iter,'SLIPCRACK_H_DV']=f1.iloc[37,4]
            if Distress_3 == 18:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'SWELL_L']=f1.iloc[27,4]
                    sub.at[iter,'SWELL_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'SWELL_M']=f1.iloc[28,4]
                    sub.at[iter,'SWELL_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'SWELL_H']=f1.iloc[29,4]
                    sub.at[iter,'SWELL_H_DV']=f1.iloc[37,4]
            if Distress_3 == 19:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'RAVEL_L']=f1.iloc[27,4]
                    sub.at[iter,'RAVEL_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'RAVEL_M']=f1.iloc[28,4]
                    sub.at[iter,'RAVEL_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'RAVEL_H']=f1.iloc[29,4]
                    sub.at[iter,'RAVEL_H_DV']=f1.iloc[37,4]
            if Distress_3 == 20:
                if Distress_3_dvl >= 0:
                    sub.at[iter,'WEATHERING_L']=f1.iloc[27,4]
                    sub.at[iter,'WEATHERING_L_DV']=f1.iloc[35,4]
                if Distress_3_dvm >= 0:
                    sub.at[iter,'WEATHERING_M']=f1.iloc[28,4]
                    sub.at[iter,'WEATHERING_M_DV']=f1.iloc[36,4] 
                if Distress_3_dvh >= 0:
                    sub.at[iter,'WEATHERING_H']=f1.iloc[29,4]
                    sub.at[iter,'WEATHERING_H_DV']=f1.iloc[37,4]

            if Distress_4 == 1:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'ALLIGATOR_L']=f1.iloc[27,5]
                    sub.at[iter,'ALLIGATOR_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'ALLIGATOR_M']=f1.iloc[28,5]
                    sub.at[iter,'ALLIGATOR_M_DV']=f1.iloc[36,5]
                if Distress_4_dvh >= 0:
                    sub.at[iter,'ALLIGATOR_H']=f1.iloc[29,5]
                    sub.at[iter,'ALLIGATOR_H_DV']=f1.iloc[37,5] 

            if Distress_4 == 2:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'BLEED_L']=f1.iloc[27,5]
                    sub.at[iter,'BLEED_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'BLEED_M']=f1.iloc[28,5]
                    sub.at[iter,'BLEED_M_DV']=f1.iloc[36,5]   
                if Distress_4_dvh >= 0:
                    sub.at[iter,'BLEED_H']=f1.iloc[29,5]
                    sub.at[iter,'BLEED_H_DV']=f1.iloc[37,5]

            if Distress_4 == 3:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'BLOCK_L']=f1.iloc[27,5]
                    sub.at[iter,'BLOCK_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'BLOCK_M']=f1.iloc[28,5]
                    sub.at[iter,'BLOCK_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'BLOCK_H']=f1.iloc[29,5]
                    sub.at[iter,'BLOCK_H_DV']=f1.iloc[37,5]


            if Distress_4 == 4:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'BUMP_L']=f1.iloc[27,5]
                    sub.at[iter,'BUMP_L']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'BUMP_M']=f1.iloc[28,5]
                    sub.at[iter,'BUMP_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'BUMP_H']=f1.iloc[29,5]
                    sub.at[iter,'BUMP_H_DV']=f1.iloc[37,5]
            if Distress_4 == 5:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'CORRUGATION_L']=f1.iloc[27,5]
                    sub.at[iter,'CORRUGATION_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'CORRUGATION_M']=f1.iloc[28,5]
                    sub.at[iter,'CORRUGATION_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'CORRUGATION_H']=f1.iloc[29,5]
                    sub.at[iter,'CORRUGATION_H_DV']=f1.iloc[37,5]
            if Distress_4 == 6:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'DEPRESSION_L']=f1.iloc[27,5]
                    sub.at[iter,'DEPRESSION_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'DEPRESSION_M']=f1.iloc[28,5]
                    sub.at[iter,'DEPRESSION_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'DEPRESSION_H']=f1.iloc[29,5]
                    sub.at[iter,'DEPRESSION_H_DV']=f1.iloc[37,5]
            if Distress_4 == 7:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'EDGE_L']=f1.iloc[27,5]
                    sub.at[iter,'EDGE_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'EDGE_M']=f1.iloc[28,5]
                    sub.at[iter,'EDGE_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'EDGE_H']=f1.iloc[29,5]
                    sub.at[iter,'EDGE_H_DV']=f1.iloc[37,5]
            if Distress_4 == 8:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'REFLECTION_L']=f1.iloc[27,5]
                    sub.at[iter,'REFLECTION_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'REFLECTION_M']=f1.iloc[28,5]
                    sub.at[iter,'REFLECTION_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'REFLECTION_H']=f1.iloc[29,5]
                    sub.at[iter,'REFLECTION_H_DV']=f1.iloc[37,5]
            if Distress_4 == 9:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'LANEDROP_L']=f1.iloc[27,5]
                    sub.at[iter,'LANEDROP_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'LANEDROP_M']=f1.iloc[28,5]
                    sub.at[iter,'LANEDROP_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'LANEDROP_H']=f1.iloc[29,5]
                    sub.at[iter,'LANEDROP_H_DV']=f1.iloc[37,5]

            if Distress_4 == 10:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'LONG_L']=f1.iloc[27,5]
                    sub.at[iter,'LONG_L_DV']=f1.iloc[35,5]

                if Distress_4_dvm >= 0:
                    sub.at[iter,'LONG_M']=f1.iloc[28,5]
                    sub.at[iter,'LONG_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'LONG_H']=f1.iloc[29,5]
                    sub.at[iter,'LONG_H_DV']=f1.iloc[37,5]


            if Distress_4 == 11:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'PATCH_L']=f1.iloc[27,5]
                    sub.at[iter,'PATCH_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'PATCH_M']=f1.iloc[28,5]
                    sub.at[iter,'PATCH_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'PATCH_H']=f1.iloc[29,5]
                    sub.at[iter,'PATCH_H_DV']=f1.iloc[37,5]
            if Distress_4 == 12:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'POLAG_L']=f1.iloc[27,5]
                    sub.at[iter,'POLAG_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'POLAG_M']=f1.iloc[28,5]
                    sub.at[iter,'POLAG_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'POLAG_H']=f1.iloc[29,5]
                    sub.at[iter,'POLAG_H_DV']=f1.iloc[37,5]
            if Distress_4 == 13:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'POTHOL_L']=f1.iloc[27,5]
                    sub.at[iter,'POTHOL_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'POTHOL_M']=f1.iloc[28,5]
                    sub.at[iter,'POTHOL_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'POTHOL_H']=f1.iloc[29,5]
                    sub.at[iter,'POTHOL_H_DV']=f1.iloc[37,5]

            if Distress_4 == 14:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'RAIL_L']=f1.iloc[27,5]
                    sub.at[iter,'RAIL_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'RAIL_M']=f1.iloc[28,5]
                    sub.at[iter,'RAIL_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'RAIL_H']=f1.iloc[29,5]
                    sub.at[iter,'RAIL_H_DV']=f1.iloc[37,5]
            if Distress_4 == 15:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'RUTTING_L']=f1.iloc[27,5]
                    sub.at[iter,'RUTTING_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'RUTTING_M']=f1.iloc[28,5]
                    sub.at[iter,'RUTTING_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'RUTTING_H']=f1.iloc[29,5]
                    sub.at[iter,'RUTTING_H_DV']=f1.iloc[37,5]
            if Distress_4 == 16:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'SHOVING_L']=f1.iloc[27,5]
                    sub.at[iter,'SHOVING_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'SHOVING_M']=f1.iloc[28,5]
                    sub.at[iter,'SHOVING_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'SHOVING_H']=f1.iloc[29,5]
                    sub.at[iter,'SHOVING_H_DV']=f1.iloc[37,5]
            if Distress_4 == 17:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'SLIPCRACK_L']=f1.iloc[27,5]
                    sub.at[iter,'SLIPCRACK_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'SLIPCRACK_M']=f1.iloc[28,5]
                    sub.at[iter,'SLIPCRACK_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'SLIPCRACK_H']=f1.iloc[29,5]
                    sub.at[iter,'SLIPCRACK_H_DV']=f1.iloc[37,5]
            if Distress_4 == 18:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'SWELL_L']=f1.iloc[27,5]
                    sub.at[iter,'SWELL_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'SWELL_M']=f1.iloc[28,5]
                    sub.at[iter,'SWELL_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'SWELL_H']=f1.iloc[29,5]
                    sub.at[iter,'SWELL_H_DV']=f1.iloc[37,5]
            if Distress_4 == 19:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'RAVEL_L']=f1.iloc[27,5]
                    sub.at[iter,'RAVEL_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'RAVEL_M']=f1.iloc[28,5]
                    sub.at[iter,'RAVEL_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'RAVEL_H']=f1.iloc[29,5]
                    sub.at[iter,'RAVEL_H_DV']=f1.iloc[37,5]
            if Distress_4 == 20:
                if Distress_4_dvl >= 0:
                    sub.at[iter,'WEATHERING_L']=f1.iloc[27,5]
                    sub.at[iter,'WEATHERING_L_DV']=f1.iloc[35,5]
                if Distress_4_dvm >= 0:
                    sub.at[iter,'WEATHERING_M']=f1.iloc[28,5]
                    sub.at[iter,'WEATHERING_M_DV']=f1.iloc[36,5] 
                if Distress_4_dvh >= 0:
                    sub.at[iter,'WEATHERING_H']=f1.iloc[29,5]
                    sub.at[iter,'WEATHERING_H_DV']=f1.iloc[37,5]

            if Distress_5 == 1:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'ALLIGATOR_L']=f1.iloc[27,6]
                    sub.at[iter,'ALLIGATOR_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'ALLIGATOR_M']=f1.iloc[28,6]
                    sub.at[iter,'ALLIGATOR_M_DV']=f1.iloc[36,6]
                if Distress_5_dvh >= 0:
                    sub.at[iter,'ALLIGATOR_H']=f1.iloc[29,6]
                    sub.at[iter,'ALLIGATOR_H_DV']=f1.iloc[37,6] 

            if Distress_5 == 2:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'BLEED_L']=f1.iloc[27,6]
                    sub.at[iter,'BLEED_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'BLEED_M']=f1.iloc[28,6]
                    sub.at[iter,'BLEED_M_DV']=f1.iloc[36,6]   
                if Distress_5_dvh >= 0:
                    sub.at[iter,'BLEED_H']=f1.iloc[29,6]
                    sub.at[iter,'BLEED_H_DV']=f1.iloc[37,6]

            if Distress_5 == 3:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'BLOCK_L']=f1.iloc[27,6]
                    sub.at[iter,'BLOCK_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'BLOCK_M']=f1.iloc[28,6]
                    sub.at[iter,'BLOCK_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'BLOCK_H']=f1.iloc[29,6]
                    sub.at[iter,'BLOCK_H_DV']=f1.iloc[37,6]


            if Distress_5 == 4:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'BUMP_L']=f1.iloc[27,6]
                    sub.at[iter,'BUMP_L']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'BUMP_M']=f1.iloc[28,6]
                    sub.at[iter,'BUMP_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'BUMP_H']=f1.iloc[29,6]
                    sub.at[iter,'BUMP_H_DV']=f1.iloc[37,6]
            if Distress_5 == 5:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'CORRUGATION_L']=f1.iloc[27,6]
                    sub.at[iter,'CORRUGATION_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'CORRUGATION_M']=f1.iloc[28,6]
                    sub.at[iter,'CORRUGATION_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'CORRUGATION_H']=f1.iloc[29,6]
                    sub.at[iter,'CORRUGATION_H_DV']=f1.iloc[37,6]
            if Distress_5 == 6:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'DEPRESSION_L']=f1.iloc[27,6]
                    sub.at[iter,'DEPRESSION_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'DEPRESSION_M']=f1.iloc[28,6]
                    sub.at[iter,'DEPRESSION_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'DEPRESSION_H']=f1.iloc[29,6]
                    sub.at[iter,'DEPRESSION_H_DV']=f1.iloc[37,6]
            if Distress_5 == 7:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'EDGE_L']=f1.iloc[27,6]
                    sub.at[iter,'EDGE_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'EDGE_M']=f1.iloc[28,6]
                    sub.at[iter,'EDGE_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'EDGE_H']=f1.iloc[29,6]
                    sub.at[iter,'EDGE_H_DV']=f1.iloc[37,6]
            if Distress_5 == 8:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'REFLECTION_L']=f1.iloc[27,6]
                    sub.at[iter,'REFLECTION_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'REFLECTION_M']=f1.iloc[28,6]
                    sub.at[iter,'REFLECTION_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'REFLECTION_H']=f1.iloc[29,6]
                    sub.at[iter,'REFLECTION_H_DV']=f1.iloc[37,6]
            if Distress_5 == 9:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'LANEDROP_L']=f1.iloc[27,6]
                    sub.at[iter,'LANEDROP_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'LANEDROP_M']=f1.iloc[28,6]
                    sub.at[iter,'LANEDROP_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'LANEDROP_H']=f1.iloc[29,6]
                    sub.at[iter,'LANEDROP_H_DV']=f1.iloc[37,6]

            if Distress_5 == 10:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'LONG_L']=f1.iloc[27,6]
                    sub.at[iter,'LONG_L_DV']=f1.iloc[35,6]

                if Distress_5_dvm >= 0:
                    sub.at[iter,'LONG_M']=f1.iloc[28,6]
                    sub.at[iter,'LONG_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'LONG_H']=f1.iloc[29,6]
                    sub.at[iter,'LONG_H_DV']=f1.iloc[37,6]


            if Distress_5 == 11:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'PATCH_L']=f1.iloc[27,6]
                    sub.at[iter,'PATCH_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'PATCH_M']=f1.iloc[28,6]
                    sub.at[iter,'PATCH_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'PATCH_H']=f1.iloc[29,6]
                    sub.at[iter,'PATCH_H_DV']=f1.iloc[37,6]
            if Distress_5 == 12:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'POLAG_L']=f1.iloc[27,6]
                    sub.at[iter,'POLAG_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'POLAG_M']=f1.iloc[28,6]
                    sub.at[iter,'POLAG_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'POLAG_H']=f1.iloc[29,6]
                    sub.at[iter,'POLAG_H_DV']=f1.iloc[37,6]
            if Distress_5 == 13:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'POTHOL_L']=f1.iloc[27,6]
                    sub.at[iter,'POTHOL_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'POTHOL_M']=f1.iloc[28,6]
                    sub.at[iter,'POTHOL_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'POTHOL_H']=f1.iloc[29,6]
                    sub.at[iter,'POTHOL_H_DV']=f1.iloc[37,6]

            if Distress_5 == 14:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'RAIL_L']=f1.iloc[27,6]
                    sub.at[iter,'RAIL_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'RAIL_M']=f1.iloc[28,6]
                    sub.at[iter,'RAIL_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'RAIL_H']=f1.iloc[29,6]
                    sub.at[iter,'RAIL_H_DV']=f1.iloc[37,6]
            if Distress_5 == 15:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'RUTTING_L']=f1.iloc[27,6]
                    sub.at[iter,'RUTTING_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'RUTTING_M']=f1.iloc[28,6]
                    sub.at[iter,'RUTTING_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'RUTTING_H']=f1.iloc[29,6]
                    sub.at[iter,'RUTTING_H_DV']=f1.iloc[37,6]
            if Distress_5 == 16:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'SHOVING_L']=f1.iloc[27,6]
                    sub.at[iter,'SHOVING_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'SHOVING_M']=f1.iloc[28,6]
                    sub.at[iter,'SHOVING_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'SHOVING_H']=f1.iloc[29,6]
                    sub.at[iter,'SHOVING_H_DV']=f1.iloc[37,6]
            if Distress_5 == 17:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'SLIPCRACK_L']=f1.iloc[27,6]
                    sub.at[iter,'SLIPCRACK_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'SLIPCRACK_M']=f1.iloc[28,6]
                    sub.at[iter,'SLIPCRACK_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'SLIPCRACK_H']=f1.iloc[29,6]
                    sub.at[iter,'SLIPCRACK_H_DV']=f1.iloc[37,6]
            if Distress_5 == 18:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'SWELL_L']=f1.iloc[27,6]
                    sub.at[iter,'SWELL_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'SWELL_M']=f1.iloc[28,6]
                    sub.at[iter,'SWELL_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'SWELL_H']=f1.iloc[29,6]
                    sub.at[iter,'SWELL_H_DV']=f1.iloc[37,6]
            if Distress_5 == 19:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'RAVEL_L']=f1.iloc[27,6]
                    sub.at[iter,'RAVEL_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'RAVEL_M']=f1.iloc[28,6]
                    sub.at[iter,'RAVEL_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'RAVEL_H']=f1.iloc[29,6]
                    sub.at[iter,'RAVEL_H_DV']=f1.iloc[37,6]
            if Distress_5 == 20:
                if Distress_5_dvl >= 0:
                    sub.at[iter,'WEATHERING_L']=f1.iloc[27,6]
                    sub.at[iter,'WEATHERING_L_DV']=f1.iloc[35,6]
                if Distress_5_dvm >= 0:
                    sub.at[iter,'WEATHERING_M']=f1.iloc[28,6]
                    sub.at[iter,'WEATHERING_M_DV']=f1.iloc[36,6] 
                if Distress_5_dvh >= 0:
                    sub.at[iter,'WEATHERING_H']=f1.iloc[29,6]
                    sub.at[iter,'WEATHERING_H_DV']=f1.iloc[37,6]



            iter = iter+1





        sub2 = sub2.append(sub,ignore_index=True)
        f2= pd.read_excel(input_excel+"\\"+file)
        for b in range(9,len(fx.sheet_names)):
            f2= pd.read_excel(input_excel+"\\"+file,index_col = None, header= None,sheet_name = b )

            PMS_start = f2.iloc[24,15]
            PMS_CHAINAGE = sub1.at[itera,'PMS_CHAINAGE_START']= PMS_start
            PMS_CHAINAGE = str(PMS_CHAINAGE)
            PMS_CHAINAGE = PMS_CHAINAGE.replace('.0','')
            Survey = f2.iloc[7,10]
            sub1.at[itera,'PCI_RATING']=f2.iloc[42,18]
            sub1.at[itera,'LANE_WIDTH']=f2.iloc[14,4]
            PMS_end = f2.iloc[24,18]          
            PMS_CHAINAGE_END = sub1.at[itera,'PMS_CHAINAGE_END']= PMS_end
            PMS_CHAINAGE_END = str(PMS_CHAINAGE_END)
            PMS_CHAINAGE_END = PMS_CHAINAGE_END.replace('.0','')

            Survey_start = f2.iloc[25,15]
            SURVEY_CHAINAGE = sub1.at[itera,'SURVEY_CHAINAGE_START']=  Survey_start
            SURVEY_CHAINAGE = str(SURVEY_CHAINAGE)
            SURVEY_CHAINAGE = PMS_CHAINAGE.replace('.0','')

            Survey_end = f2.iloc[25,18]          
            SURVEY_CHAINAGE_END = sub1.at[itera,'SURVEY_CHAINAGE_END']= Survey_end
            SURVEY_CHAINAGE_END = str(SURVEY_CHAINAGE_END)
            SURVEY_CHAINAGE_END = PMS_CHAINAGE_END.replace('.0','')

            sub1.at[itera,'SURVEY_ID']= Survey

            link = sub1.at[itera,'LINK']= str(Survey)+'_'+PMS_CHAINAGE
            sub1.at[itera,'PCI_VALUE']=f2.iloc[42,15]

            Distres_1 = f2.iloc[26,14]
            Distres_1l = f2.iloc[27,14]
            Distres_1m = f2.iloc[28,14]
            Distres_1h = f2.iloc[29,14]
            Distres_1_dvl = f2.iloc[35,14]
            Distres_1_dvm = f2.iloc[36,14]
            Distres_1_dvh = f2.iloc[37,14]

            Distres_2 = f2.iloc[26,15]
            Distres_2l = f2.iloc[27,15]
            Distres_2m = f2.iloc[28,15]
            Distres_2h = f2.iloc[29,15]
            Distres_2_dvl = f2.iloc[35,15]
            Distres_2_dvm = f2.iloc[36,15]
            Distres_2_dvh = f2.iloc[37,15]



            Distres_3 = f2.iloc[26,16]
            Distres_3l = f2.iloc[27,16]
            Distres_3m = f2.iloc[28,16]
            Distres_3h = f2.iloc[29,16]
            Distres_3_dvl = f2.iloc[35,16]
            Distres_3_dvm = f2.iloc[36,16]
            Distres_3_dvh = f2.iloc[37,16]



            Distres_4 = f2.iloc[26,17]
            Distres_4l = f2.iloc[27,17]
            Distres_4m = f2.iloc[28,17]
            Distres_4h = f2.iloc[29,17]
            Distres_4_dvl = f2.iloc[35,17]
            Distres_4_dvm = f2.iloc[36,17]
            Distres_4_dvh = f2.iloc[37,17]



            Distres_5 = f2.iloc[26,18]
            Distres_5l = f2.iloc[27,18]
            Distres_5m = f2.iloc[28,18]
            Distres_5h = f2.iloc[29,18]
            Distres_5_dvl = f2.iloc[35,18]
            Distres_5_dvm = f2.iloc[36,18]
            Distres_5_dvh = f2.iloc[37,18]

            if Distres_1 == 1:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'ALLIGATOR_L']=f2.iloc[27,14]
                    sub1.at[itera,'ALLIGATOR_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'ALLIGATOR_M']=f2.iloc[28,14]
                    sub1.at[itera,'ALLIGATOR_M_DV']=f2.iloc[36,14]
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'ALLIGATOR_H']=f2.iloc[29,14]
                    sub1.at[itera,'ALLIGATOR_H_DV']=f2.iloc[37,14] 

            if Distres_1 == 2:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'BLEED_L']=f2.iloc[27,14]
                    sub1.at[itera,'BLEED_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'BLEED_M']=f2.iloc[28,14]
                    sub1.at[itera,'BLEED_M_DV']=f2.iloc[36,14]   
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'BLEED_H']=f2.iloc[29,14]
                    sub1.at[itera,'BLEED_H_DV']=f2.iloc[37,14]

            if Distres_1 == 3:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'BLOCK_L']=f2.iloc[27,14]
                    sub1.at[itera,'BLOCK_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'BLOCK_M']=f2.iloc[28,14]
                    sub1.at[itera,'BLOCK_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'BLOCK_H']=f2.iloc[29,14]
                    sub1.at[itera,'BLOCK_H_DV']=f2.iloc[37,14]


            if Distres_1 == 4:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'BUMP_L']=f2.iloc[27,14]
                    sub1.at[itera,'BUMP_L']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'BUMP_M']=f2.iloc[28,14]
                    sub1.at[itera,'BUMP_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'BUMP_H']=f2.iloc[29,14]
                    sub1.at[itera,'BUMP_H_DV']=f2.iloc[37,14]
            if Distres_1 == 5:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'CORRUGATION_L']=f2.iloc[27,14]
                    sub1.at[itera,'CORRUGATION_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'CORRUGATION_M']=f2.iloc[28,14]
                    sub1.at[itera,'CORRUGATION_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'CORRUGATION_H']=f2.iloc[29,14]
                    sub1.at[itera,'CORRUGATION_H_DV']=f2.iloc[37,14]
            if Distres_1 == 6:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'DEPRESSION_L']=f2.iloc[27,14]
                    sub1.at[itera,'DEPRESSION_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'DEPRESSION_M']=f2.iloc[28,14]
                    sub1.at[itera,'DEPRESSION_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'DEPRESSION_H']=f2.iloc[29,14]
                    sub1.at[itera,'DEPRESSION_H_DV']=f2.iloc[37,14]
            if Distres_1 == 7:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'EDGE_L']=f2.iloc[27,14]
                    sub1.at[itera,'EDGE_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'EDGE_M']=f2.iloc[28,14]
                    sub1.at[itera,'EDGE_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'EDGE_H']=f2.iloc[29,14]
                    sub1.at[itera,'EDGE_H_DV']=f2.iloc[37,14]
            if Distres_1 == 8:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'REFLECTION_L']=f2.iloc[27,14]
                    sub1.at[itera,'REFLECTION_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'REFLECTION_M']=f2.iloc[28,14]
                    sub1.at[itera,'REFLECTION_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'REFLECTION_H']=f2.iloc[29,14]
                    sub1.at[itera,'REFLECTION_H_DV']=f2.iloc[37,14]
            if Distres_1 == 9:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'LANEDROP_L']=f2.iloc[27,14]
                    sub1.at[itera,'LANEDROP_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'LANEDROP_M']=f2.iloc[28,14]
                    sub1.at[itera,'LANEDROP_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'LANEDROP_H']=f2.iloc[29,14]
                    sub1.at[itera,'LANEDROP_H_DV']=f2.iloc[37,14]

            if Distres_1 == 10:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'LONG_L']=f2.iloc[27,14]
                    sub1.at[itera,'LONG_L_DV']=f2.iloc[35,14]

                if Distres_1_dvm >= 0:
                    sub1.at[itera,'LONG_M']=f2.iloc[28,14]
                    sub1.at[itera,'LONG_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'LONG_H']=f2.iloc[29,14]
                    sub1.at[itera,'LONG_H_DV']=f2.iloc[37,14]


            if Distres_1 == 11:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'PATCH_L']=f2.iloc[27,14]
                    sub1.at[itera,'PATCH_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'PATCH_M']=f2.iloc[28,14]
                    sub1.at[itera,'PATCH_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'PATCH_H']=f2.iloc[29,14]
                    sub1.at[itera,'PATCH_H_DV']=f2.iloc[37,14]
            if Distres_1 == 12:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'POLAG_L']=f2.iloc[27,14]
                    sub1.at[itera,'POLAG_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'POLAG_M']=f2.iloc[28,14]
                    sub1.at[itera,'POLAG_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'POLAG_H']=f2.iloc[29,14]
                    sub1.at[itera,'POLAG_H_DV']=f2.iloc[37,14]
            if Distres_1 == 13:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'POTHOL_L']=f2.iloc[27,14]
                    sub1.at[itera,'POTHOL_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'POTHOL_M']=f2.iloc[28,14]
                    sub1.at[itera,'POTHOL_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'POTHOL_H']=f2.iloc[29,14]
                    sub1.at[itera,'POTHOL_H_DV']=f2.iloc[37,14]

            if Distres_1 == 14:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'RAIL_L']=f2.iloc[27,14]
                    sub1.at[itera,'RAIL_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'RAIL_M']=f2.iloc[28,14]
                    sub1.at[itera,'RAIL_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'RAIL_H']=f2.iloc[29,14]
                    sub1.at[itera,'RAIL_H_DV']=f2.iloc[37,14]
            if Distres_1 == 15:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'RUTTING_L']=f2.iloc[27,14]
                    sub1.at[itera,'RUTTING_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'RUTTING_M']=f2.iloc[28,14]
                    sub1.at[itera,'RUTTING_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'RUTTING_H']=f2.iloc[29,14]
                    sub1.at[itera,'RUTTING_H_DV']=f2.iloc[37,14]
            if Distres_1 == 16:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'SHOVING_L']=f2.iloc[27,14]
                    sub1.at[itera,'SHOVING_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'SHOVING_M']=f2.iloc[28,14]
                    sub1.at[itera,'SHOVING_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'SHOVING_H']=f2.iloc[29,14]
                    sub1.at[itera,'SHOVING_H_DV']=f2.iloc[37,14]
            if Distres_1 == 17:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'SLIPCRACK_L']=f2.iloc[27,14]
                    sub1.at[itera,'SLIPCRACK_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'SLIPCRACK_M']=f2.iloc[28,14]
                    sub1.at[itera,'SLIPCRACK_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'SLIPCRACK_H']=f2.iloc[29,14]
                    sub1.at[itera,'SLIPCRACK_H_DV']=f2.iloc[37,14]
            if Distres_1 == 18:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'SWELL_L']=f2.iloc[27,14]
                    sub1.at[itera,'SWELL_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'SWELL_M']=f2.iloc[28,14]
                    sub1.at[itera,'SWELL_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'SWELL_H']=f2.iloc[29,14]
                    sub1.at[itera,'SWELL_H_DV']=f2.iloc[37,14]
            if Distres_1 == 19:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'RAVEL_L']=f2.iloc[27,14]
                    sub1.at[itera,'RAVEL_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'RAVEL_M']=f2.iloc[28,14]
                    sub1.at[itera,'RAVEL_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'RAVEL_H']=f2.iloc[29,14]
                    sub1.at[itera,'RAVEL_H_DV']=f2.iloc[37,14]
            if Distres_1 == 20:
                if Distres_1_dvl >= 0:
                    sub1.at[itera,'WEATHERING_L']=f2.iloc[27,14]
                    sub1.at[itera,'WEATHERING_L_DV']=f2.iloc[35,14]
                if Distres_1_dvm >= 0:
                    sub1.at[itera,'WEATHERING_M']=f2.iloc[28,14]
                    sub1.at[itera,'WEATHERING_M_DV']=f2.iloc[36,14] 
                if Distres_1_dvh >= 0:
                    sub1.at[itera,'WEATHERING_H']=f2.iloc[29,14]
                    sub1.at[itera,'WEATHERING_H_DV']=f2.iloc[37,14]

            if Distres_2 == 1:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'ALLIGATOR_L']=f2.iloc[27,15]
                    sub1.at[itera,'ALLIGATOR_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'ALLIGATOR_M']=f2.iloc[28,15]
                    sub1.at[itera,'ALLIGATOR_M_DV']=f2.iloc[36,15]
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'ALLIGATOR_H']=f2.iloc[29,15]
                    sub1.at[itera,'ALLIGATOR_H_DV']=f2.iloc[37,15] 

            if Distres_2 == 2:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'BLEED_L']=f2.iloc[27,15]
                    sub1.at[itera,'BLEED_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'BLEED_M']=f2.iloc[28,15]
                    sub1.at[itera,'BLEED_M_DV']=f2.iloc[36,15]   
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'BLEED_H']=f2.iloc[29,15]
                    sub1.at[itera,'BLEED_H_DV']=f2.iloc[37,15]

            if Distres_2 == 3:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'BLOCK_L']=f2.iloc[27,15]
                    sub1.at[itera,'BLOCK_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'BLOCK_M']=f2.iloc[28,15]
                    sub1.at[itera,'BLOCK_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'BLOCK_H']=f2.iloc[29,15]
                    sub1.at[itera,'BLOCK_H_DV']=f2.iloc[37,15]


            if Distres_2 == 4:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'BUMP_L']=f2.iloc[27,15]
                    sub1.at[itera,'BUMP_L']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'BUMP_M']=f2.iloc[28,15]
                    sub1.at[itera,'BUMP_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'BUMP_H']=f2.iloc[29,15]
                    sub1.at[itera,'BUMP_H_DV']=f2.iloc[37,15]
            if Distres_2 == 5:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'CORRUGATION_L']=f2.iloc[27,15]
                    sub1.at[itera,'CORRUGATION_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'CORRUGATION_M']=f2.iloc[28,15]
                    sub1.at[itera,'CORRUGATION_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'CORRUGATION_H']=f2.iloc[29,15]
                    sub1.at[itera,'CORRUGATION_H_DV']=f2.iloc[37,15]
            if Distres_2 == 6:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'DEPRESSION_L']=f2.iloc[27,15]
                    sub1.at[itera,'DEPRESSION_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'DEPRESSION_M']=f2.iloc[28,15]
                    sub1.at[itera,'DEPRESSION_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'DEPRESSION_H']=f2.iloc[29,15]
                    sub1.at[itera,'DEPRESSION_H_DV']=f2.iloc[37,15]
            if Distres_2 == 7:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'EDGE_L']=f2.iloc[27,15]
                    sub1.at[itera,'EDGE_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'EDGE_M']=f2.iloc[28,15]
                    sub1.at[itera,'EDGE_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'EDGE_H']=f2.iloc[29,15]
                    sub1.at[itera,'EDGE_H_DV']=f2.iloc[37,15]
            if Distres_2 == 8:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'REFLECTION_L']=f2.iloc[27,15]
                    sub1.at[itera,'REFLECTION_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'REFLECTION_M']=f2.iloc[28,15]
                    sub1.at[itera,'REFLECTION_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'REFLECTION_H']=f2.iloc[29,15]
                    sub1.at[itera,'REFLECTION_H_DV']=f2.iloc[37,15]
            if Distres_2 == 9:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'LANEDROP_L']=f2.iloc[27,15]
                    sub1.at[itera,'LANEDROP_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'LANEDROP_M']=f2.iloc[28,15]
                    sub1.at[itera,'LANEDROP_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'LANEDROP_H']=f2.iloc[29,15]
                    sub1.at[itera,'LANEDROP_H_DV']=f2.iloc[37,15]

            if Distres_2 == 10:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'LONG_L']=f2.iloc[27,15]
                    sub1.at[itera,'LONG_L_DV']=f2.iloc[35,15]

                if Distres_2_dvm >= 0:
                    sub1.at[itera,'LONG_M']=f2.iloc[28,15]
                    sub1.at[itera,'LONG_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'LONG_H']=f2.iloc[29,15]
                    sub1.at[itera,'LONG_H_DV']=f2.iloc[37,15]


            if Distres_2 == 11:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'PATCH_L']=f2.iloc[27,15]
                    sub1.at[itera,'PATCH_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'PATCH_M']=f2.iloc[28,15]
                    sub1.at[itera,'PATCH_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'PATCH_H']=f2.iloc[29,15]
                    sub1.at[itera,'PATCH_H_DV']=f2.iloc[37,15]
            if Distres_2 == 12:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'POLAG_L']=f2.iloc[27,15]
                    sub1.at[itera,'POLAG_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'POLAG_M']=f2.iloc[28,15]
                    sub1.at[itera,'POLAG_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'POLAG_H']=f2.iloc[29,15]
                    sub1.at[itera,'POLAG_H_DV']=f2.iloc[37,15]
            if Distres_2 == 13:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'POTHOL_L']=f2.iloc[27,15]
                    sub1.at[itera,'POTHOL_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'POTHOL_M']=f2.iloc[28,15]
                    sub1.at[itera,'POTHOL_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'POTHOL_H']=f2.iloc[29,15]
                    sub1.at[itera,'POTHOL_H_DV']=f2.iloc[37,15]

            if Distres_2 == 14:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'RAIL_L']=f2.iloc[27,15]
                    sub1.at[itera,'RAIL_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'RAIL_M']=f2.iloc[28,15]
                    sub1.at[itera,'RAIL_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'RAIL_H']=f2.iloc[29,15]
                    sub1.at[itera,'RAIL_H_DV']=f2.iloc[37,15]
            if Distres_2 == 15:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'RUTTING_L']=f2.iloc[27,15]
                    sub1.at[itera,'RUTTING_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'RUTTING_M']=f2.iloc[28,15]
                    sub1.at[itera,'RUTTING_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'RUTTING_H']=f2.iloc[29,15]
                    sub1.at[itera,'RUTTING_H_DV']=f2.iloc[37,15]
            if Distres_2 == 16:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'SHOVING_L']=f2.iloc[27,15]
                    sub1.at[itera,'SHOVING_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'SHOVING_M']=f2.iloc[28,15]
                    sub1.at[itera,'SHOVING_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'SHOVING_H']=f2.iloc[29,15]
                    sub1.at[itera,'SHOVING_H_DV']=f2.iloc[37,15]
            if Distres_2 == 17:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'SLIPCRACK_L']=f2.iloc[27,15]
                    sub1.at[itera,'SLIPCRACK_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'SLIPCRACK_M']=f2.iloc[28,15]
                    sub1.at[itera,'SLIPCRACK_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'SLIPCRACK_H']=f2.iloc[29,15]
                    sub1.at[itera,'SLIPCRACK_H_DV']=f2.iloc[37,15]
            if Distres_2 == 18:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'SWELL_L']=f2.iloc[27,15]
                    sub1.at[itera,'SWELL_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'SWELL_M']=f2.iloc[28,15]
                    sub1.at[itera,'SWELL_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'SWELL_H']=f2.iloc[29,15]
                    sub1.at[itera,'SWELL_H_DV']=f2.iloc[37,15]
            if Distres_2 == 19:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'RAVEL_L']=f2.iloc[27,15]
                    sub1.at[itera,'RAVEL_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'RAVEL_M']=f2.iloc[28,15]
                    sub1.at[itera,'RAVEL_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'RAVEL_H']=f2.iloc[29,15]
                    sub1.at[itera,'RAVEL_H_DV']=f2.iloc[37,15]
            if Distres_2 == 20:
                if Distres_2_dvl >= 0:
                    sub1.at[itera,'WEATHERING_L']=f2.iloc[27,15]
                    sub1.at[itera,'WEATHERING_L_DV']=f2.iloc[35,15]
                if Distres_2_dvm >= 0:
                    sub1.at[itera,'WEATHERING_M']=f2.iloc[28,15]
                    sub1.at[itera,'WEATHERING_M_DV']=f2.iloc[36,15] 
                if Distres_2_dvh >= 0:
                    sub1.at[itera,'WEATHERING_H']=f2.iloc[29,15]
                    sub1.at[itera,'WEATHERING_H_DV']=f2.iloc[37,15]


            if Distres_3 == 1:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'ALLIGATOR_L']=f2.iloc[27,16]
                    sub1.at[itera,'ALLIGATOR_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'ALLIGATOR_M']=f2.iloc[28,16]
                    sub1.at[itera,'ALLIGATOR_M_DV']=f2.iloc[36,16]
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'ALLIGATOR_H']=f2.iloc[29,16]
                    sub1.at[itera,'ALLIGATOR_H_DV']=f2.iloc[37,16] 

            if Distres_3 == 2:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'BLEED_L']=f2.iloc[27,16]
                    sub1.at[itera,'BLEED_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'BLEED_M']=f2.iloc[28,16]
                    sub1.at[itera,'BLEED_M_DV']=f2.iloc[36,16]   
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'BLEED_H']=f2.iloc[29,16]
                    sub1.at[itera,'BLEED_H_DV']=f2.iloc[37,16]

            if Distres_3 == 3:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'BLOCK_L']=f2.iloc[27,16]
                    sub1.at[itera,'BLOCK_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'BLOCK_M']=f2.iloc[28,16]
                    sub1.at[itera,'BLOCK_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'BLOCK_H']=f2.iloc[29,16]
                    sub1.at[itera,'BLOCK_H_DV']=f2.iloc[37,16]


            if Distres_3 == 4:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'BUMP_L']=f2.iloc[27,16]
                    sub1.at[itera,'BUMP_L']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'BUMP_M']=f2.iloc[28,16]
                    sub1.at[itera,'BUMP_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'BUMP_H']=f2.iloc[29,16]
                    sub1.at[itera,'BUMP_H_DV']=f2.iloc[37,16]
            if Distres_3 == 5:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'CORRUGATION_L']=f2.iloc[27,16]
                    sub1.at[itera,'CORRUGATION_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'CORRUGATION_M']=f2.iloc[28,16]
                    sub1.at[itera,'CORRUGATION_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'CORRUGATION_H']=f2.iloc[29,16]
                    sub1.at[itera,'CORRUGATION_H_DV']=f2.iloc[37,16]
            if Distres_3 == 6:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'DEPRESSION_L']=f2.iloc[27,16]
                    sub1.at[itera,'DEPRESSION_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'DEPRESSION_M']=f2.iloc[28,16]
                    sub1.at[itera,'DEPRESSION_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'DEPRESSION_H']=f2.iloc[29,16]
                    sub1.at[itera,'DEPRESSION_H_DV']=f2.iloc[37,16]
            if Distres_3 == 7:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'EDGE_L']=f2.iloc[27,16]
                    sub1.at[itera,'EDGE_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'EDGE_M']=f2.iloc[28,16]
                    sub1.at[itera,'EDGE_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'EDGE_H']=f2.iloc[29,16]
                    sub1.at[itera,'EDGE_H_DV']=f2.iloc[37,16]
            if Distres_3 == 8:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'REFLECTION_L']=f2.iloc[27,16]
                    sub1.at[itera,'REFLECTION_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'REFLECTION_M']=f2.iloc[28,16]
                    sub1.at[itera,'REFLECTION_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'REFLECTION_H']=f2.iloc[29,16]
                    sub1.at[itera,'REFLECTION_H_DV']=f2.iloc[37,16]
            if Distres_3 == 9:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'LANEDROP_L']=f2.iloc[27,16]
                    sub1.at[itera,'LANEDROP_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'LANEDROP_M']=f2.iloc[28,16]
                    sub1.at[itera,'LANEDROP_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'LANEDROP_H']=f2.iloc[29,16]
                    sub1.at[itera,'LANEDROP_H_DV']=f2.iloc[37,16]

            if Distres_3 == 10:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'LONG_L']=f2.iloc[27,16]
                    sub1.at[itera,'LONG_L_DV']=f2.iloc[35,16]

                if Distres_3_dvm >= 0:
                    sub1.at[itera,'LONG_M']=f2.iloc[28,16]
                    sub1.at[itera,'LONG_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'LONG_H']=f2.iloc[29,16]
                    sub1.at[itera,'LONG_H_DV']=f2.iloc[37,16]


            if Distres_3 == 11:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'PATCH_L']=f2.iloc[27,16]
                    sub1.at[itera,'PATCH_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'PATCH_M']=f2.iloc[28,16]
                    sub1.at[itera,'PATCH_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'PATCH_H']=f2.iloc[29,16]
                    sub1.at[itera,'PATCH_H_DV']=f2.iloc[37,16]
            if Distres_3 == 12:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'POLAG_L']=f2.iloc[27,16]
                    sub1.at[itera,'POLAG_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'POLAG_M']=f2.iloc[28,16]
                    sub1.at[itera,'POLAG_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'POLAG_H']=f2.iloc[29,16]
                    sub1.at[itera,'POLAG_H_DV']=f2.iloc[37,16]
            if Distres_3 == 13:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'POTHOL_L']=f2.iloc[27,16]
                    sub1.at[itera,'POTHOL_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'POTHOL_M']=f2.iloc[28,16]
                    sub1.at[itera,'POTHOL_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'POTHOL_H']=f2.iloc[29,16]
                    sub1.at[itera,'POTHOL_H_DV']=f2.iloc[37,16]

            if Distres_3 == 14:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'RAIL_L']=f2.iloc[27,16]
                    sub1.at[itera,'RAIL_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'RAIL_M']=f2.iloc[28,16]
                    sub1.at[itera,'RAIL_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'RAIL_H']=f2.iloc[29,16]
                    sub1.at[itera,'RAIL_H_DV']=f2.iloc[37,16]
            if Distres_3 == 15:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'RUTTING_L']=f2.iloc[27,16]
                    sub1.at[itera,'RUTTING_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'RUTTING_M']=f2.iloc[28,16]
                    sub1.at[itera,'RUTTING_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'RUTTING_H']=f2.iloc[29,16]
                    sub1.at[itera,'RUTTING_H_DV']=f2.iloc[37,16]
            if Distres_3 == 16:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'SHOVING_L']=f2.iloc[27,16]
                    sub1.at[itera,'SHOVING_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'SHOVING_M']=f2.iloc[28,16]
                    sub1.at[itera,'SHOVING_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'SHOVING_H']=f2.iloc[29,16]
                    sub1.at[itera,'SHOVING_H_DV']=f2.iloc[37,16]
            if Distres_3 == 17:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'SLIPCRACK_L']=f2.iloc[27,16]
                    sub1.at[itera,'SLIPCRACK_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'SLIPCRACK_M']=f2.iloc[28,16]
                    sub1.at[itera,'SLIPCRACK_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'SLIPCRACK_H']=f2.iloc[29,16]
                    sub1.at[itera,'SLIPCRACK_H_DV']=f2.iloc[37,16]
            if Distres_3 == 18:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'SWELL_L']=f2.iloc[27,16]
                    sub1.at[itera,'SWELL_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'SWELL_M']=f2.iloc[28,16]
                    sub1.at[itera,'SWELL_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'SWELL_H']=f2.iloc[29,16]
                    sub1.at[itera,'SWELL_H_DV']=f2.iloc[37,16]
            if Distres_3 == 19:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'RAVEL_L']=f2.iloc[27,16]
                    sub1.at[itera,'RAVEL_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'RAVEL_M']=f2.iloc[28,16]
                    sub1.at[itera,'RAVEL_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'RAVEL_H']=f2.iloc[29,16]
                    sub1.at[itera,'RAVEL_H_DV']=f2.iloc[37,16]
            if Distres_3 == 20:
                if Distres_3_dvl >= 0:
                    sub1.at[itera,'WEATHERING_L']=f2.iloc[27,16]
                    sub1.at[itera,'WEATHERING_L_DV']=f2.iloc[35,16]
                if Distres_3_dvm >= 0:
                    sub1.at[itera,'WEATHERING_M']=f2.iloc[28,16]
                    sub1.at[itera,'WEATHERING_M_DV']=f2.iloc[36,16] 
                if Distres_3_dvh >= 0:
                    sub1.at[itera,'WEATHERING_H']=f2.iloc[29,16]
                    sub1.at[itera,'WEATHERING_H_DV']=f2.iloc[37,16]

            if Distres_4 == 1:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'ALLIGATOR_L']=f2.iloc[27,17]
                    sub1.at[itera,'ALLIGATOR_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'ALLIGATOR_M']=f2.iloc[28,17]
                    sub1.at[itera,'ALLIGATOR_M_DV']=f2.iloc[36,17]
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'ALLIGATOR_H']=f2.iloc[29,17]
                    sub1.at[itera,'ALLIGATOR_H_DV']=f2.iloc[37,17] 

            if Distres_4 == 2:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'BLEED_L']=f2.iloc[27,17]
                    sub1.at[itera,'BLEED_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'BLEED_M']=f2.iloc[28,17]
                    sub1.at[itera,'BLEED_M_DV']=f2.iloc[36,17]   
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'BLEED_H']=f2.iloc[29,17]
                    sub1.at[itera,'BLEED_H_DV']=f2.iloc[37,17]

            if Distres_4 == 3:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'BLOCK_L']=f2.iloc[27,17]
                    sub1.at[itera,'BLOCK_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'BLOCK_M']=f2.iloc[28,17]
                    sub1.at[itera,'BLOCK_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'BLOCK_H']=f2.iloc[29,17]
                    sub1.at[itera,'BLOCK_H_DV']=f2.iloc[37,17]


            if Distres_4 == 4:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'BUMP_L']=f2.iloc[27,17]
                    sub1.at[itera,'BUMP_L']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'BUMP_M']=f2.iloc[28,17]
                    sub1.at[itera,'BUMP_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'BUMP_H']=f2.iloc[29,17]
                    sub1.at[itera,'BUMP_H_DV']=f2.iloc[37,17]
            if Distres_4 == 5:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'CORRUGATION_L']=f2.iloc[27,17]
                    sub1.at[itera,'CORRUGATION_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'CORRUGATION_M']=f2.iloc[28,17]
                    sub1.at[itera,'CORRUGATION_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'CORRUGATION_H']=f2.iloc[29,17]
                    sub1.at[itera,'CORRUGATION_H_DV']=f2.iloc[37,17]
            if Distres_4 == 6:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'DEPRESSION_L']=f2.iloc[27,17]
                    sub1.at[itera,'DEPRESSION_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'DEPRESSION_M']=f2.iloc[28,17]
                    sub1.at[itera,'DEPRESSION_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'DEPRESSION_H']=f2.iloc[29,17]
                    sub1.at[itera,'DEPRESSION_H_DV']=f2.iloc[37,17]
            if Distres_4 == 7:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'EDGE_L']=f2.iloc[27,17]
                    sub1.at[itera,'EDGE_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'EDGE_M']=f2.iloc[28,17]
                    sub1.at[itera,'EDGE_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'EDGE_H']=f2.iloc[29,17]
                    sub1.at[itera,'EDGE_H_DV']=f2.iloc[37,17]
            if Distres_4 == 8:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'REFLECTION_L']=f2.iloc[27,17]
                    sub1.at[itera,'REFLECTION_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'REFLECTION_M']=f2.iloc[28,17]
                    sub1.at[itera,'REFLECTION_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'REFLECTION_H']=f2.iloc[29,17]
                    sub1.at[itera,'REFLECTION_H_DV']=f2.iloc[37,17]
            if Distres_4 == 9:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'LANEDROP_L']=f2.iloc[27,17]
                    sub1.at[itera,'LANEDROP_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'LANEDROP_M']=f2.iloc[28,17]
                    sub1.at[itera,'LANEDROP_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'LANEDROP_H']=f2.iloc[29,17]
                    sub1.at[itera,'LANEDROP_H_DV']=f2.iloc[37,17]

            if Distres_4 == 10:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'LONG_L']=f2.iloc[27,17]
                    sub1.at[itera,'LONG_L_DV']=f2.iloc[35,17]

                if Distres_4_dvm >= 0:
                    sub1.at[itera,'LONG_M']=f2.iloc[28,17]
                    sub1.at[itera,'LONG_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'LONG_H']=f2.iloc[29,17]
                    sub1.at[itera,'LONG_H_DV']=f2.iloc[37,17]


            if Distres_4 == 11:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'PATCH_L']=f2.iloc[27,17]
                    sub1.at[itera,'PATCH_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'PATCH_M']=f2.iloc[28,17]
                    sub1.at[itera,'PATCH_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'PATCH_H']=f2.iloc[29,17]
                    sub1.at[itera,'PATCH_H_DV']=f2.iloc[37,17]
            if Distres_4 == 12:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'POLAG_L']=f2.iloc[27,17]
                    sub1.at[itera,'POLAG_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'POLAG_M']=f2.iloc[28,17]
                    sub1.at[itera,'POLAG_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'POLAG_H']=f2.iloc[29,17]
                    sub1.at[itera,'POLAG_H_DV']=f2.iloc[37,17]
            if Distres_4 == 13:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'POTHOL_L']=f2.iloc[27,17]
                    sub1.at[itera,'POTHOL_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'POTHOL_M']=f2.iloc[28,17]
                    sub1.at[itera,'POTHOL_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'POTHOL_H']=f2.iloc[29,17]
                    sub1.at[itera,'POTHOL_H_DV']=f2.iloc[37,17]

            if Distres_4 == 14:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'RAIL_L']=f2.iloc[27,17]
                    sub1.at[itera,'RAIL_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'RAIL_M']=f2.iloc[28,17]
                    sub1.at[itera,'RAIL_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'RAIL_H']=f2.iloc[29,17]
                    sub1.at[itera,'RAIL_H_DV']=f2.iloc[37,17]
            if Distres_4 == 15:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'RUTTING_L']=f2.iloc[27,17]
                    sub1.at[itera,'RUTTING_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'RUTTING_M']=f2.iloc[28,17]
                    sub1.at[itera,'RUTTING_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'RUTTING_H']=f2.iloc[29,17]
                    sub1.at[itera,'RUTTING_H_DV']=f2.iloc[37,17]
            if Distres_4 == 16:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'SHOVING_L']=f2.iloc[27,17]
                    sub1.at[itera,'SHOVING_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'SHOVING_M']=f2.iloc[28,17]
                    sub1.at[itera,'SHOVING_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'SHOVING_H']=f2.iloc[29,17]
                    sub1.at[itera,'SHOVING_H_DV']=f2.iloc[37,17]
            if Distres_4 == 17:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'SLIPCRACK_L']=f2.iloc[27,17]
                    sub1.at[itera,'SLIPCRACK_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'SLIPCRACK_M']=f2.iloc[28,17]
                    sub1.at[itera,'SLIPCRACK_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'SLIPCRACK_H']=f2.iloc[29,17]
                    sub1.at[itera,'SLIPCRACK_H_DV']=f2.iloc[37,17]
            if Distres_4 == 18:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'SWELL_L']=f2.iloc[27,17]
                    sub1.at[itera,'SWELL_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'SWELL_M']=f2.iloc[28,17]
                    sub1.at[itera,'SWELL_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'SWELL_H']=f2.iloc[29,17]
                    sub1.at[itera,'SWELL_H_DV']=f2.iloc[37,17]
            if Distres_4 == 19:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'RAVEL_L']=f2.iloc[27,17]
                    sub1.at[itera,'RAVEL_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'RAVEL_M']=f2.iloc[28,17]
                    sub1.at[itera,'RAVEL_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'RAVEL_H']=f2.iloc[29,17]
                    sub1.at[itera,'RAVEL_H_DV']=f2.iloc[37,17]
            if Distres_4 == 20:
                if Distres_4_dvl >= 0:
                    sub1.at[itera,'WEATHERING_L']=f2.iloc[27,17]
                    sub1.at[itera,'WEATHERING_L_DV']=f2.iloc[35,17]
                if Distres_4_dvm >= 0:
                    sub1.at[itera,'WEATHERING_M']=f2.iloc[28,17]
                    sub1.at[itera,'WEATHERING_M_DV']=f2.iloc[36,17] 
                if Distres_4_dvh >= 0:
                    sub1.at[itera,'WEATHERING_H']=f2.iloc[29,17]
                    sub1.at[itera,'WEATHERING_H_DV']=f2.iloc[37,17]

            if Distres_5 == 1:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'ALLIGATOR_L']=f2.iloc[27,18]
                    sub1.at[itera,'ALLIGATOR_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'ALLIGATOR_M']=f2.iloc[28,18]
                    sub1.at[itera,'ALLIGATOR_M_DV']=f2.iloc[36,18]
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'ALLIGATOR_H']=f2.iloc[29,18]
                    sub1.at[itera,'ALLIGATOR_H_DV']=f2.iloc[37,18] 

            if Distres_5 == 2:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'BLEED_L']=f2.iloc[27,18]
                    sub1.at[itera,'BLEED_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'BLEED_M']=f2.iloc[28,18]
                    sub1.at[itera,'BLEED_M_DV']=f2.iloc[36,18]   
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'BLEED_H']=f2.iloc[29,18]
                    sub1.at[itera,'BLEED_H_DV']=f2.iloc[37,18]

            if Distres_5 == 3:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'BLOCK_L']=f2.iloc[27,18]
                    sub1.at[itera,'BLOCK_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'BLOCK_M']=f2.iloc[28,18]
                    sub1.at[itera,'BLOCK_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'BLOCK_H']=f2.iloc[29,18]
                    sub1.at[itera,'BLOCK_H_DV']=f2.iloc[37,18]


            if Distres_5 == 4:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'BUMP_L']=f2.iloc[27,18]
                    sub1.at[itera,'BUMP_L']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'BUMP_M']=f2.iloc[28,18]
                    sub1.at[itera,'BUMP_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'BUMP_H']=f2.iloc[29,18]
                    sub1.at[itera,'BUMP_H_DV']=f2.iloc[37,18]
            if Distres_5 == 5:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'CORRUGATION_L']=f2.iloc[27,18]
                    sub1.at[itera,'CORRUGATION_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'CORRUGATION_M']=f2.iloc[28,18]
                    sub1.at[itera,'CORRUGATION_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'CORRUGATION_H']=f2.iloc[29,18]
                    sub1.at[itera,'CORRUGATION_H_DV']=f2.iloc[37,18]
            if Distres_5 == 6:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'DEPRESSION_L']=f2.iloc[27,18]
                    sub1.at[itera,'DEPRESSION_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'DEPRESSION_M']=f2.iloc[28,18]
                    sub1.at[itera,'DEPRESSION_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'DEPRESSION_H']=f2.iloc[29,18]
                    sub1.at[itera,'DEPRESSION_H_DV']=f2.iloc[37,18]
            if Distres_5 == 7:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'EDGE_L']=f2.iloc[27,18]
                    sub1.at[itera,'EDGE_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'EDGE_M']=f2.iloc[28,18]
                    sub1.at[itera,'EDGE_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'EDGE_H']=f2.iloc[29,18]
                    sub1.at[itera,'EDGE_H_DV']=f2.iloc[37,18]
            if Distres_5 == 8:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'REFLECTION_L']=f2.iloc[27,18]
                    sub1.at[itera,'REFLECTION_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'REFLECTION_M']=f2.iloc[28,18]
                    sub1.at[itera,'REFLECTION_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'REFLECTION_H']=f2.iloc[29,18]
                    sub1.at[itera,'REFLECTION_H_DV']=f2.iloc[37,18]
            if Distres_5 == 9:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'LANEDROP_L']=f2.iloc[27,18]
                    sub1.at[itera,'LANEDROP_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'LANEDROP_M']=f2.iloc[28,18]
                    sub1.at[itera,'LANEDROP_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'LANEDROP_H']=f2.iloc[29,18]
                    sub1.at[itera,'LANEDROP_H_DV']=f2.iloc[37,18]

            if Distres_5 == 10:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'LONG_L']=f2.iloc[27,18]
                    sub1.at[itera,'LONG_L_DV']=f2.iloc[35,18]

                if Distres_5_dvm >= 0:
                    sub1.at[itera,'LONG_M']=f2.iloc[28,18]
                    sub1.at[itera,'LONG_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'LONG_H']=f2.iloc[29,18]
                    sub1.at[itera,'LONG_H_DV']=f2.iloc[37,18]


            if Distres_5 == 11:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'PATCH_L']=f2.iloc[27,18]
                    sub1.at[itera,'PATCH_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'PATCH_M']=f2.iloc[28,18]
                    sub1.at[itera,'PATCH_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'PATCH_H']=f2.iloc[29,18]
                    sub1.at[itera,'PATCH_H_DV']=f2.iloc[37,18]
            if Distres_5 == 12:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'POLAG_L']=f2.iloc[27,18]
                    sub1.at[itera,'POLAG_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'POLAG_M']=f2.iloc[28,18]
                    sub1.at[itera,'POLAG_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'POLAG_H']=f2.iloc[29,18]
                    sub1.at[itera,'POLAG_H_DV']=f2.iloc[37,18]
            if Distres_5 == 13:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'POTHOL_L']=f2.iloc[27,18]
                    sub1.at[itera,'POTHOL_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'POTHOL_M']=f2.iloc[28,18]
                    sub1.at[itera,'POTHOL_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'POTHOL_H']=f2.iloc[29,18]
                    sub1.at[itera,'POTHOL_H_DV']=f2.iloc[37,18]

            if Distres_5 == 14:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'RAIL_L']=f2.iloc[27,18]
                    sub1.at[itera,'RAIL_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'RAIL_M']=f2.iloc[28,18]
                    sub1.at[itera,'RAIL_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'RAIL_H']=f2.iloc[29,18]
                    sub1.at[itera,'RAIL_H_DV']=f2.iloc[37,18]
            if Distres_5 == 15:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'RUTTING_L']=f2.iloc[27,18]
                    sub1.at[itera,'RUTTING_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'RUTTING_M']=f2.iloc[28,18]
                    sub1.at[itera,'RUTTING_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'RUTTING_H']=f2.iloc[29,18]
                    sub1.at[itera,'RUTTING_H_DV']=f2.iloc[37,18]
            if Distres_5 == 16:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'SHOVING_L']=f2.iloc[27,18]
                    sub1.at[itera,'SHOVING_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'SHOVING_M']=f2.iloc[28,18]
                    sub1.at[itera,'SHOVING_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'SHOVING_H']=f2.iloc[29,18]
                    sub1.at[itera,'SHOVING_H_DV']=f2.iloc[37,18]
            if Distres_5 == 17:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'SLIPCRACK_L']=f2.iloc[27,18]
                    sub1.at[itera,'SLIPCRACK_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'SLIPCRACK_M']=f2.iloc[28,18]
                    sub1.at[itera,'SLIPCRACK_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'SLIPCRACK_H']=f2.iloc[29,18]
                    sub1.at[itera,'SLIPCRACK_H_DV']=f2.iloc[37,18]
            if Distres_5 == 18:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'SWELL_L']=f2.iloc[27,18]
                    sub1.at[itera,'SWELL_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'SWELL_M']=f2.iloc[28,18]
                    sub1.at[itera,'SWELL_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'SWELL_H']=f2.iloc[29,18]
                    sub1.at[itera,'SWELL_H_DV']=f2.iloc[37,18]
            if Distres_5 == 19:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'RAVEL_L']=f2.iloc[27,18]
                    sub1.at[itera,'RAVEL_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'RAVEL_M']=f2.iloc[28,18]
                    sub1.at[itera,'RAVEL_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'RAVEL_H']=f2.iloc[29,18]
                    sub1.at[itera,'RAVEL_H_DV']=f2.iloc[37,18]
            if Distres_5 == 20:
                if Distres_5_dvl >= 0:
                    sub1.at[itera,'WEATHERING_L']=f2.iloc[27,18]
                    sub1.at[itera,'WEATHERING_L_DV']=f2.iloc[35,18]
                if Distres_5_dvm >= 0:
                    sub1.at[itera,'WEATHERING_M']=f2.iloc[28,18]
                    sub1.at[itera,'WEATHERING_M_DV']=f2.iloc[36,18] 
                if Distres_5_dvh >= 0:
                    sub1.at[itera,'WEATHERING_H']=f2.iloc[29,18]
                    sub1.at[itera,'WEATHERING_H_DV']=f2.iloc[37,18]


            itera = itera+1
        sub3 = sub3.append(sub1,ignore_index=True)       
except:
    print("error"+file)
    #final = sub1.append(pd.read_excel(input_excel+"_"+"PCI_Increament_Fast.xlsx"), ignore_index=True)
sub.to_excel(input_excel+"\\"+file[0:-4]+"_"+"PCI_Increament_Fast.xlsx")
sub3.to_excel(input_excel+"\\"+file[0:-4]+"_"+"PCI_Increament_Slow.xlsx")
    #os.remove(path+"_"+"PCI_Increament_Fast.xlsx")